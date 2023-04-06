from typing import List, Dict, Any
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By


@dataclass
class SearchResult:
    header: str
    url: str


class GoogleScraper:
    def __init__(self, driver_path: str, browser: str):
        self.driver_path = driver_path
        if browser == 'chrome':
            self.browser = webdriver.Chrome(executable_path=self.driver_path)
        elif browser == 'firefox':
            self.browser = webdriver.Firefox(executable_path=self.driver_path)
        else:
            raise ValueError(f'Invalid browser specified: {browser}')

    def start_browser(self):
        self.browser.get('https://www.google.com')

    def close_browser(self):
        if self.browser is not None:
            self.browser.quit()

    def scrape(self, query: str) -> list[dict[str, Any]]:
        search_box = self.browser.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.submit()

        urls = self.browser.find_elements(
            By.XPATH, '//div[@id="search"]//div[@data-snf="x5WNvb"]//div[@class="yuRUbf"]/a')
        headers = self.browser.find_elements(
            By.XPATH, '//div[@id="search"]//div[@data-snf="x5WNvb"]//div[@class="yuRUbf"]//h3')

        results = []
        for url, header in zip(urls[:5], headers[:5]):
            results.append({'header': header.text, 'url': url.get_attribute('href')})

        return results

from utils.scraper import GoogleScraper
from config.settings import SEARCH_QUERY, BROWSER

if __name__ == '__main__':
    scraper = GoogleScraper(BROWSER['driver_path'], BROWSER['name'])
    scraper.start_browser()
    results = scraper.scrape(SEARCH_QUERY)
    scraper.close_browser()

    for result in results:
        print(result)

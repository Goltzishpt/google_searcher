import os

CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver')
FIREFOX_DRIVER_PATH = os.path.join(os.getcwd(), 'geckodriver')
SEARCH_QUERY = 'Python Developer'

BROWSER = {
    'name': 'chrome',  # or 'firefox'
    'driver_path': CHROME_DRIVER_PATH,  # or FIREFOX_DRIVER_PATH
}

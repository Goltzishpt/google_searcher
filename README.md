# Google Searcher
This is a simple Python project that scrapes Google search results using Selenium.

## Installation
- Clone the repository: git clone https://github.com/Goltzishpt/google_searcher
- Navigate to the project directory: cd google_searcher
- Install the required dependencies: pip install -r requirements.txt

## Usage
- Open config/settings.py and set the desired search query and browser options.
- Run main.py to start the scraper.
- The results will be printed to the console.

## Configuration
The scraper can be configured by editing the values in config/settings.py. The following options are available:

* **SEARCH_QUERY:** The search query to be used by the scraper.
* **BROWSER:** A dictionary containing the following options:
    + **name:** The name of the browser to be used (chrome or firefox). 
    + **driver_path:** The path to the browser driver executable.


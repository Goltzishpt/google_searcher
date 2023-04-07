# Google Searcher
This is a simple Python project that scrapes Google search results using Selenium.

## Installation
- Clone the repository: 
``` Copy code
git clone https://github.com/Goltzishpt/google_searcher
```
- Navigate to the project directory: 
``` bash Copy code
cd google_searcher
```
- Install the required dependencies: pip install -r requirements.txt

## Usage
- Open config/settings.py and set the desired search query and browser options. 
``` arduino Copy code
python main.py
```
to start the scraper.
- The results will be printed to the console.

## Configuration
The scraper can be configured by editing the values in config/settings.py. The following options are available:

* **SEARCH_QUERY:** The search query to be used by the scraper.
* **BROWSER:** A dictionary containing the following options:
    + **name:** The name of the browser to be used (chrome or firefox). 
    + **driver_path:** The path to the browser driver executable.


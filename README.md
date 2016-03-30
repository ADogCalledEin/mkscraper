# pimpmkscraper
Web Scraper for the status page of PimpMyKeyboard

### scraper.py
The bread of the process. This scrapes the page, then uses XPath and Pandas to spit out a csv of the page contents.

### run.sh
The butter of the process. This runs a command called csvtomd, which converts the csv into a markdown table.

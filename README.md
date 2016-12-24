# mkscraper
Scraper that gets the status page of keycap manufacturer's websites and formats it into a reddit post, or however I feel like formatting it. 

### scraper.py
The bread of the process. This scrapes the page, then uses XPath and Pandas to spit out a csv of the status table. 

### run.sh
The butter of the process. This runs a command called csvtomd, which converts the csv into a markdown table.

### Coming soon
1. Script to create the Reddit post to be uploaded
2. Getting it approved by the mods of /r/mk to have a stickied post of this stoof (loooooooooooooooooooooooooooooooooooooong way off).

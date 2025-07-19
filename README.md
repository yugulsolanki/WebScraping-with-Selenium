# WebScraping-with-Selenium

Selenium
-Can interact with dynamic content rendered by JavaScript
-Can click, scroll, and wait for elements like a real user
-Built-in .find_element() and .text are enough for simple scraping

Selenium + BeautifulSoup
-BeautifulSoup can’t handle JavaScript-rendered content by itself
-Used if you want easier HTML parsing after loading with Selenium
-Useful for complex HTML parsing like nested tags, attributes

**Use Selenium to load the page and BeautifulSoup to easily parse the HTML — especially when the structure is complex.

**To Run
1.create your env
2. pip install selenium beautifulsoup4
3. mkdir my_scraping_project
4. cd my_scraping_project
5. add chromedriver.exe inside it (it should same as of your chrome version)
6. python scraper.py
7. python selenium_with_beautifulsoup.py

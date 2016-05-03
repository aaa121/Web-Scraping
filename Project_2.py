# Web Scraping the practice of using computer programme to filter a
# webpage, gather data in useful format, and maintain the structure of the data
# LXML and REQUESTS are the two most effective modules for parsing/
# analyzing text in XML & HTML documents format. The two modules are better than urllib2 built-in module
from lxml import html
import requests
url1='http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html'
url='http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?617e8ad39ee9680b17895792f6a6949e'

webpage=requests.get(url)
tree=html.fromstring(webpage.content)
webpage.encoding='utf-8'
print(webpage.text)



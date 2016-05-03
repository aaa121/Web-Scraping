# Web Scraping the practice of using computer programme to filter a
# webpage, gather data in useful format, and maintain the structure of the data
# LXML and REQUESTS are the two most effective modules for parsing/
# analyzing text in XML & HTML documents format. The two modules are better than urllib2 built-in module
from lxml import html
import requests
url='http://econpy.pythonanywhere.com/ex/001.html'
url2='http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html'
url3='http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'


webpage=requests.get(url3).text
#print(webpage)
tree=html.fromstring(webpage)
#print(tree)

buyers=tree.xpath('//div[@title="buyer-name"]/text()')
prices=tree.xpath('//span[@class="item-price"]/text()')
print(buyers)
print(prices)


'''
# Another approach is Check the inspect the elements on Google chrome and copy the xpath as:
/html/body/div[2]/div
/html/body/div[2]/span
Then, edit as follows:

buyers=tree.xpath('/html/body/div/div/text()')
prices=tree.xpath('/html/body/div/span/text()')
print(buyers)
print(prices)
'''
'''
buyers2=tree.xpath('/html/body/div/div/text()')
prices2=tree.xpath('/html/body/div/span/text()')
print(buyers2)
print(prices2)

'''
'''
The xpath of the third url is:
//*[@id="lid-10722083"]/div/div[2]/div[2]/div[1]/p

//*[@id="lid-1050840"]/div/div[2]/div[2]/div[1]/p

//*[@id="lid-467426526"]/div/div[2]/div[2]/div[1]/p

Absolute path without sub-tree for the phone number is:
//*[@id="lid-467426526"]/div/div[2]/div[2]/div[1]/div
Edit the lid-XXXXX identifier and present as this:
phone-numbers=tree.xpath('//*[@id]/div/div[2]/div[2]/div[1]/div/text()')
print(phone)

# For TripAdvisor rating that couldn't be parsed using BeautifulSoup and Requests, use:
//*[@id="lid-467426526"]/div/div[2]/div[2]/div[1]/a[2]/span
Edit as follows:
ta_rating=tree.xpath('//*[@id]/div/div[2]/div[2]/div[1]/a[2]/span/text()')
print(ta_rating)
or
ta_rating=tree.xpath('//*[@id="lid-467426526"]/div/div[2]/div[2]/div[1]/a[2]/span/text()')
print(ta_rating)

#It will also return [] (null list). Same reason apply to this. The HTML content does not contain the trip advisor rating.
'''
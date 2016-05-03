url='http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA&page='
for i in range(1,11):
    print(i)
    page=url+str(i)
    print(page)
    from Web_Scraping_LXML_and_Requests_Modules import web_stat as ws
    web_stat=ws.web_stat(page)
def web_stat(url):
    import requests
    web=requests.get(url)
    status=web.status_code
    head=web.headers['content-type']
    encode=web.encoding
    return print('Status:{}\nHeader:{}\nEncode:{}\n'.format(status,head,encode))


url='http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'
url2='https://www.google.co.nz/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=donald%20trump%20news'
url3='http://www.latimes.com/politics/la-na-donald-trump-20160331-story.html'
web_stat(url3)
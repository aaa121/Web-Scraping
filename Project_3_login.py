import requests
'''
with requests.Session() as log:
    url='https://www.facebook.com/login/'
    usern='tripplehay777@yahoo.com'
    passw='soptc4112'
    log.get(url)
    csrftoken=log.cookies['csrftoken']
    log_details=dict(csrfmiddlewaretoken=csrftoken, email=usern, passw=passw)
    log.post(url,data=log_details)
    webpage=log.get('https://www.facebook.com/atanda.akinwande')
    print(webpage.content)
# It is better to request for FB API to have access to their server. Also, REQUESTS is very useful for parsing
JSON data relative to HTML documents
'''
url='https://www.facebook.com/login/'

web=requests.get(url)
print(web.headers['content-type'])
print(web.status_code)
print(web.encoding)
print(web.content)
print(web.text)



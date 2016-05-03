import urllib.request
url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as hopedalefile:
    hopedalefile.readline().strip().decode('utf-8')
    data=hopedalefile.readline().strip().decode('utf-8')
    while data.startswith('#'): # STARTSWITH not startwith
        data=hopedalefile.readline().strip().decode('utf-8')
    print(data)
    fox_sum=int(data)
    for data in hopedalefile:
        fox_sum +=int(data)
    print(fox_sum)
















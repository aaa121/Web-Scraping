from urllib import request as ur
url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with ur.urlopen(url) as webpage:
    for line in webpage:
        line=line.strip()
        line=line.decode('utf-8')
        print(line)

import urllib.request as ur
url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with ur.urlopen(url) as webpage:
    for line in webpage:
        line=line.strip()
        line=line.decode('utf-8')
        print(line)

from urllib import request as ur
url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with ur.urlopen(url) as webpage:
    data=webpage.readline().strip()
    data=webpage.readline().strip()
    data=webpage.readline().strip()
    sum_of_fox=0
    for line in webpage:
        line=line.strip().decode('utf-8')
        print(line)
        sum_of_fox += int(line)
    print(sum_of_fox)


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
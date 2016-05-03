# Exchange Rate Scraping

url='http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html'
import requests
from bs4 import BeautifulSoup
web=requests.get(url)
soup=BeautifulSoup(web.content,'lxml',from_encoding='utf-8')
soup.prettify()
#print(soup)

date=soup.find_all("main")
scrape_date=[]
for time in date:
    date2=time.find_all("h2")
    for time2 in date2:
        #print(time2.contents)
        scrape_date+=[time2.text]
scrape_date=scrape_date[0]
scrape_date=scrape_date[-12:]
print("Scrape Date:\t",scrape_date)

#Currency
currency=soup.find_all("table", {"class":"ecb-forexTable fullWidth"})
Curr_Name=[]
Curr_Ticker=[]
Spot_Rate=[]
for exch in currency:
    currency2=exch.find_all("tbody")
    for exch2 in currency2:
        #print(exch2.contents)
        currency3=exch2.find_all("td", {"class":"currency"})
        currency4=exch2.find_all("td", {"class":"alignLeft"})
        currency5=exch2.find_all("td", {"class":"spot number"})
        for exch4 in currency4:
            #print(exch4.text)
            data1=exch4.text
            Curr_Name+=[data1]
        for exch3 in currency3:
            #print(exch3.text)
            data2=exch3.text
            Curr_Ticker += [data2]
        for exch5 in currency5:
            #print(exch5.text)
            data3 = exch5.text
            Spot_Rate += [float(data3)]

#print(Curr_Name,Curr_Ticker,Spot_Rate,sep="\t\t")

# Fix the list to remove the last currency, "Icelandic krona - The last rate was published on 3 Dec 2008"
Curr_Name=Curr_Name[:-1]
Curr_Ticker=Curr_Ticker[:-1]
Spot_Rate=Spot_Rate[:]

#Covert to USD
usd_eur=1/Spot_Rate[0]
USD_rates=[]+[round(usd_eur,4)]
#print(USD_rates)
for i in range(1,len(Spot_Rate)):
    convert=Spot_Rate[i]*usd_eur
    USD_rates+=[round(convert,4)]

print()
print("Currency:\t",Curr_Name)
print()
print("Ticker:\t",Curr_Ticker)
print()
print("Spot Rate (EUR 1=):\t",Spot_Rate)
print()
print("Spot Rate (USD 1=):\t",USD_rates)

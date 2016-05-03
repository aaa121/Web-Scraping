from bs4 import BeautifulSoup
import requests
# The website to loop through
url='http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA&s=average_rating&page='
#Create Empty List for the variables of interest
Name=[]
Address=[]
Phone_Number=[]
YP_Rating=[]
Address_modified=[]
# It is only the first five pages that has consistent rating if you are using url without sortby rating otherwise, you can scrape in rating for the first 10 pages.
# uisng the url2 as shown in Project 4d
for i in range(1,11):
    # print(i)
    page=url+str(i)
    # print(page)
    # from Web_Scraping_LXML_and_Requests_Modules import web_stat as ws
    # web_stat=ws.web_stat(page)
    # print(web_stat)
    webpage = requests.get(page)
    soup = BeautifulSoup(webpage.content, 'lxml', from_encoding='utf-8')
    # For parsing the web content that has been derived using requests. A particular parser
    # can also be specified such as 'lxml'. Also the encoding format can be specified after checking or using the web_stat program.
    # soup.prettify()# Print this statemenet. The BeautifulSoup prettify function makes the webpage more readable. But it doesn't do much for the actual task).
    '''
    print(soup.find_all('a'))# This string function finds all the links <a> in the prettified content, soup
    '''
    g_data = soup.find_all("div", {"class": "info"})  # This search for the content  within the specified xpath or tree
    for item in g_data:  # Loop to slice each content into a list of the specified tag and printed in text or conetnt form.
        # print(item.text)
        # print(item.contents) # The elements as viewed using Chrome indicate that each element has three
        # children i.e. indicating the position of the variables of interest in each list.
        # print(item.contents[0].text)##This will print the first content that contains the name coffee shops. But each name ends with MENU
        # print(item.contents[1].text)  # This will print the second content that contain the address and phone number not seperated
        # print(item.contents[2].text)#This will print the third content that contains category of the coffee shops.
        # To correct for the identified issues, each child's sub-elements (grand-child) can be traced as follows:
        biz_name = item.contents[0].find_all("a", {"class": "business-name"})[0].text
        Name = Name + [biz_name]
        print(biz_name)  # (1). First do print(item.contents[0]) without text to identify the tag i.e. <h3>..</h3>;
        # (2) Go back to Chrome, identify the tag/element and class name that corresponds to the name without Menu i.e.<a>...class:"business-name"</a>;
        # (3) Identify the position i.e. first (0). Note, the word menu is in second position(1) and with <a>...class:"menu"</a>;
        # (4) .text the content search
        biz_adr = item.contents[1].find_all("p", {"class": "adr"})[0].text
        Address = Address + [biz_adr]
        print(biz_adr)  # This returns the address alone with zip code.
        '''
        print(item.contents[1].find_all("div", {"class": "phones phone primary"})[1].text)
        If you try input 0 or 1 as the last position indicating the next grandchild, it will return list index out of range.
        Then try the following:

        try:
            print(item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text)
        except:
            pass
        '''
        try:
            biz_phone = item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text
            print(biz_phone)  # Print the phone number
            Phone_Number = Phone_Number + [biz_phone]
        except:
            pass

        sub_data1 = item.find_all("div", {"class": "info-section info-primary"})
        # print(sub_data) #Print the list to know the number of elements in the list for position determination
        for rate1 in sub_data1:
            # print(rate1.text)
            # print(rate1.contents) # This indicates that rating is the second element in the list
            # This element has other sub-data as branches with other branches.
            sub_data2 = rate1.find_all("a", {"class": "rating"})
            for rate2 in sub_data2:
                # print(rate2.contents) # This content show that there is another branch inside the content
                sub_data3 = rate2.find_all("span", {"class": "count"})
                for rate3 in sub_data3:
                    # print(rate3.text) # This prints the ratings but with parenthesis. To remove run the following
                    p1 = rate3.text[1:]
                    # print(p1)
                    yellowrating = p1[:-1]
                    print(yellowrating)
                    YP_Rating = YP_Rating + [yellowrating]
            '''
            TripAdvisor rating is not in the HTML content. BeautifulSoup can't be used to parse the rating runing the following commands:
            sub2_data2 = rate1.find_all("a", {"class": "ta-rating-wrapper"})
            for rate4 in sub2_data2:
                sub2_data3=rate4.find_all("span", {"class": "ta-count"})
                for rate5 in sub2_data3:
                    print(rate5.contents)
            '''
        '''
        The next loops(rate1, rate2, and rate3) can be also be represented as:
        ssub_data=item.contents[1].find_all("a", {"class": "rating hasExtraRating"})
        #print(ssub_data)
        for rrate in ssub_data:
            #print(rrate.contents)
            print(rrate.find_all("span",{"class":"count"}))
            ssub_data2=rrate.find_all("span",{"class":"count"})
            for rrate2 in ssub_data2: #For each element in ssub_data2 list,
                print(rrate2.text)    # print the text
        '''
        '''
    # Re-defined the object based on the 2nd fix
    Name = Name[:(30*i)]
    Address_modified = Address_modified[:(30*i)]
    Phone_Number = Phone_Number[:]
    YP_Rating = YP_Rating[:(30*i)]
'''
#print(Address)
#The address has to be modified to remove the '\Xa' that prefixed the zip code '0900XX'
Address_modified=[]
for add in Address:
    #print(add[:-1])
    Address_modified+=[add[:-6]]

#Re-defined the object based on the 2nd fix
# It is only the first page that contains 5 adverts. It is only the first iterations affected
Name=Name[:30]+Name[35:]
Address_modified=Address_modified[:30]+Address_modified[35:]
Phone_Number=Phone_Number[:]
#It is only three of the adverts that has rating i.e position Advert 1, 4 and 5.
YP_Rating=YP_Rating[:30]+YP_Rating[33:]

#Print All Details
print(Name)
print(Address_modified)
print(Phone_Number)
print(YP_Rating)

print(len(Name),len(Address_modified),len(Phone_Number),len(YP_Rating),sep='\n')


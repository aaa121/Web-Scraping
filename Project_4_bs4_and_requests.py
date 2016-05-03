from bs4 import BeautifulSoup
import requests
url='http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'
webpage=requests.get(url)
soup=BeautifulSoup(webpage.content,'lxml',from_encoding='utf-8')# For parsing the web content that has been derived using requests. A particular parser
# can also be specified such as 'lxml'. Also the encoding format can be specified after checking or using the web_stat program.
#soup.prettify()# Print this statemenet. The BeautifulSoup prettify function makes the webpage more readable. But it doesn't do much for the actual task).
'''
print(soup.find_all('a'))# This string function finds all the links <a> in the prettified content, soup
'''
links=soup.find_all('a')
#Create a loop to search for each links or href:
for link in links: # The loop find all links on the page with the <a> tag and present each on a line
    #print(link) #It seperates the links to line
    #print(link.get('href')) # This prints the link inside of the unicode
    #print(link.text) # It returns the text content of the web without any href
    # print(link.get_text) #It prints the entire text with href. It is often not useful
    # print(link.text,links.get('href')) # This retrieves both text and its corresponding href
    # print("<a href='%s'>%s</a>"%(links.get('href'),links.text)) # Instead of printing the above,
    # this format method can be used to create a href tree.
    # print("<a href='{}'>{}</a>".format(link.get('href'),link.text)) # The above command line gives the same as this.
    '''
    This seems non-iterable due to Nontype nature of the loop.
    while link.get('href').startswith('http'):
        print("<a href='{}'>{}</a>".format(link.get('href'),link.text))

    if 'http' in link.get('href'):
        print("<a href='{}'>{}</a>".format(link.get('href'), link.text))
    '''
# To get the main information about each coffee cafe. Right click on the page on chrome and select inspect element.
# Figure out the tag that express the content of interest such as [<div class:"info">...</div>].
# Then, find the info between this tag common to all the search output
g_data=soup.find_all("div",{"class":"info"}) # This search for the content  within the specified xpath or tree

#Create Empty List for the variables of interest
Name=[]
Address=[]
Phone_Number=[]
YP_Rating=[]
for item in g_data: #Loop to slice each content into a list of the specified tag and printed in text or conetnt form.
    # print(item.text)
    # print(item.contents) # The elements as viewed using Chrome indicate that each element has three
    # children i.e. indicating the position of the variables of interest in each list.
    # print(item.contents[0].text)##This will print the first content that contains the name coffee shops. But each name ends with MENU
    # print(item.contents[1].text)  # This will print the second content that contain the address and phone number not seperated
    # print(item.contents[2].text)#This will print the third content that contains category of the coffee shops.
    # To correct for the identified issues, each child's sub-elements (grand-child) can be traced as follows:
    biz_name=item.contents[0].find_all("a",{"class":"business-name"})[0].text
    Name=Name+[biz_name]
    print(biz_name) # (1). First do print(item.contents[0]) without text to identify the tag i.e. <h3>..</h3>;
    # (2) Go back to Chrome, identify the tag/element and class name that corresponds to the name without Menu i.e.<a>...class:"business-name"</a>;
    # (3) Identify the position i.e. first (0). Note, the word menu is in second position(1) and with <a>...class:"menu"</a>;
    # (4) .text the content search
    biz_adr=item.contents[1].find_all("p", {"class": "adr"})[0].text
    Address=Address+[biz_adr]
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
        biz_phone=item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text
        print(biz_phone)#Print the phone number
        Phone_Number=Phone_Number+[biz_phone]
    except:
        pass

    sub_data1=item.find_all("div", {"class": "info-section info-primary"})
    #print(sub_data) #Print the list to know the number of elements in the list for position determination
    for rate1 in sub_data1:
        #print(rate1.text)
        # print(rate1.contents) # This indicates that rating is the second element in the list
        # This element has other sub-data as branches with other branches.
        sub_data2 = rate1.find_all("a", {"class": "rating hasExtraRating"})
        for rate2 in sub_data2:
            # print(rate2.contents) # This content show that there is another branch inside the content
            sub_data3=rate2.find_all("span",{"class": "count"})
            for rate3 in sub_data3:
                #print(rate3.text) # This prints the ratings but with parenthesis. To remove run the following
                p1=rate3.text[1:]
                #print(p1)
                yellowrating=p1[:-1]
                print(yellowrating)
                YP_Rating=YP_Rating+[yellowrating]
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

#print(Address)
#The address has to be modifed to remove the '\Xa' that prefixed the zip code '0900XX'
Address_modified=[]
for add in Address:
    #print(add[:-1])
    Address_modified+=[add[:-6]]

#Print All Details
print(Name)
print(Address_modified)
print(Phone_Number)
print(YP_Rating)

print(len(Name),len(Address_modified),len(Phone_Number),len(YP_Rating),sep='\n')



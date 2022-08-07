# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:46:43 2020

@author: Anonymous
"""
import pandas as pd 
import requests
from bs4 import BeautifulSoup

print("Libraries Imported......")

# Send Request 
url = 'https://www.flipkart.com/laptops/~cs-47csocz3bw/pr?sid=6bo%2Cb5g&collection-tab-name=High%20Performance%20Laptops&fm=neo%2Fmerchandising&iid=M_22c68482-05f1-48bc-b568-fc3c6abf3bb9_20.SEUXONG2OHZ6&ssid=w00yz9btrl929pmo1595415512266&otracker=hp_omu_New%2BLaunches_4_11.dealCard.OMU_New%2BLaunches_SEUXONG2OHZ6_6&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_New%2BLaunches_NA_dealCard_cc_4_NA_view-all_6&cid=SEUXONG2OHZ6'
page = requests.get(url)

# Formatting to user readable form 
soup = BeautifulSoup(page.text,'html.parser')

# laptop names 
def scraping(class_attribute):
    elements= list()
    elem = soup.find_all('div',class_ = class_attribute)
    for item in elem:
        elements.append(item.text)
    return elements

# user rating 

# laptop names     
laptops = scraping("_3wU53n")

# user rating
user_rating = scraping("hGSR34")

#Price and offer
original_price = scraping("_3auQ3N _2GcJzG")
offer_percentage = scraping("VGWI6T")
offer_price = scraping("_1vC4OE _2rQ-NK")

#Exchange 
exchange = scraping("_2nE8_R")
#exchange_elem = Soup.find_all('div',{'class':"_3_G5Wj",'class':"_3_G5Wj"})
#for i in range(len(exchange)):
    #if exchange[i].startswith('Upto'):
       #exchange[i]=(exchange[i]+ " " + exchange[i+1])
      # i=i+2
    #else:
        #i=i+1
# as the element upto..... and no cost emi split into 2 elements to merge and segregate 
exc=[]
i=0
while i<len(exchange):
    if (exchange[i]==('Upto ₹8,400 Off on Exchange') and exchange[i+1]=='No Cost EMI') :
        exc.append(exchange[i]+" " + exchange[i+1])
        i=i+2
    else:
        exc.append(exchange[i])
        i=i+1
            
#fassure = list()
#fassure_elem = Soup.find_all('div',{'class':'_3n6o0t'})

#for item in fassure_elem:
    #fassure.append(item.find('img').get('src'))   


  
# Create a pandas dataframe 
        
Final_Array = []
for name,rati,price1,offer,off_pri,exc_1 in zip(laptops,user_rating,original_price,offer_percentage,offer_price,exc):
    Final_Array.append({'Product_name':name,'User_rating':rati,'price':price1,'off_per':offer,'offer_price':off_pri,'exchange_and_EMI':exc_1})
    
df = pd.DataFrame(Final_Array)
    
df.to_excel("./Modified_Laptops_deatils_1.xlsx");



import pandas as pd 
import requests
from bs4 import BeautifulSoup
#Extracting each product specifications using their href link
link_text = ""
li=[]
for a in soup.find_all("a", href=True,class_="_31qSD5"):
    link_text = a.get('href')
    li.append("https://www.flipkart.com"+link_text)   # it will collect all href links 
    
spec_1 = []
spec_2 = []
def specification_extractor(specification_table_class_attribute):   
    for i in li:
        page = requests.get(i) 
        Soup = BeautifulSoup(page.text,'html.parser')
        laptops_elem = Soup.find_all(class_ = specification_table_class_attribute)
        for j in range(len(laptops_elem)):
            spec_2.append(pd.read_html(str(laptops_elem[j])))
            j=j+1
        spec_1.append(spec_2)
    return spec_1
    
specifications = specification_extractor("_3ENrHu")

    

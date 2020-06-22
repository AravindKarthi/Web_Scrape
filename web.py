import requests
import bs4
import csv
import pandas as pd
res=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
soup=bs4.BeautifulSoup(res.text,"lxml")
name=soup.select("._3wU53n")
price=soup.select("._1vC4OE._2rQ-NK")
details = pd.DataFrame(columns = ("Name", "Price"))
l=0
for i,j in zip(name,price):
    details.loc[l]=i.text,j.text;
    l+=1
    print(details)
    details.to_csv("Flipkart.csv")
    #details.to_excel("f.xlsx")
    #details.head()
    
    





    

# Importing required modules
from bs4 import BeautifulSoup
import requests
import csv

# function for fetching data from 2022 to 2024
def get_data(url,file):
    # sending request
    page = requests.get( url )
    
    # fetching the whole html page
    soup = BeautifulSoup( page.text , 'html.parser' )
    
    # storage list for data fetched
    datas = []

    # fetching the section where our required data is present
    a = soup.find( 'div' ,{ 'id' : 'autab3-2022' })

    # parsing through data of different teams
    for i in a.findAll( 'div' , attrs = { 'class' : 'ih-pt-tab-bg' }):
        # fetching the section where our required data of present team is present
        b = i.find( 'tbody' , attrs = { 'id' : 'pointsdata' })
        # parsing through each row of data
        for j in b.findAll( 'tr' ):
            # dictionary to help identifying columns
            data={}
            # as all the data of each row were under different tags of same name
            k= j.findAll( 'td' )
            # fetcing data
            data[ "Sr. No." ] = int( k[0].text )
            data[ "Pl. Name" ] = k[1].text.strip( '\n' )
            data[ "Price" ] = int( ''.join( k[4].text.split(",") ))
            data[ "Sold to" ] = i.h2.text
            # storing data in the list
            datas.append(data)

    # opening file to write
    with open( file ,'w') as f:
        #setting columns
        w = csv.DictWriter(f,['Sr. No.','Pl. Name','Price','Sold to'])
        w.writeheader()
        for data in datas:
            # writing each row
            w.writerow(data)

# For fetching data from 2021 as the format of this page was different from others
# same as in function "get_data"
page = requests.get( 'https://www.iplt20.com/auction/2021' )
soup = BeautifulSoup( page.text , 'html.parser' )
datas = []
a = soup.find( 'div' ,{ 'id' : 'autab3' })

for i in a.findAll( 'div' , attrs = { 'class' : 'ih-pt-tab-bg' }):
    b = i.find( 'tbody' , attrs = { 'id' : 'pointsdata' })
    for j in b.findAll( 'tr' ):
        data={}
        k= j.findAll( 'td' )
        data[ "Sr. No." ] = int( k[0].text )
        data[ "Pl. Name" ] = k[1].text.strip( '\n' )
        data[ "Price" ] = int( ''.join( k[3].text.split(",") ))
        data[ "Sold to" ] = i.h2.text
        datas.append(data)

with open( 'storage/player_data1.csv' ,'w') as f:
    w = csv.DictWriter(f,['Sr. No.','Pl. Name','Price','Sold to'])
    w.writeheader()
    for data in datas:
        w.writerow(data)


url3 = 'https://www.iplt20.com/auction/2024'
url2 = 'https://www.iplt20.com/auction/2023'
url1 = 'https://www.iplt20.com/auction/2022'

get_data(url1,'storage/player_data2.csv')
get_data(url2,'storage/player_data3.csv')
get_data(url3,'storage/player_data4.csv')

# For fetching data from 2025 as the format of this page was different from others
# same as in function "get_data"
page = requests.get( 'https://www.iplt20.com/auction/2025' )
soup = BeautifulSoup( page.text , 'html.parser' )
datas = []
a = soup.find( 'div' ,{ 'id' : 'autab3-2022' })

for i in a.findAll( 'div' , attrs = { 'class' : 'ih-pt-tab-bg' }):
    b = i.find( 'tbody' , attrs = { 'id' : 'pointsdata' })
    for j in b.findAll( 'tr' ):
        data={}
        k= j.findAll( 'td' )
        data[ "Sr. No." ] = int( k[0].text )
        data[ "Pl. Name" ] = k[1].text.strip( '\n' )
        data[ "Price" ] = int( ''.join( k[3].text.split(",") ))
        data[ "Sold to" ] = i.h2.text
        datas.append(data)

with open( 'storage/player_data5.csv' ,'w') as f:
    w = csv.DictWriter(f,['Sr. No.','Pl. Name','Price','Sold to'])
    w.writeheader()
    for data in datas:
        w.writerow(data)


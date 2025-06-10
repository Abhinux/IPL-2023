# Importing required modules
import matplotlib.pyplot as mpl
import numpy as np
import csv

# Lists to carry collective data of every year
CSK=[]
GT=[]
LSG=[]
MI=[]
RCB=[]
RR=[]
KKR=[]
PK=[]
SH=[]
DC=[]


# function to sum the spendings and appending to their respective list
def sum_of_team(file):
    global CSK,KKR,DC,GT,SH,RCB,MI,PK,LSG,RR
    with open(file) as f:
        # read the file
        reader = csv.DictReader(f)
        # variables to store the sum of spendings of each team
        csk=0
        gt=0
        lsg=0
        mi=0
        rcb=0
        rr=0
        kkr=0
        pk=0
        sh=0
        dc=0
        # read each row
        for row in reader:
            # checking "Sold to" field to know which team bought the player
            match row['Sold to']:
                case " Chennai Super Kings":
                    csk+=int(row['Price'])
                case " Delhi Capitals":
                    dc+=int(row['Price'])
                case " Gujarat Titans":
                    gt+=int(row['Price'])
                case " Kolkata Knight Riders":
                    kkr+=int(row['Price'])
                case " Lucknow Super Giants":
                    lsg+=int(row['Price'])
                case " Mumbai Indians":
                    mi+=int(row['Price'])
                case " Punjab Kings":
                    pk+=int(row['Price'])
                case " Rajasthan Royals":
                    rr+=int(row['Price'])
                case " Royal Challengers Bangalore"|" Royal Challengers Bengaluru":
                    rcb+=int(row['Price'])
                case " Sunrisers Hyderabad":
                    sh+=int(row['Price'])
    # Append the sum to their respective lists
    # Divided by 10,00,00,000 as the number was huge
    CSK.append(csk/100000000)
    RR.append(rr/100000000)
    KKR.append(kkr/100000000)
    LSG.append(lsg/100000000)
    MI.append(mi/100000000)
    PK.append(pk/100000000)
    DC.append(dc/100000000)
    RCB.append(rcb/100000000)
    SH.append(sh/100000000)
    GT.append(gt/100000000)

# run the function for each year
sum_of_team('storage/player_data1.csv')
sum_of_team('storage/player_data2.csv')
sum_of_team('storage/player_data3.csv')
sum_of_team('storage/player_data4.csv')
sum_of_team('storage/player_data5.csv')

Team_data=[]

def set_team_data(team:str,team_data:list):
    Team={}
    Team["Team"]=team
    Team["2021"]=team_data[0]
    Team["2022"]=team_data[1]
    Team["2023"]=team_data[2]
    Team["2024"]=team_data[3]
    Team["2025"]=team_data[4]
    Team_data.append(Team)

set_team_data("Chennai Super Kings",CSK)
set_team_data("Rajasthan Royals",RR)
set_team_data("Mumbai Indian",MI)
set_team_data("Kolkata Knight Riders",KKR)
set_team_data("Lucknow Super Giants",LSG)
set_team_data("Punjab Kings",PK)
set_team_data("Delhi Capitals",DC)
set_team_data("Royal Challengers Bangalore",RCB)
set_team_data("Sunrisers Hyderabad",SH)
set_team_data("Gujrat Titans",GT)

with open( 'storage/Team_data.csv' ,'w') as f:
    w = csv.DictWriter(f,['Team','2021','2022','2023','2024','2025'])
    w.writeheader()
    for data in Team_data:
        w.writerow(data)

# X-axis contains year
X_Value=[2021,2022,2023,2024,2025]

# setting graph Title
mpl.title('Spendings per year of each team\n\n')
mpl.axis('off')

# Setting subplots for each team

# For Chennai Super Kings
mpl.subplot(4,5,1)
mpl.grid("on")
mpl.plot(X_Value,CSK, color='y',marker='o',label='CSK',ls=':')
mpl.title("CSK")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Kolkata Knight Riders
mpl.subplot(4,5,3)
mpl.grid("on")
mpl.plot(X_Value,KKR, color='purple',marker='o',label='KKR',ls=':')
mpl.title("KKR")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Mumbai Indians
mpl.subplot(4,5,5)
mpl.grid("on")
mpl.plot(X_Value,MI, color='#0000ff',marker='o',label='MI',ls=':')
mpl.title("MI")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Delhi Capitals
mpl.subplot(4,5,7)
mpl.grid("on")
mpl.plot(X_Value,DC, color='#c92d2d',marker='o',label='DC',ls=':')
mpl.title("DC")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Rajasthan Royals
mpl.subplot(4,5,9)
mpl.grid("on")
mpl.plot(X_Value,RR, color='#d909a5',marker='o',label='RR',ls=':')
mpl.title("RR")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Punjab Kings
mpl.subplot(4,5,11)
mpl.grid("on")
mpl.plot(X_Value,PK, color='#ff0000',marker='o',label='PK',ls=':')
mpl.title("PK")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Royal Challengers Banglore
mpl.subplot(4,5,13)
mpl.grid("on")
mpl.plot(X_Value,RCB, color='#800707',marker='o',label='RCB',ls=':')
mpl.title("RCB")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Gujrat Titans
mpl.subplot(4,5,15)
mpl.grid("on")
mpl.plot(X_Value,GT, color='#9f950a',marker='o',label='GT',ls=':')
mpl.title("GT")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Lucknow Super Giants
mpl.subplot(4,5,17)
mpl.grid("on")
mpl.plot(X_Value,LSG, color='#01c4a0',marker='o',label='LSG',ls=':')
mpl.title("LSG")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For Sunrisers Hyderabad
mpl.subplot(4,5,19)
mpl.grid("on")
mpl.plot(X_Value,SH, color='orange',marker='o',label='SH',ls=':')
mpl.title("SH")
mpl.xlabel("Years")
mpl.ylabel("Spending in 10 crores")

# For displaying the resulting graph
mpl.show()
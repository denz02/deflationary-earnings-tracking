# This script doesn't work fully it records number changes but it doesn't have the price so it is work in progress
# Tip jar address if you appreciate this script my safemoon address 0x32D2da7308516e46D38EC638FE2144dE2250B7D3 Thank You 
#
#Big thanks again to Sam Brimhall
#After installing python you also need to install module requests and pandas to do this simple type in command prompt 
# following command 'python -m pip install requests' and python -m pip install pandas
########################## INSERT YOUR INFO AS NEEDED BELOW ################################################

#Contract Address - the token you wish to read value from on Etherscan.io (set to Saitamu Inu, If you want a different token change it)
contractAddr = '0x8b3192f5eebd8579568a2ed41e6feb402f93f73f'

#Wallet Address - INSERT YOUR PUBLIC WALLET ADDRESS HERE
walletAddr = ''

#API Key for etherscan - MAKE AND ACCOUNT https://etherscan.io verify your account then log back in to https://etherscan.io and on the left hand side API-KEY menu and generate a new API key. INSERT THAT API KEY HERE
ethAPIkey = ''


#Location and file name example below
sfmoonfile = 'C:/temp/Ethereum-DailyTracker.csv'

#How the date gets recorded in Australia it is dd/mm/yyyy
datefor = "%d/%m/%Y"

#To get rid of an error it needs to have a start balance this figure is just used as movement between second row please use just whole numbers
# eg 1,000.34 please enter 1000 different regions type thousand separator differently and it causing issues 
startbal = '1'

#To get net sale figure default 12% slipage is used 
sfslipageper = '12'

#If you want to change the column header name
sfheader1 = 'Date'
sfheader2 = 'Opening Balance'
sfheader3 = 'Daily Gain'
sfheader4 = 'Closing Balance'
sfheader5 = '% Increase'
sfheader6 = 'Price'
sfheader7 = 'Earned Reflactions'
sfheader8 = 'Price From'
sfheader9 = 'Gross Value'
sfheader10 = 'Net Value'

# if you want to change text
sftextp = 'Pancakeswap price US'

############################################################################################################

###PROGRAM CODE BELOW - DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING###
############################################################################################################

###PROGRAM CODE BELOW - DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING###
import requests
import json
import time
import csv
import pandas as pd
import os
from datetime import date
from pandas import DataFrame
import locale
locale.setlocale(locale.LC_ALL, '')
col_names = [sfheader1,
             sfheader2,
             sfheader3,
             sfheader4,
             sfheader5,
             sfheader6,
             sfheader7,
             sfheader8,
             sfheader9,
             sfheader10,]

path = sfmoonfile
if not os.path.exists(path):
    with open(path, 'w') as f:
        value = sfheader1 + "," + sfheader2 + "," + sfheader3 + "," + sfheader4 + "," + sfheader5 + "," + sfheader6 + "," + sfheader7 + "," + sfheader8 + "," + sfheader9 + "," + sfheader10
        s = str(value)
        f.write(s + '\n' + ',' + ',' + ',' + startbal + '\n')
        f.close()
d_data = pd.read_csv(sfmoonfile,names=col_names,encoding='UTF-8',index_col=False,skiprows=[0], low_memory=False)
series = d_data[sfheader4]
bottom = series.values[-1]
print (bottom)
#Testing to see if there is a comma 
x = bottom
try:
	print ("It is a number " , float(x))
except:
    bottom = bottom.replace(',', '')
    print (bottom)
today = date.today()
bscResponse = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=' + contractAddr + '&address=' + walletAddr + '&tag=latest&apikey=' + bscAPIkey)
print (bscResponse)
#ethData = bscResponse.json() if bscResponse and bscResponse.status_code == 200 else None
#safemoonAmount = bscData["result"]
#safemoonAmount = float(safemoonAmount)
#safemoonAmount = safemoonAmount / 1000000000
## This produces correct result https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x8b3192f5eebd8579568a2ed41e6feb402f93f73f&address=0x78778d5b0132643d58df4acb2cd24c1c106d50a6&tag=latest&apikey=Z7VXZNX3CCH63DNABQVEY2BSRUH5J382BP
ethResponse = requests.get('https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=' + contractAddr + '&address=' + walletAddr + '&tag=latest&apikey=' + ethAPIkey)
print (ethResponse)
ethData = ethResponse.json() if ethResponse and ethResponse.status_code == 200 else None
safemoonAmount = ethData["result"]
print ('correct amount')
print (safemoonAmount)
safemoonAmount = float(safemoonAmount)
safemoonAmount = safemoonAmount / 1000000000
print (safemoonAmount)
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")  
d1 = today.strftime(datefor)       
#pkResponse = requests.get('https://api.pancakeswap.info/api/v2/tokens')
#pkData = pkResponse.json() if pkResponse and pkResponse.status_code == 200 else None
#safemoonPrice = pkData["data"][contractAddr]["price"]
#print("SafeMoon Price: " + safemoonPrice)
safemoonPrice = 100
sfValue = safemoonAmount * float(safemoonPrice)
sfValue = str(sfValue)
sfOpening = float(bottom)
#print (sfOpening)
sfReflac =  safemoonAmount - sfOpening
#print (sfReflac)
sfClosing = safemoonAmount
sfReflacPer = sfReflac / sfOpening
#print (sfReflacPer)
sfslipagepercalint = float(sfslipageper)
sfslipagepercal = (100 - sfslipagepercalint) 
print (sfslipagepercal)
sfslipagepercal1 = (sfslipagepercal/100)
print (sfslipagepercal1)
sfSlipage = float(sfValue) * float(sfslipagepercal1)
print (sfSlipage)
sfReflacEarn = sfReflac * float(safemoonPrice)
#data = d1,safemoonAmount, sfReflac, sfClosing, sfReflacPer, safemoonPrice, sfValue,'' ,'','Pancakeswap price US', sfSlipage
data = {sfheader1 : [d1],
        sfheader2 : [sfOpening],
        sfheader3 : [sfReflac],
        sfheader4 : [sfClosing],
        sfheader5 : [sfReflacPer],
        sfheader6 : [safemoonPrice],
        sfheader7 : [sfReflacEarn],
        sfheader8 : [sftextp],
        sfheader9 : [sfValue],
        sfheader10 : [sfSlipage]
        }
df = pd.DataFrame(data, columns= [sfheader1,sfheader2,sfheader3,sfheader4,sfheader5,sfheader6,sfheader7,sfheader8,sfheader9,sfheader10])
df.to_csv (sfmoonfile, mode='a',index = False, header=False)

exit()

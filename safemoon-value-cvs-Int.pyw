#############################
# Tip jar address if you appreciate this script 0x32D2da7308516e46D38EC638FE2144dE2250B7D3 Thank You 
#
#Big thanks again to Sam Brimhall
#After installing python you also need to install module requests and pandas to do this simple type in command prompt 
# following command 'python -m pip install requests' and python -m pip install pandas
########################## INSERT YOUR INFO AS NEEDED BELOW ################################################

#Contract Address - the token you wish to read value from on Bscscan (set to Safemoon, DO NOT CHANGE)
contractAddr = '0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3'

#Wallet Address - INSERT YOUR PUBLIC WALLET ADDRESS HERE 
walletAddr = ''

##API Key for openexchange they offer free plans - MAKE AND ACCOUNT https://openexchangerates.org/
openExcAddr = ''


#API Key for bscscan - MAKE AND ACCOUNT https://bscscan.com/register verify your account then go to https://bscscan.com/myapikey and generate a new API key. INSERT THAT API KEY HERE
bscAPIkey = ''

#Location and file name example below
sfmoonfile = 'C:/CRYPTO/Safemoon-Tracker.csv'

#How the date gets recorded in Australia it is dd/mm/yyyy
datefor = "%d/%m/%Y"

#Foreign Exchange Country Code substitute with your own country code
sfExchanCountCod = "AUD"

#To get rid of an error it needs to have a start balance this figure is just used as movement between second row please use just whole numbers
# eg 1,000.34 please enter 1000 different regions type thousand separator differently and it causing issues 
startbal = '1000'

#To get net sale figure default 12% slipage is used 
sfslipageper = '12'

#If you want to change the column header name
sfheader1 = 'Date'
sfheader2 = 'Opening Balance'
sfheader3 = 'Daily Gain'
sfheader4 = 'Closing Balance'
sfheader5 = '% Increase'
sfheader6 = 'Price ' + sfExchanCountCod
sfheader7 = 'Earned Reflactions '  + sfExchanCountCod
sfheader8 = ' Gross Value ' + sfExchanCountCod
sfheader9 = 'Net Value ' + sfExchanCountCod
sfheader10 = 'USA ' + sfExchanCountCod + ' Rate' 
sfheader11 = 'USD Price'
sfheader12 = 'Price From'

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
             sfheader10,
	     sfheader11,
             sfheader12,]

path = sfmoonfile
if not os.path.exists(path):
    with open(path, 'w') as f:
        value = sfheader1 + "," + sfheader2 + "," + sfheader3 + "," + sfheader4 + "," + sfheader5 + "," + sfheader6 + "," + sfheader7 + "," + sfheader8 + "," + sfheader9 + "," + sfheader10 + "," + sfheader11 + "," + sfheader12
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

#########
bscResponse = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=' + contractAddr + '&address=' + walletAddr + '&tag=latest&apikey=' + bscAPIkey)
bscData = bscResponse.json() if bscResponse and bscResponse.status_code == 200 else None
safemoonAmount = bscData["result"]
safemoonAmount = float(safemoonAmount)
safemoonAmount = safemoonAmount / 1000000000
#####################
## Exchange rates using openexchangerates.org
####
url = 'https://openexchangerates.org/api/latest.json?app_id=' + openExcAddr
 
response = requests.get(url)
data = response.text
parsed = json.loads(data)

 
rates = parsed["rates"]
 
for currency, rate in rates.items():
    print("USA =",currency, rate)



USABase_rate = parsed["rates"][sfExchanCountCod]
print(str(USABase_rate))

# dd/mm/YY
#d1 = today.strftime("%d/%m/%Y")  
d1 = today.strftime(datefor)       
pkResponse = requests.get('https://api.pancakeswap.info/api/v2/tokens')
pkData = pkResponse.json() if pkResponse and pkResponse.status_code == 200 else None
safemoonPrice = pkData["data"][contractAddr]["price"]
#print("SafeMoon Price: " + safemoonPrice)
sfValue = safemoonAmount * float(safemoonPrice)
sfValue = float(sfValue) * USABase_rate
sfOpening = float(bottom)
#print (sfOpening)
sfReflac =  safemoonAmount - sfOpening
#print (sfReflac)
sfClosing = safemoonAmount
sfReflacPer = sfReflac / sfOpening
safemoonPriceConv = float(safemoonPrice) * USABase_rate
#print (sfReflacPer)
sfslipagepercalint = float(sfslipageper)
sfslipagepercal = (100 - sfslipagepercalint) 
print (sfslipagepercal)
sfslipagepercal1 = (sfslipagepercal/100)
print (sfslipagepercal1)
sfSlipage = float(sfValue) * float(sfslipagepercal1)
print (sfSlipage)
sfReflacEarn = sfReflac * float(safemoonPrice)

data = {sfheader1 : [d1],
        sfheader2 : [sfOpening],
        sfheader3 : [sfReflac],
        sfheader4 : [sfClosing],
        sfheader5 : [sfReflacPer],
        sfheader6 : [safemoonPriceConv],
        sfheader7 : [sfReflacEarn],
        sfheader8 : [sfValue],
        sfheader9 : [sfSlipage],
        sfheader10 : [USABase_rate],
        sfheader11 : [safemoonPrice],
        sfheader12 : [sftextp]
        
        }
df = pd.DataFrame(data, columns= [sfheader1,sfheader2,sfheader3,sfheader4,sfheader5,sfheader6,sfheader7,sfheader8,sfheader9,sfheader10,sfheader11,sfheader12])
df.to_csv (sfmoonfile, mode='a',index = False, header=False)

exit()

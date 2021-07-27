# safemoon-tracker


A simple python based tracker for cryptocurrency price, wallet balance and wallet value. 

For use tracking the Safemoon cryptocurrency based on the BSCscan and Pancakeswap API's. Trust wallet doesn't give you the accurate value figure as it is using prices from different exchanges and they are irrelevant if you are using pancakeswap. 

This project does not work out of the box. If you wish to use it to track your own wallet, you must set it up yourself. There are comments within the source code explaining how to do this, it is also outlined below:

1: You must set up your own bscscan API key to access bscscan data. Create an account on bscscan found here: https://bscscan.com/apis

2: Once your account is set up, generate an API key and copy it. Open the source code in your editor of choice (Notepad is ok) and insert the key in the designated variable as outlined by the comments. You can generate your API key here: https://bscscan.com/myapikey click on left hand side you will see API-KEY click on Add and then copy that key to the script. 

3: The other thing you need is your public Safemoon wallet address. You can find this on Trustwallet and Metamask easily, by navigating to the 'receive' page on your wallet and copying your address. Paste it in the designated variable within the source code. You can easily use someone elses address to test it out all the addresses are public and you can find them here https://www.bscscan.com/token/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3#balances if you also type your address in search bar you can see that anyone can see it as it is a public address. Never ever give your 12 word or 24 word pass phrase to anyone as that is how people get scammed. 

4. To use the foreign exchange you need to register https://openexchangerates.org/signup and obtain API Key above the paying plans there is a click button for Free Plans it is very easy process. 

5: You need to have python installed on your system to work if you don't python can be downloaded from python.org and when you are installing it click Add Python 3.x to PATH once it is installed you need to install three modules to do that open command prompt and type 'python -m pip install requests','python -m pip install pandas' 'python -m pip install openpyxl' and 'python -m pip install xlsxwriter'. You can set up for daily downloads in task scheduler one item that you need to change in settings is 'Stop the task if it runs longer than: to 1 hour. For some reason task scheduler is reporting that it is running when it is not. If you are having issue saving check in general tab maybe the user is wrong the user the user should be system. 

NOTE: This is not a compiled EXE. It's simply a .pyw file, so you must have python installed to run it. Also, note that putting your public wallet key into this program is 100% safe. Nobody can access your coin just with your public key. You can see the entire source code, so if you are afraid anything fishy is being pulled go ahead and look through it to see how the program uses your public key.

There are currently four files I have made two CSV and two excel files. There is an international version that uses foreign exchange rates 

If you want to reach me I am available on reddit as user Odd_Cat_5975

A big thanks goes to Sam Brimhall as he has done the hard yards so a big thank you to him

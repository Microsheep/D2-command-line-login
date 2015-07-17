from bs4 import BeautifulSoup
import requests
import getpass

### input account ###
account_name=""
account_password=""
account_name = input("Enter username ___@nctu.edu.tw: ")
account_name = getpass.getpass("Enter Password: ")
### get magic ###
res = requests.get("http://www.google.com")
raw_data = BeautifulSoup(res.text, "lxml")
reply = raw_data.find_all('input')[0]["value"]
### make payload ###
payload = {'magic': reply,'username': account_name+'@nctu.edu.tw', 'password': account_password, '4Tredir': "/"}
### post payload ###
r = requests.post("http://www.google.com", data=payload)
print("Payload sent! XD")
print(r)
### check if success ###
cres = requests.get("http://www.google.com")
craw_data = BeautifulSoup(cres.text, "lxml")
creply = raw_data.find_all('input')[0]["value"]
if creply=="Big5":
    print("Success!")
else:
    print("Failed with unknown reason!")


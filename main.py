import get as get
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import smtplib
import time

URL = 'https://www.amazon.com/Tracfone-Apple-iPhone-Prepaid-Smartphone/dp/B07QHQ2JJC/ref=sr_1_1?keywords=iphone+5&qid=1573254443&sr=8-1'

#you can check your user agent by just typing it in google search.
headers = {
    "User-Agent": 'Here_you_copy/paste_your_user_agent'}

def check_price():

    page = requests.get(URL, headers=headers)

    #I am making soup2 to trick amazon because of the javascript.
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text() #source code of the page
    price = soup2.find(id="priceblock_ourprice").get_text() #source code of the page

    converted_price = float(price[1:6]) #in order to show first 6 char

    if(converted_price < 120:
        send_mail()

    print(title.strip())
    print(converted_price)

    if(converted_price < 120):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #passing verification
    server.ehlo() #connection
    server.starttls() #encrypting connection
    server.ehlo()

    server.login('YourEmail@mail.com', 'YourPassword') #I recommend a two way verification

    subject = 'Price fell down!'
    body = 'Check the amazon link: https://www.amazon.com/Tracfone-Apple-iPhone-Prepaid-Smartphone/dp/B07QHQ2JJC/ref=sr_1_1?keywords=iphone+5&qid=1573254443&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Sending@mail.com', #from
        'Receiving@mail.com', #to
        msg #msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit() #close the server

#create a loop to run the script for a period of time, endless :)
while (True):
    check_price()
    time.sleep(60 * 60)
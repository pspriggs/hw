import time
import threading
import datetime
import smtplib
import socket
import json
import requests
import pytemperature
import pyzmail


jsonDataasPythonValue = requests.get('http://api.openweathermap.org/data/2.5/weather?q=colorado+springs&appid=9737923cb9003cf43725c14250599994')
stringsOfJsonData = json.loads(jsonDataasPythonValue.text)
print('Start of program.')
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
print(smtpObj.ehlo())
smtpObj.starttls()
#smtpObj.starttls()
print(smtpObj.login('sammythesp3rmy@yahoo.com', 'Lfd346712@'))

currentTemp = pytemperature.k2f(stringsOfJsonData['main']['temp'])
print(currentTemp)
messageTwo = "Bring a coat, it is cold at " + str(currentTemp) + ' degrees right now'
messageThree = "Wear something light, it is hot today"
if float(currentTemp) < 68:
    message = "Subject: Here is the weather for the day \n\n" \
          "This is the temperature of " + str(stringsOfJsonData['name']) + '\n' + messageTwo

print(message)


print(smtpObj.sendmail('sammythesp3rmy@yahoo.com', 'sammythesp3rmy@yahoo.com', message))
#print(smtpObj.ehlo())
#print(smtpObj.starttls())
tomorrowmorning = datetime.datetime(2019, 4, 17, 15, 46, 0)
#print(smtpObj.quit())



def takeANap():
    while datetime.datetime.now() < tomorrowmorning:
        time.sleep(1)
        print('Not time yet')
    else:
        print('it is time')

    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of program.')

import pywhatkit
from datetime import datetime

now = datetime.now()

mobile = input("Enter Mobile No of Receiver : ")
message = input("Enter Message you wanna send : ")
hour = int(input("Enter hour : "))  # Convert hour to integer
minute = int(input("Enter minute : "))  # Convert minute to integer

pywhatkit.sendwhatmsg(mobile,message,hour,minute,)

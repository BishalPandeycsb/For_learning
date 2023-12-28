from time import gmtime, strftime          #inbuilt libraries
import time
def timezone(hour,min,sec,time_of_day):    # function to display the user input and corresponding gmt time
    print("Output of user input :-->" + hour + ":" + min + ":" + sec + ' ' + time_of_day)
    print("\nGMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
    print("Local: " + strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))

hour=input("Enter hour")
min=input("Enter min ")
sec=input("Enter sec")
time_of_day=input("Enter whether it's Am or Pm")

timezone(hour,min,sec,time_of_day)             #function call


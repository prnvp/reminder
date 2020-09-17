import time
from datetime import datetime
from datetime import timedelta
from win10toast import ToastNotifier 

def askTime():
    print("\nPlease input the time at which you want to be reminded : ")
    print("(According to 12 hour clock)")
    try:
        h = int(input("\nEnter hour of the time you want to be reminded : "))
        m = int(input("Enter minute at which you want to reminded : "))
        s = int(input("Enter second at which you want to be reminded : "))
        t = input("AM or PM? - ")
    except:
        print("Please enter a valid entry")
    return h,m,s,t

def askMessage():
    message = input("\nPlease enter a message for the reminder : ")
    return message

def convertToSecond(hour,minute,second):
    return hour*3600+minute*60+second

print("\nWelcome to reminder app")
permission = "c"
while permission == "c":
    print("Current time is : ",time.strftime("%H : %M : %S",time.localtime()))
    h,m,s,t = askTime()
    if 0<=h<=12 and 0<=m<60 and 0<=s<60 and (t.lower() == 'pm' or t.lower() == 'am'):
        real_h = h
        if t.lower() == "pm":
            h = h + 12
        current_hour = int(datetime.now().strftime("%H"))
        current_minute = int(datetime.now().strftime("%M"))
        current_second = int(datetime.now().strftime("%S"))
        timeNowSec = convertToSecond(current_hour,current_minute,current_second)
        timeEnteredSec = convertToSecond(h,m,s)
        if timeEnteredSec > timeNowSec:             
            message = askMessage()
            print("\nSetting Reminder for :",timedelta(seconds=convertToSecond(real_h,m,s)),t)
            remaining_time_h = h - current_hour
            remaining_time_m = m - current_minute
            remaining_time_s = s - current_second
            time_left = convertToSecond(remaining_time_h,remaining_time_m,remaining_time_s)
            print("Remaining time - ",timedelta(seconds = time_left))
            time.sleep(time_left)
            toaster = ToastNotifier()
            toaster.show_toast("Reminder",message)
            permission = input("Enter c to continue or any other letter to exit : ")
        else:
            print("The time has already passed, please enter valid time")
            askTime()
    else:
        print("The time entered is invalid .Please try again")
        askTime()

print("Thank you!")

    
    

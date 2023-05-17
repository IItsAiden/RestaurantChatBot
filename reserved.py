import os
import re
from datetime import datetime, time

filename = "reservation.txt"
cancelCall = False

# Check if the file exists. If not, create it
if not os.path.exists(filename):
    with open(filename, "w") as file:
        pass

def save(name: str, contactNum: str, date, time):
    # Open the text file in "append" mode and write the user's information to it
    with open(filename, "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Contact Number: {contactNum}\n")
        file.write(f"Date: {date}\n")
        file.write(f"Time: {time}\n\n")

    print("Your table is booked")

def reserved():
    global cancelCall
    date = getDate()
    if cancelCall == True:
        print("Okay, action cancelled.")
        cancelCall = False
        return 0
    time = getTime()
    if cancelCall == True:
        print("Okay, action cancelled.")
        cancelCall = False
        return 0
    name = getName()
    contactNum = getContact()
    save(name, contactNum, date, time)

def getAddress():
    address = input("Where would you like us to deliver to?\n")
    return address

def getName():
    name = input("How can we address you?\n")
    return name

def getContact():
    contactNum = input("Your contact number please.\n")
    return contactNum

def getDate():
    global cancelCall
    while True:
        dateStr = input("Enter the date in yyyy-mm-dd format:\n")
        if dateStr.lower() == 'cancel':
            cancelCall = True
            break
        try:
            date = datetime.strptime(dateStr, "%Y-%m-%d").date()
            return date
        except ValueError:
            print("Invalid date format. Please enter the date in yyyy-mm-dd format.")

def getTime():
    global cancelCall
    while True:
        timeStr = input("Enter the time in hh:mm format between 11am to 9pm:\n")
        if timeStr.lower() == 'cancel':
            cancelCall = True
            break
        if re.match(r"^(?:1[1-9]|2[0-1]):[0-5]\d$", timeStr):
            # Convert the input time to a time object
            time_obj = datetime.strptime(timeStr, "%H:%M").time()
            if time(11, 0) <= time_obj <= time(21, 0):
                timeV = time_obj.strftime("%H:%M")
                return timeV
            else:
                print("Time should be between 11 am to 9 pm.")
        else:
            print("Invalid time format. Please enter the time in hh:mm format.")

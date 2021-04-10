# dateValidator.py
#   This program receives a date in a dd/mm/yyyy format and checks if it's correct
#   This is a test

from calendar import monthrange

def isInt(inputString):
    try:
        int(inputString)
        return True
    except ValueError:
        return False
    
def checkDay(day,month,year):
    if isInt(day):
        day=int(day)
        if isInt(month) and isInt(year):
            month=int(month)
            year=int(year)
            daysInMonth=int(monthrange(year,month)[1])
            if 1<=day<=daysInMonth:
                return True
            else:
                print('The day field must be between 1 and '+ str(daysInMonth)+'.')
                return False
    else:
        print('The day field must be an integer.')
        return False
            
def checkMonth(month):
    if isInt(month):
        month=int(month)
        if month>=1 and month<=12:
            return True
        else:
            print('The month field must be between 1 and 12.')
            return False
    else:
        print('The month field must be an integer.')
        return False
    
def checkYear(year):
    if isInt(year):
        year=int(year)
        if year>=1:
            return True
        else:
            print('The year field must be 1 or greater.')
            return False
    else:
        print('The year field must be an integer.')
        return False
        
def main():
    print('This program validates a date')
    date= input('Enter your date in a dd/mm/yyyy format: ')
    dateArray= date.split('/')
    yearVal=checkYear(dateArray[2])
    monthVal=checkMonth(dateArray[1])
    if yearVal and monthVal:
        if checkDay(dateArray[0],dateArray[1],dateArray[2]):
            print('The date',date,'is correct!')
        
main()
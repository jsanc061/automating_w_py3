# Create a simple timesheet app that records when you type a person’s name 
# and uses the current time to clock them in or out.

import time

# Get the employee ID
def getEmployeeID():
    while True:
        try:
            employeeID = int(input('Enter employee ID to clock in: '))
            return employeeID
        except ValueError:
            print('Enter a valid employee ID: ')

eid = getEmployeeID()  
  
startShift = time.time()    # get the initial time employee clocked in 
clockedIn = True

while clockedIn:
    print('Working...')
    time.sleep(5)
    userPrompt = input('Do you want to keep working? Enter Y or N: ')
    if userPrompt == 'N' or userPrompt == 'n':
        print('\nEmployee ' + str(eid) + ' logged out.')
        clockedIn = False
        hoursWorked = round(time.time() - startShift)
        print('Hours Worked Today: ' + str(hoursWorked))
    else:
        print('Back to work.')


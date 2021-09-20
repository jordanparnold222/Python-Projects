
##PARENT CLASS -- REGULAR CUSTOMERS
class Member:
    name = "Jordan"
    email = "jordan@gmail.com"
    password = "9771900"

    ##LOGIN FUNCTION FOR CUSTOMERS
    def login(self):
        print('\nWelcome, valued customer!')

        enter_name = input('What is your first name?: ')
        enter_email = input('What is your email?: ')
        enter_password = input('What is your password?: ')

        if (enter_email == self.email and enter_password == self.password):
            print('\nHi {}! Welcome back to the member portal.'.format(self.name))
        else:
            print('\nInvalid credentials. Please try again.')
            Member.login(self)

##CHILD CLASS -- STORE MANAGERS
class Manager(Member):
    manager_id = 146343
    store_number = 37

    ##LOGIN FUNCTION FOR MANAGERS
    def login(self):
        print('\nWelcome, store manager!')

        enter_mgmtID = input('What is your manager ID?: ')
        enter_password = input('What is your password?: ')

        if (enter_mgmtID == self.manager_id and enter_password == self.password):
            print('\nHi {}! Welcome back to the manager portal.'.format(self.name))
        else:
            print('\nInvalid credentials. Please try again.')
            Manager.login(self)
##CHILD CLASS -- STORE EMPLOYEES
class Employee(Member):
    employee_id = 503948
    store_number = 37

    ##LOGIN FUNCTION FOR EMPLOYEES
    def login(self):
        print('\nWelcome, store employee!')

        enter_empID = input('What is your employee ID?: ')
        enter_password = input('What is your password?: ')

        if (enter_emptID == self.employee_id and enter_password == self.password):
            print('\nHi {}! Welcome back to the employee portal.'.format(self.name))
        else:
            print('\nInvalid credentials. Please try again.')
            Employee.login(self)

##tHIS FUNCTION WILL BE CALLED ON, SO THAT IT CAN DIRECT THE USER TO THE NECESSARY LOGIN SCREEN
def determineStatus():
    print('Welcome to the grocery store website!')

    status = input('\nAre you a customer, employee, or manager?: \n~~>'.lower())

    if status == "customer":
        member = Member()
        member.login()
        
    elif status == "employee":
        employee = Employee()
        employee.login()

    elif status == "manager":
        manager = Manager()
        manager.login()

    else:
        print("Im sorry, please select from the options provided. \n \n \n")
        determineStatus()

determineStatus()







'''member = Member()

member.login()'''

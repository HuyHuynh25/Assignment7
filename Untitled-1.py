########################################################################
##
## CS 101 Lab
## Program 7
## Name: Huynh Gia Huy-Jim Huynh
## Email: hghydv@umsystem.edu
##
## PROBLEM : Create write a program to read through a file containing 
## information about fuel economy and output the results to a file above 
## a threshold that the user gives
## ALGORITHM :
##      Step 1: Start
##      Step 2: Define function get_minimum_mpg()
##      Step 3: Define function get_input_file()
##      Step 4: Define function get_output_file(minimum_mpg,file_data)
##      Step 5: Declare minimum_mpg equal to function get_minimum_mpg()
##      Step 6: Declare file_data equal to get_input_file()
##      Step 7: Call function get_output_file(minimum_mpg, file_data)
##      Step 10: End
##ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def get_minimum_mpg():
    while True:
        try:
            minimum_mpg = float(input("Enter the minimum mpg ==> "))
            if minimum_mpg < 0:
                print('Fuel economy given must be greater than 0')
            elif minimum_mpg > 100:
                print('Fuel economy must be less than 100')
            else:
                return minimum_mpg
        except:
            print('You must enter a number for the fuel economy')

def get_input_file():
    while True:
        user_file = input('Enter the name of the input vehicle file ==> ')
        try:
            with open(user_file,'r') as read_file:
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]

        except:
            print('Could not open file',user_file)
def get_output_file(minimum_mpg,file_data):
    while True:
        try:
            user_file = input('Enter the name of the file to output to ==> ')
            with open(user_file, 'w') as write_file:
                for data in file_data:
                    try:
                        if minimum_mpg >= float(data[7]):
                            write_file.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(data[0], data[1], data[2], data[7]))
                    except:
                        print('Could not convert value invalid for vehicle', data[0], data[1], data[2])
            break
        except:
            print('There is an IO Error', user_file)
if __name__ == "__main__":
    minimum_mpg = get_minimum_mpg()
    file_data = get_input_file()
    get_output_file(minimum_mpg, file_data)
    
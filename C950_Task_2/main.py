# Student ID: 011788985
from load_trucks import *
from options import *

def main():
    print("Welcome to WGUPS.")
    print("1. Print Total Mileage")
    print("2. Get All Packages at a single time.")
    print("3. Get A Specific package at a single time.")
    print("4. Exit the Program")

    #Continuous loop for menu display, user can break out of loop with option 4
    #O(n^2) complexity since case 2 + 3 contains O(n) functions.
    while True:
        try:
            i = int(input("Please enter one of the following options [1,2,3,4]: "))
            match i:
                case 1:
                    print(f'Total distance traveled is {get_total_distance():.2f} miles.\n')
                case 2:
                    time = input('Enter time in (HH:MM:SS) format: ')
                    get_all_packages(hm, time)
                    break
                case 3:
                    id = int(input('Enter package ID: '))
                    time = input('Enter time in (HH:MM:SS) format: ')
                    get_single_package(hm, id,time)
                    break
                case 4:
                    print('Have a good day.')
                    break

        except:
            print('Invalid input, try again.')
                
if __name__ == "__main__":
    main()
# Student ID: 011788985
from load_trucks import *
from options import *
from visualization import *  # Import the visualization function
from load_trucks import get_total_distance




def main():
    print("Welcome to WGUPS.")
    print("1. Print Total Mileage")
    print("2. Get All Packages at a single time.")
    print("3. Get A Specific package at a single time.")
    print("4. Visualize Package Weights")  # New option
    print("5. Visualize Trucks Completion Times")  # New option
    print("6. Visualize delivery data.")  # New option
    print("7. Exit the Program")


    #Continuous loop for menu display, user can break out of loop with option 4
    #O(n^2) complexity since case 2 + 3 contains O(n) functions.
    while True:
        try:
            i = int(input("Please enter one of the following options [1,2,3,4,5,6,7]: "))
            match i:
                case 1:
                    print(f'Total distance traveled is {get_total_distance():.2f} miles.\n')
                case 2:
                    time = input('Enter time in (HH:MM:SS) format: ')
                    get_all_packages(hm, time)

                case 3:
                    id = int(input('Enter package ID: '))
                    time = input('Enter time in (HH:MM:SS) format: ')
                    get_single_package(hm, id,time)
                    break
                case 4:
                    time_str = input('Enter the time (HH:MM:SS) to retrieve and visualize package data: ')
                    try:
                        package_data = get_package_data_for_visualization(hm, time_str)
                        print(f"Visualizing data for {len(package_data)} packages...")
                        visualize_package_weight(package_data)  # Call visualization
                    except Exception as e:
                        print(f"Failed to visualize package data: {e}")
                case 5:
                    # view package completion amongst trucks (working)
                    visualize_truck_completion_times()

                case 6:
                    # view distances traveled (working)
                    visualize_distance_data()

                case 7:
                    print('Have a good day.')
                    break


        except:
            print('Invalid input, try again.')
                
if __name__ == "__main__":
    main()
import csv
from package import Package
from hashtable import ChainingHashTable
from nearest_neighbor import *
import distances

import datetime

# Example dynamic time setup
current_time = datetime.datetime.now().strftime('%H:%M:%S')

#To set location of packages on truck
#O(n^2)
def set_location(truck):
    for package in truck:
        for address in distances.get_address():
            if package.address == address[2]:
                package.location = address[0]

#Compute the total distance travelled by a truck
#O(n)
def compute_truck_distance(truck_list, idx_list):
    total_distance=0

    for idx in range(len(idx_list)):
        try:
            total_distance = distances.get_distance(int(idx_list[idx]), int(idx_list[idx+1]), total_distance)
            delivery_status = distances.get_time_left(distances.get_current_distance(int(idx_list[idx]), int(idx_list[idx+1])), truck_list[idx].start)
            truck_list[idx].status = str(delivery_status)
            hm.insert(truck_list[idx].ID, truck_list[idx])
        except IndexError:
            pass

    return total_distance

#Read in package data
with open('csv_files/package.csv') as f:
    packageData = csv.reader(f, delimiter=',')
    next(packageData)

    #hm = HashMap()
    hm = ChainingHashTable()
    truck_1 = []
    truck_2 = []
    truck_3= []

    #Iterate through each package
    #O(n)
    for package in packageData:
        id = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        zip = int(package[4])
        deadline = package[5]
        weight = int(package[6])
        notes = package[7]
        start = ''
        location = ''
        status = 'At hub'

        #create instance of a package
        p = Package(id, address, city, state, zip, deadline, weight, notes, start, location, status)

        #Package with wrong address put in truck 3 to allow time for address change
        if 'Wrong' in notes:
            p.start = ['11:00:00']
            p.truck_num = "3"
            truck_3.append(p)

        #First trucks packages
        if deadline != 'EOD':
            if 'Must' in notes or len(notes) == 0:
                p.start = ['8:00:00']
                p.truck_num = "1"
                truck_1.append(p)

        #
        # #Second trucks packages
        # if 'Delayed' in notes or 'Can only' in notes:
        #     p.start = ['9:10:00']
        #     p.truck_num = "2"
        #     truck_2.append(p)
        #
        # if id == 9:  # Package #9 has an incorrect address initially
        #     p.start = ['10:20:00']  # Delay until 10:20 a.m. when address is corrected
        #     p.address = "410 S. State St., Salt Lake City, UT 84111"  # Correct address
        #     p.location = '5'  # Replace with actual location index
        #     truck_3.append(p)  # Assign to truck 3 as before for address correction
        #
        # #Evenly distibute remaining packages across trucks 2 and 3
        # if p not in truck_1 and p not in truck_2 and p not in truck_3:
        #     if len(truck_2) < len(truck_3):
        #         p.start = ['9:10:00']
        #         p.truck_num = "2"
        #         truck_2.append(p)
        #     else:
        #         p.start = ['11:00:00']
        #         p.truck_num = "3"
        #         truck_3.append(p)
        #
        # #store package in a hashmap
        # hm.insert(p.ID, p)
        # Second truck's packages
        if 'Delayed' in notes or 'Can only' in notes:
            p.start = ['9:10:00']
            p.truck_num = "2"
            truck_2.append(p)

        # Package #9 has an incorrect address initially
        if id == 9:
            if current_time < '10:20:00':  # Check if the current time is before 10:20:00
                p.address = "Original Address, Salt Lake City, UT"  # Set to the incorrect address
            else:
                p.address = "410 S. State St., Salt Lake City, UT 84111"  # Corrected address
            p.start = ['10:20:00']  # Delay until 10:20 a.m. when address is corrected
            p.location = '5'  # Replace with actual location index
            truck_3.append(p)  # Assign to truck 3 as before for address correction

        # Evenly distribute remaining packages across trucks 2 and 3
        if p not in truck_1 and p not in truck_2 and p not in truck_3:
            if len(truck_2) < len(truck_3):
                p.start = ['9:10:00']
                p.truck_num = "2"
                truck_2.append(p)
            else:
                p.start = ['11:00:00']
                p.truck_num = "3"
                truck_3.append(p)

        # Store package in a hashmap
        hm.insert(p.ID, p)

        # Optional debug print to verify package state
        # print(p.ID, hm.search(p.ID))


    #Set package starting locations
    set_location(truck_1)
    set_location(truck_2)
    set_location(truck_3)

    #Sort packages on truck based on optimimal ordering
    truck_1_sorted = optimized_route(truck_1, 0,[],[0])
    truck_2_sorted = optimized_route(truck_2, 0,[],[0])
    truck_3_sorted = optimized_route(truck_3, 0,[],[0])

    #Compute the distance travelled by each truck
    truck_1_dist = compute_truck_distance(truck_1_sorted[0], truck_1_sorted[1])
    truck_2_dist = compute_truck_distance(truck_2_sorted[0], truck_2_sorted[1])
    truck_3_dist = compute_truck_distance(truck_3_sorted[0], truck_3_sorted[1])

    #Return total distance travelled by all trucks
    #O(1)
    def get_total_distance():
        return truck_1_dist + truck_2_dist + truck_3_dist








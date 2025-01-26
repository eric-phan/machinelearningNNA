from package import Package
from hashtable import HashTable
from nearest_neighbor import *
import distances
import matplotlib.pyplot as plt

import datetime
import csv


# To set location of packages on truck
# O(n^2)
def set_location(truck):
    for package in truck:
        for address in distances.get_address():
            if package.address == address[2]:
                package.location = address[0]

# Compute the total distance travelled by a truck
# O(n)
def compute_truck_distance(truck_list, idx_list):
    total_distance = 0

    # # Print truck details before computing the distance
    # print(f"Truck details (Total packages: {len(truck_list)}):")
    # print(f"Truck start time: {truck_list[0].start}")
    # print(f"Truck ID: {truck_list[0].truck_num}")
    # print(f"Truck current status: {truck_list[0].status}")

    for idx in range(len(idx_list)):
        try:
            total_distance = distances.get_distance(int(idx_list[idx]), int(idx_list[idx+1]), total_distance)
            delivery_status = distances.get_time_left(distances.get_current_distance(int(idx_list[idx]), int(idx_list[idx+1])), truck_list[idx].start)
            truck_list[idx].status = str(delivery_status)
            hm.insert(truck_list[idx].ID, truck_list[idx])
        except IndexError:
            pass

    return total_distance

# Read in package data
with open('csv_files/package.csv') as f:
    packageData = csv.reader(f, delimiter=',')
    next(packageData)

    # Initialize hash map and trucks
    hm = HashTable()
    truck_1 = []
    truck_2 = []
    truck_3 = []

    # Iterate through packages
    # O(n)
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

        # Create instance of a package
        p = Package(id, address, city, state, zip, deadline, weight, notes, start, location, status)

        #  If package has wrong address put in truck 3 to allow time for address change
        if 'Wrong' in notes:
            p.start = ['11:00:00']
            p.truck_num = "3"
            truck_3.append(p)

        # First truck's packages (start at 8:00 AM)
        if deadline != 'EOD':
            if 'Must' in notes or len(notes) == 0:
                p.start = ['8:00:00']
                p.truck_num = "1"
                truck_1.append(p)

        # Second truck's packages (start at 9:10 AM)
        if 'Delayed' in notes or 'Can only' in notes:
            p.start = ['9:10:00']
            p.truck_num = "2"
            truck_2.append(p)

        # Evenly distribute remaining packages across trucks 1 and 2, ensuring each truck doesn't exceed 16 packages
        if p not in truck_1 and p not in truck_2 and p not in truck_3:
            if len(truck_1) < 16:  # Check if truck_1 has fewer than 16 packages
                p.start = ['8:00:00']  # Start time for truck 1
                p.truck_num = "1"
                truck_1.append(p)
            elif len(truck_2) < 16:  # Check if truck_2 has fewer than 16 packages
                p.start = ['9:10:00']  # Start time for truck 2
                p.truck_num = "2"
                truck_2.append(p)
            elif len(truck_3) < 16:  # If truck_1 and truck_2 are full, use truck_3
                p.start = ['11:00:00']  # Start time for truck 3
                p.truck_num = "3"
                truck_3.append(p)

        # Store package in a hashmap
        hm.insert(p.ID, p)

    # Set package starting locations
    set_location(truck_1)
    set_location(truck_2)
    set_location(truck_3)

    # Sort packages on truck based on optimal ordering
    truck_1_sorted = optimized_route(truck_1, 0, [], [0])
    truck_2_sorted = optimized_route(truck_2, 0, [], [0])
    truck_3_sorted = optimized_route(truck_3, 0, [], [0])

    # Compute the distance travelled by each truck
    truck_1_dist = compute_truck_distance(truck_1_sorted[0], truck_1_sorted[1])
    truck_2_dist = compute_truck_distance(truck_2_sorted[0], truck_2_sorted[1])

    # Calculate completion times for Truck 1 and Truck 2
    truck_speed = 18  # Assigning truck speed of 18 km/h
    truck_1_completion_time = datetime.datetime.strptime('08:00:00', '%H:%M:%S') + datetime.timedelta(hours=(truck_1_dist / truck_speed))
    truck_2_completion_time = datetime.datetime.strptime('09:10:00', '%H:%M:%S') + datetime.timedelta(hours=(truck_2_dist / truck_speed))

    # Start Truck 3 only after Truck 1 and Truck 2 have completed deliveries
    truck_3_start_time = datetime.datetime.strptime('11:00:00', '%H:%M:%S')
    actual_truck_3_start_time = max(truck_3_start_time, truck_1_completion_time, truck_2_completion_time)

    if actual_truck_3_start_time >= truck_3_start_time:
        # Truck 3 can start
        # print(f"Truck 3 starts at {actual_truck_3_start_time.time()}")
        truck_3_dist = compute_truck_distance(truck_3_sorted[0], truck_3_sorted[1])
    else:
        truck_3_dist = 0
        # print("Truck 1 and 2 are not finished. Truck 3 cannot start yet.")



    # Return total distance travelled by all 3 trucks
    def get_total_distance():
        return truck_1_dist + truck_2_dist + truck_3_dist

    # Output the total distance
    # print(f"Total distance traveled by all trucks: {get_total_distance()} km")

    #load truck for visualizations:

    def load_truck_data():
        # Define truck data loading and processing logic here
        truck_data = {

            "truck_1_dist": truck_1_dist,
            "truck_2_dist": truck_2_dist,
            "truck_3_dist": truck_3_dist,
            "total_distance": get_total_distance(),
            "completion_times": {
                "truck_1": truck_1_completion_time.time(),
                "truck_2": truck_2_completion_time.time(),
                "truck_3_start": actual_truck_3_start_time.time(),
            },
        }
        return truck_data


def visualize_truck_completion_times():
    # Calculate the time it took for each truck to complete its delivery (in hours)
    truck_1_duration = (truck_1_completion_time - datetime.datetime.strptime('08:00:00', '%H:%M:%S')).seconds / 3600
    truck_2_duration = (truck_2_completion_time - datetime.datetime.strptime('09:10:00', '%H:%M:%S')).seconds / 3600
    truck_3_duration = (actual_truck_3_start_time - datetime.datetime.strptime('11:00:00', '%H:%M:%S')).seconds / 3600

    completion_times = {
        "Truck 1": truck_1_duration,
        "Truck 2": truck_2_duration,
        "Truck 3": truck_3_duration
    }

    # Plot the time durations
    plt.bar(completion_times.keys(), completion_times.values(), color='lightgreen')
    plt.title("Truck Delivery Completion Times (in Hours)")
    plt.xlabel("Truck")
    plt.ylabel("Time Taken (hours)")
    plt.show()





# from distances import *
#
#
# # Nearest Neighbor Algorithm to determine the optimal ordering of a truck's packages
# # O(n^2) runtime
# def optimized_route(truck, current_location, sorted_truck, sorted_truck_idx):
#     if not len(truck):  # Base case: if there are no more packages to deliver
#         return sorted_truck, sorted_truck_idx
#
#     # Find the nearest package to the current location
#     next_package = None
#     shortest_distance = float('inf')
#
#     for package in truck:
#         d = int(package.location)
#         distance = get_current_distance(current_location, d)
#
#         if distance < shortest_distance:
#             shortest_distance = distance
#             next_package = package
#
#     # Add the nearest package to the sorted truck
#     sorted_truck.append(next_package)
#     sorted_truck_idx.append(int(next_package.location))
#
#     # Remove the selected package from the truck (simulate delivery)
#     truck.remove(next_package)
#
#     # Update the current location to the new package's location and continue the process
#     current_location = int(next_package.location)
#
#     # Recursively call the function to find the next nearest package
#     return optimized_route(truck, current_location, sorted_truck, sorted_truck_idx)


from distances import *

# Nearest Neighbor Algorithm to determine the optimal ordering of a truck's packages
# O(n^2) runtime
def optimized_route(truck, current_location, sorted_truck, sorted_truck_idx):
    if not len(truck):  # Base case: if there are no more packages to deliver
        return sorted_truck, sorted_truck_idx

    # Find the nearest package to the current location
    next_package = None
    shortest_distance = float('inf')

    for package in truck:
        # Check for empty or invalid location before converting to an integer
        if package.location == '' or package.location is None:
            print(f"Warning: Package {package.ID} has an invalid location. Skipping...")
            continue  # Skip packages with invalid locations

        try:
            d = int(package.location)  # Convert location to integer
        except ValueError:
            print(f"Error: Invalid location value for Package {package.ID}, location: {package.location}. Skipping...")
            continue  # Skip package if location is still invalid

        # Calculate the distance to the current package
        distance = get_current_distance(current_location, d)

        if distance < shortest_distance:
            shortest_distance = distance
            next_package = package

    # If a valid next package is found, process it
    if next_package:
        # Add the nearest package to the sorted truck
        sorted_truck.append(next_package)
        sorted_truck_idx.append(int(next_package.location))

        # Remove the selected package from the truck (simulate delivery)
        truck.remove(next_package)

        # Update the current location to the new package's location and continue the process
        current_location = int(next_package.location)

        # Recursively call the function to find the next nearest package
        return optimized_route(truck, current_location, sorted_truck, sorted_truck_idx)

    # If no valid package is found, return the current state
    return sorted_truck, sorted_truck_idx

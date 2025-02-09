import pandas as pd
import matplotlib.pyplot as plt
from load_trucks import load_truck_data
from package import Package
from options import *
from hashtable import HashTable
import datetime

def visualize_distance_data():
    """
    Visualize the distances traveled by each truck using a pie chart.
    """
    # Load truck data
    truck_data = load_truck_data()

    # Truck distances
    distances = [
        truck_data["truck_1_dist"],
        truck_data["truck_2_dist"],
        truck_data["truck_3_dist"],
    ]
    truck_labels = ["Truck 1", "Truck 2", "Truck 3"]

    # Pie chart for distances
    plt.figure(figsize=(8, 8))
    plt.pie(
        distances,
        labels=truck_labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=["blue", "green", "orange"]
    )
    plt.title("Distance Traveled by Each Truck")
    plt.show()


def visualize_distance_data2(hm, time_str):
    """
    Visualize the distances traveled by each truck using a pie chart and print package data.
    """
    # Load truck data
    truck_data = load_truck_data()

    # Truck distances
    distances = [
        truck_data["truck_1_dist"],
        truck_data["truck_2_dist"],
        truck_data["truck_3_dist"],
    ]
    truck_labels = ["Truck 1", "Truck 2", "Truck 3"]

    # Retrieve and print package data for the given time
    print(f"Package data at {time_str}:")
    package_data = get_package_data_for_visualization(hm, time_str)
    for pkg in package_data:
        print(f"ID: {pkg['ID']}, Status: {pkg['Status']}, Address: {pkg['Address']}, "
              f"Start Time: {pkg['Start Time']}, Weight: {pkg['Weight']}")

    # Pie chart for distances
    plt.figure(figsize=(8, 8))
    plt.pie(
        distances,
        labels=truck_labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=["blue", "green", "orange"]
    )
    plt.title("Distance Traveled by Each Truck")
    plt.show()



def visualize_package_weight(package_data):
    """
    Visualize the status and other attributes of packages at a given time.

    Args:
        package_data (list): List of dictionaries containing package details.
    """
    if not package_data:
        print("No package data available to visualize.")
        return

    # Convert package data to a DataFrame for easier manipulation
    df = pd.DataFrame(package_data)

    # Create a bar chart to show the number of packages by status
    # status_counts = df['Status'].value_counts()

    # plt.figure(figsize=(10, 6))
    # status_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    # plt.title("Package Status Distribution")
    # plt.xlabel("Status")
    # plt.ylabel("Number of Packages")
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # For example, package weights
    plt.figure(figsize=(10, 6))
    df['Weight'].plot(kind='hist', bins=10, color='orange', edgecolor='black')
    plt.title("Distribution of Package Weights")
    plt.xlabel("Weight (kg)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()










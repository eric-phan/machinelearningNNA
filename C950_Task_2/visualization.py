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











# 📦 WGUPS Package Delivery Optimization

This project simulates a package delivery system for WGUPS (Western Governors University Parcel Service), using real-world-inspired logistics data and machine learning  algorithms to determine efficient delivery routes and provide visual insights into package metrics.

---

## 🚀 Features

- 🧭 **Route Optimization**: Implements the Nearest Neighbor Algorithm (NNA) to determine efficient delivery routes with O(n²) complexity.
- 📊 **Visualizations**:
  - Distribution of package weights
  - Truck completion times
  - Total distance traveled by each truck
- 🕓 **Time-Based Lookup**:
  - View all package statuses at a specific time
  - View the status of a single package at a specific time

---

## 🗂️ Data Format

- Package and distance data are loaded from **CSV files**.
- Ensure your CSVs are formatted correctly and located in the appropriate directory before running the application.

---

## 💻 How to Use

### 1. 📥 Install Required Libraries

Make sure you have the required Python libraries installed:

- pip install pandas matplotlib

### 2. ▶️ Run the Application

Execute the program via the terminal:

```bash
python main.py

You will be greeted with a command-line interface:

Welcome to WGUPS.  
1. Print Total Mileage  
2. Get All Packages at a single time.  
3. Get A Specific package at a single time.  
4. Visualize Package Weights  
5. Visualize Trucks Completion Times  
6. Visualize distance traveled by truck.  
7. Exit the Program  

Choose a menu option to interact with the system.
```

## 🧠 Why This Matters
This project showcases practical applications of algorithmic thinking, machine learning, and data visualization in logistics — useful for roles involving backend systems, optimization problems, or data-centric engineering.

## 🛠 Tech Stack
- Python

- Pandas for data manipulation

- Matplotlib for data visualization

- CSV for data input
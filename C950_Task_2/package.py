#Package class, defines attributes for package
class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, notes, start, location, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.start = start
        self.location = location
        self.status = status
        self.truck_num = ""
    
    #Returns string with package data
    #O(1)
    def __str__(self):  # this overrides print(Package)
        return (
            f'ID: {self.ID} Delivery Address: {self.address}, Delivery City: {self.city}, Delivery State: {self.state}, Delivery Zip Code: {self.zip}, Delivery Deadline: {self.deadline}, '
            f'Package Weight: {self.weight}, Delivery Start Time: {self.start}, Delivery Status: {self.status}'
            f' Truck Number: {self.truck_num}')



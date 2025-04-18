import datetime

#Return information for all packages for a inputted time
#O(n)
#hm is hashmap that store data of Package objects
def get_all_packages(hm, time):
    try:
        (h, m, s) = time.split(':')
        time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        for i in range(1, 41):
            
            try:
                start = hm.search(i).start
                status = hm.search(i).status
                (h,m,s) = start[0].split(':')
                start = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h,m,s) = status.split(':')
                status = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            except ValueError:
                pass
            if i == 9:  # Specific logic for package ID 10
                # Update the address based on time conditions
                if time < datetime.timedelta(hours=10, minutes=20):  # Compare with desired time
                    hm.search(i).address = "300 State St, Salt Lake City, UT, 84103"  # Update the address
                else:
                    hm.search(i).address = "410 S. State St., Salt Lake City, UT 84111"  # Update the address

            if start >= time:
                hm.search(i).status = 'At Hub'
                hm.search(i).start = 'Departing at ' + str(start)
                print(hm.search(i))

            elif start <= time:
                if status > time:
                    hm.search(i).status = 'In Route'
                    hm.search(i).start = 'Departed at ' + str(start)
                    print(hm.search(i))
                else:
                    hm.search(i).status = 'Delivered at ' + str(status)
                    hm.search(i).start = 'Departed at ' + str(start)
                    print(hm.search(i))

    except:
        print('Invalid input, try again.')

#Return a single package for an inputted ID and time
#O(1)
def get_single_package(hm, id, time):
    try:
        start = hm.search(id).start
        status = hm.search(id).status
        (h,m,s) = start[0].split(':')
        start = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h,m,s) = status.split(':')
        status = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h,m,s) = time.split(':')
        time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        if id == 9:  # Specific logic for package ID 10
            # Update the address based on time conditions
            if time < datetime.timedelta(hours=10, minutes=20):  # Compare with desired time
                hm.search(id).address = "300 State St, Salt Lake City, UT, 84103"  # Update the address
            else:
                hm.search(id).address = "410 S. State St., Salt Lake City, UT 84111"  # Update the address

        if start > time:
            hm.search(id).status = 'At Hub'
            hm.search(id).start = 'Departing at ' + str(start)
            print('Package ID: ' + str(hm.search(id).ID))
            print('Status of Delivery: ' + str(hm.search(id).status))
            print(hm.search(id))

        elif start <= time:
            if time < status:
                hm.search(id).status = 'In Route'
                hm.search(id).start = 'Departed at ' + str(start)
                print(hm.search(id))
            else:
                hm.search(id).status = 'Delivered at ' + str(status)
                hm.search(id).start = 'Departed at ' + str(start)
                print(hm.search(id))

    except:
        print('Invalid input, try again.')



def get_package_data_for_visualization(hm, time_str):
    try:
        # Parse time
        time = datetime.timedelta(
            hours=int(time_str.split(":")[0]),
            minutes=int(time_str.split(":")[1]),
            seconds=int(time_str.split(":")[2])
        )

        package_data = []

        # Retrieve package data
        for i in range(1, 41):  # Assuming package IDs are 1 to 40
            package = hm.search(i)
            if package:
                package_data.append({
                    'ID': package.ID,
                    'Status': package.status,
                    'Address': package.address,
                    'Start Time': package.start,
                    'Weight': package.weight,
                })

        return package_data

    except Exception as e:
        print(f"Error in get_package_data_for_visualization: {e}")
        raise  # Re-raise the exception for further debugging


import datetime

#Return information for all of the packages that match a given time
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
            
            if start >= time:
                hm.search(i).status = 'At Hub'
                hm.search(i).start = 'Departing at ' + str(start)
                print(hm.search(i).__str__()) 

            elif start <= time:
                if status > time:
                    hm.search(i).status = 'In Route'
                    hm.search(i).start = 'Departed at ' + str(start)
                    print(hm.search(i).__str__())  
                else:
                    hm.search(i).status = 'Delivered at ' + str(status)
                    hm.search(i).start = 'Departed at ' + str(start)
                    print(hm.search(i).__str__()) 
                    

    except:
        print('Invalid input, try again.')

#Return a single package that matches a given id and time
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

        if start >= time:
            hm.search(id).status = 'At Hub'
            hm.search(id).start = 'Departing at ' + str(start)
            print('Package ID: ' + str(hm.search(id).ID))
            print('Status of Delivery: ' + str(hm.search(id).status))

        elif start <= time:
            if time < status:
                hm.search(id).status = 'In Route'
                hm.search(id).start = 'Departed at ' + str(start)
                print(hm.search(id).__str__())  
            else:
                hm.search(id).status = 'Delivered at ' + str(status)
                hm.search(id).start = 'Departed at ' + str(start)
                print(hm.search(id).__str__())  

    except:
        print('Invalid input, try again.')
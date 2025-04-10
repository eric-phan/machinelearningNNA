# HashTable class using chaining method.
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns buckets with an empty list.
    #O(n)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
      
    # Insert a new item into the hash table.
    #O(n)
    def insert(self, key, item): #  does both insert and update 
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key provided it is available in bucket
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            kv[1] = item
            return True
        
        # insert the item to the end of the bucket listif not in bucket
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches hash table for item with matching key
    # Returns the item if found, else return None.
    #O(n)
    def search(self, key):
        # given key, get bucket list
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #print(bucket_list)

        # search for key in bucket list
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            return kv[1] # value
        return None

    # Remove an item with given key from hash table.
    #O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if present.
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
              bucket_list.remove([kv[0],kv[1]])
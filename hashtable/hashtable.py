class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
jj
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # Store our array here
        self.capacity = capacity
        self.bucket = [None for i in range(capacity)]
        self.length = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # length divided by capacity
        return self.length / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # ord is a function that accepts a string of length 1 and returns unicode. Ex: B returns 66.
        hash_var = 5381
        for i in key:
            hash_var = (hash_var * 33) + ord(i)
        return hash_var
           


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        
        index = self.hash_index(key)
        new_entry = self.bucket[index]
        
        if new_entry is not None:
            if new_entry.key == key:
                new_entry.value = value
                return
            while new_entry.next:
                new_entry = new_entry.next
                if new_entry.key == key:
                    new_entry.value = value
                    return
            new_entry.next = HashTableEntry(key, value)
            self.length += 1
            if self.get_load_factor > .7:
                self.resize(self.capacity * 2)
        else:
            self.bucket[index] = HashTableEntry(key, value)
            self.length += 1
            if self.get_load_factor() > .7:
                self.resize(self.capacity * 2)
                
        
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
         # Step 1: get the hash
         # Decrement the length after deletion

        index = self.hash_index(key)
        delete_entry = self.bucket[index]
        
        if delete_entry is not None:
            if delete_entry.key == key:
                
                self.bucket[index] = delete_entry.next # this sets the NEW head
                self.length -= 1
                return
            else:
                while delete_entry.next:
                    if delete_entry.next.key == key:
                        delete_entry.next = delete_entry.next.next
                        self.length -= 1
                        return
                    else: 
                        delete_entry = delete_entry.next
        print("Item wasn't found")       
        #Step 3: use that index to access the value stored there
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        search_index = self.hash_index(key)
        current_node = self.bucket[search_index]
        if current_node == None:
            return
        elif current_node.key == key:
            return current_node.value
        while current_node.next:
            current_node = current_node.next
            if current_node.key == key:
                return current_node.value
        return None
    
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_bucket = self.bucket
        self.bucket = [None for i in range(new_capacity)]
        self.capacity = new_capacity
        for head in old_bucket:
            if head is not None:
                self.put(head.key, head.value)
                while head.next:
                    head = head.next
                    self.put(head.key, head.value)


        
        
    

        







if __name__ == "__main__":
    ht = HashTable(8)

    
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")


    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")



    # class LinkedList:
    #     def __init__(self):
    #         self.head = None

    #     def find(self, value):
    #         # start at the head
    #         current = self.head
            

    #         # loop through the list
    #         while current is not None:
    #             if current.value == value:
    #                 return current
    #             current = current.next
    #         # find value
    #         # return the node
    #         return None

    #     def delete(self, value):
    #         current = self.head
    #         if current.value == value:
    #             self.head = current.next
    #             return current
            

    #     def insert_at_head(self, node):
    #         node.next = self.head
    #         self.head = node

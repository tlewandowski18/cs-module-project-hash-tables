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

class LinkedList:
    def __init__(self):
        self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.capacity = capacity
        #without linked list
        # self.hash_table = [None] * capacity
        #with linked list
        self.hash_table = [LinkedList()] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


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
        hash = 5381
        for letter in key:
            hash = ((hash << 5) + hash) + ord(letter)
        return hash & 0XFFFFFFFF


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
        # Your code here
        # put without linked list
        # self.hash_table[self.hash_index(key)] = value
        # put with linked list
        # hash the key and get an index
        node = HashTableEntry(key, value)
        index = self.hash_index(key)

        # find the start of the linked list using the index
        linked_list = self.hash_table[index]
        # Search through linked list
        current_node = linked_list.head
        # IF the key already exists in the linked list
        while current_node is not None:
            if current_node.key == key:
                current_node.value == value:
                return
                # Replace the value
            current_node = current_node.next
        # Else
        linked_list.head.next = linked_list.head
        linked_list.head = node
            # Add new HashTable Entry to the head of linked list
​




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #without linked list
        # return self.hash_table.pop(self.hash_index(key))
        index = self.hash_index(key)
        linked_list = self.hash_table[index]
        prev_node = linked_list.head
        if prev_node.key == key:
            linked_list.head = prev_node.next
            return prev_node.value
        current_node = prev_node.next
        while current_node is not None:
            if current_node.key == key:
                prev_node.next = current_node.next
                return current_node.value
            prev_node = current_node
            current_node = current_node.next
        print(f'Warning: Key named {key} does not exist!')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # without linked list
        # return self.hash_table[self.hash_index(key)]
        # with linked list
        index = self.hash_index(key)
        linked_list = self.hash_table[index]
        current_node = linked_list.head
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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

    print("")

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

# '''
# Linked List hash table key/value pair
# '''
import hashlib

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        if node is None or node.key == key:
            self.storage[hashed_key] = LinkedPair(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            result = node.value
            if prev is None:
                self.storage[hashed_key] = node.next
            else:
                prev.next = prev.next.next
            return result

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        if node is None:
            return None

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        self.capacity *= 2
        temp = self.storage
        self.storage = [None] * self.capacity
        for item in temp:
            if item is not None:
                current = item
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

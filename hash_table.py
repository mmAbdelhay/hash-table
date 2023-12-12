import json

class HashTableLinearProbing:
    def __init__(self, size = 0):
        self.size = size
        self.table = [None] * size
                
    def save_to_json(self, filename="hash_table.json"):
        data = {"size": self.size, "table": self.table}

        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_json(self, filename="hash_table.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            if "size" in data and "table" in data:
                self.size = data["size"]
                self.table = data["table"]
                print("Hash table loaded from JSON.")

        except (FileNotFoundError, json.JSONDecodeError):
            print("JSON file not found or invalid. Using default hash table.")

    def calc_hash(self, key):
        # Simple hash function using the built-in hash function
        return hash(key) % self.size

    def insert(self, key, value):
        if None not in self.table and not self.search(key):
            print("Error: Hash table is full. Cannot insert.")
            return
    
        index = self.calc_hash(key)

        # Linear probing to find the next available slot
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                # Key already exists, update the value
                self.table[index] = (key, value)
                print("Key is already in the table, and is updated successfully");
                return

            index = (index + 1) % self.size

        # Insert the key-value pair
        self.table[index] = (key, value)

    def search(self, key):
        index = self.calc_hash(key)
        original_index = index  # Save the original index for loop termination

        while self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value

            index = (index + 1) % self.size

            # If we have probed the entire table without finding the key, exit the loop
            if index == original_index:
                break

        # Key not found
        return None

    def delete(self, key):
        index = self.calc_hash(key)

        # Linear probing to find the key
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                # Delete the key-value pair
                self.table[index] = None
                return

            index = (index + 1) % self.size

    def display(self):
        print("HashTable:")
        for i in range(self.size):
            if self.table[i] is not None:
                key, value = self.table[i]
                print(f"Index {i}: Key = {key}, Value = {value}")
            else:
                print(f"Index {i}: Empty")

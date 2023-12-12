from hash_table import HashTableLinearProbing

def get_valid_size():
    while True:
        try:
            size = int(input("Enter the size of the hash table: "))
            if size > 0:
                return size
            else:
                print("Size must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_key():
    while True:
        key = input("Enter key: ")
        if isinstance(key, str) and not key.lstrip('-').isnumeric():
            return key
        else:
            print("Invalid input. Key must be a string.")

def display_menu():
    print("\nHash Table Operations:")
    print("1. Create a new hash table")
    print("2. Load from JSON")  
    print("3. Save to JSON")
    print("4. Insert")
    print("5. Search")
    print("6. Delete")
    print("7. Display")
    print("8. Exit")

def main():
    hash_table = None

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            size = get_valid_size()
            hash_table = HashTableLinearProbing(size)
            print(f"New hash table created with size {size}.")
        elif choice == "2":
            if hash_table is not None:
                print("There is already a hash table in memory do you want to delete it")
                isSure = input('Are you sure you want to delete? (y/n): ').lower().strip() == 'y'
                if isSure:
                    hash_table = None
                    filename = input("Enter the JSON file name to load from: ")
                    hash_table = HashTableLinearProbing(0)
                    hash_table.load_from_json(filename)
            else:                
                filename = input("Enter the JSON file name to load from: ")
                hash_table = HashTableLinearProbing(0)
                hash_table.load_from_json(filename)
            
        elif choice == "3":
            if hash_table is not None:
                filename = input("Enter the JSON file name to save to: ")
                hash_table.save_to_json(filename + ".json")
                print(f"Hash table saved to {filename}.")
            else:
                print("Error: No hash table created. Create a new hash table first.")
        elif choice == "4":
            if hash_table is not None:
                key = get_valid_key()
                value = input("Enter value: ")
                hash_table.insert(key, value)
                print("Key-value pair inserted.")
            else:
                print("Error: No hash table created. Create a new hash table first.")
        elif choice == "5":
            if hash_table is not None:
                key = get_valid_key()
                result = hash_table.search(key)
                if result is not None:
                    print(f"Value for key '{key}': {result}")
                else:
                    print(f"Key '{key}' not found.")
            else:
                print("Error: No hash table created. Create a new hash table first.")
        elif choice == "6":
            if hash_table is not None:
                key = get_valid_key()
                hash_table.delete(key)
                print(f"Key '{key}' deleted.")
            else:
                print("Error: No hash table created. Create a new hash table first.")
        elif choice == "7":
            if hash_table is not None:
                hash_table.display()
            else:
                print("Error: No hash table created. Create a new hash table first.")
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

main()

# Hash Table Implementation

---

Student name : muhammad Muhammad abdelhay Muhammad Ibrahim
Student id : 1404-3-087

---

This project provides a simple implementation of a hash table using linear probing in Python. The project is divided into two main files:

## Files

### `hash_table.py`

This file contains the `HashTableLinearProbing` class, which represents the hash table. The class includes methods for initializing the hash table, saving and loading data from a JSON file, calculating hash values, inserting, searching, deleting, and displaying key-value pairs in the hash table.

#### Class Methods:

- `__init__(self, size=0)`: Initializes the hash table with an optional size parameter.
- `save_to_json(self, filename="hash_table.json")`: Saves the hash table data to a JSON file.
- `load_from_json(self, filename="hash_table.json")`: Loads the hash table data from a JSON file.
- `calc_hash(self, key)`: Calculates the hash value for a given key.
- `insert(self, key, value)`: Inserts a key-value pair into the hash table if the key does not exists and update if the ket exists.
- `search(self, key)`: Searches for a key in the hash table and returns its associated value.
- `delete(self, key)`: Deletes a key-value pair from the hash table.
- `display(self)`: Displays the contents of the hash table.

### `main.py`

This file serves as the main entry point for the hash table application. It provides a simple command-line interface for interacting with the hash table.

#### Functions:

- `get_valid_size()`: Prompts the user to enter a valid size for the hash table.
- `get_valid_key()`: Prompts the user to enter a valid string key.
- `display_menu()`: Displays the menu of available hash table operations.
- `main()`: Implements the main loop for user interaction, allowing the creation of a new hash table, loading and saving from/to JSON, and performing insert, search, delete, and display operations.

## Usage

To run the program, execute the `main.py` script. Follow the on-screen prompts to perform various operations on the hash table.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the command: `python main.py`
4. Follow the on-screen prompts to interact with the hash table.

---

# Image Gallery

### create new hash table

![create_new_hash_table](./screenshots\create_new_hash_table.png)

### delete from hash table

![delete_from_hash_table](./screenshots\delete_from_hash_table.png)

### display hash table

![display_hash_tble](./screenshots\display_hash_tble.png)

### insert into hash table (not a valid key)

![insert_into_hash_table_(not_a_valid_key)](<./screenshots\insert_into_hash_table_(not_a_valid_key).png>)

### insert into hash table (valid key)

![insert_into_hash_table_(valid_key)](<./screenshots\insert_into_hash_table_(valid_key).png>)

### invalid choice

![invalid_choice](./screenshots\invalid_choice.png)

### json file not found

![json_file_not_found](./screenshots\json_file_not_found.png)

### load from json file

![load_from_json_file](./screenshots\load_from_json_file.png)

### save to json file

![save_to_json_file](./screenshots\save_to_json_file.png)

### search for a key

![search_for_a_key](./screenshots\search_for_a_key.png)

### update value in hash table

![update_value_in_hash_table](./screenshots\update_value_in_hash_table.png)

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})  # To add a new key and value to a dictionary
capitals.update({"USA": "Las Vegas"})  # To change a value
#  capitals.pop("China") To delete a key and its value from a dictionary
#  capitals.clear() To clear the dictionary

print(capitals["Germany"])  # Obs: This way returns an error if the key does not exist
print(capitals.get("Germany"))  # That's a safer way to get a value
print(capitals.values())
print(capitals.keys())

for key, values in capitals.items():
    print(key, values)

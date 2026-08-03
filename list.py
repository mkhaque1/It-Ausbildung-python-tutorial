# list example and methods in python

city = ['New York', 'Los Angeles']

print(city[0])  # This will print the first index of the list, which is 'New York'
print(city[1])  # This will print the second index of the list, which is 'Los Angeles'

# list methods 
# append() method adds an element to the end of the list

city.append('dhaka')
print(city)  # This will print the updated list with 'dhaka' added to the end

# insert() method adds an element at a specific index in the list

city.insert(0, 'dhaka')  # This will insert 'dhaka' at index 0
print(city)  # This will print the updated list with 'dhaka' inserted at index 0

# remove() method removes the first occurrence of a specified value from the list

city.remove('dhaka')  # This will remove the first occurrence of 'dhaka'
print(city)  # This will print the updated list after removing 'dhaka'

# pop() method removes an element at a specified index and returns it

removed_city = city.pop(0)  # This will remove the element at index 0
print(removed_city)  # This will print the removed city, which is 'New York'
print(city)  # This will print the updated list after popping the element at index 0
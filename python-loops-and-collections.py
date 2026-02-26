######################################################################
# Script Name: Assignment4.py
# Title: Loops and Collections
# Description: This script demonstrates the use of loops and collections 
# in Python. It includes examples of nested loops, while loops, and for 
# loops to manipulate and display data from lists and dictionaries.
# Author: Edgar Gonzalez 
# Date:  September 24, 2022 
######################################################################

dailyTemps = [ [44, 51, 39],
               [34, 49, 40],
               [36, 52, 42],
               [42, 58, 49],
               [44, 63, 45] ] 
for x in dailyTemps : 
    for y in x :
        print( y, end=" ")
    print()
print()
#TODO 1: Print the dailyTemps values in a tabular format, i.e.
#TODO 1: only 3 values on each row. {HINT: Use nested loops}

vehicleInventory = [ {"make": "Chevrolet",
                     "model": "Camaro",
                     "year": 2019,
                     "color": "red"} 
                     ,

                     {"make": "Chevrolet",
                      "model": "Tahoe",
                      "year": 2017,
                      "color": "Silver"}
                      ,

                     {"make": "Dodge",
                      "model": "Durango",
                      "year": 2012,
                      "color": "White"} ]

for x in vehicleInventory :
    for y in x :
        print( x[y], end=" ")
    print()
print()

n = 0
while n <= 42 :
    print(n)
    n += 3
print()

for n in range( 0, 223, 3 ) :
    print (n)


print("--- Daily Temperatures ---")
for row in dailyTemps:
    for temp in row:
        print(temp, end="\t")
    print()  # New line after each row
print()

print("--- Vehicle Inventory ---")
for vehicle in vehicleInventory:
    for key, value in vehicle.items():
        print(f"{key.capitalize()}: {value}")
    print()  # Blank line between vehicles

print("--- While Loop (Increment by 3) ---")
counter = 0
iterations = 0
while iterations < 15:
    print(f"Iteration {iterations + 1}: {counter}")
    counter += 3
    iterations += 1
print()

print("--- For Loop (75 iterations) ---")
current_val = 0
for i in range(75):
    print(f"Iter {i+1}: {current_val}")
    current_val += 3
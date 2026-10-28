# Create a tuple coordinates = (10, 20) and print both elements.
coordinates=(10,20)

print(coordinates)
print(coordinates[1])
print(coordinates[0])
# Try to modify the tuple by setting coordinates[0] = 50

# coordinates[0]=50
# print(coordinates)

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple
tu=list(coordinates)

tu[0]=50

coordinates1=tuple(tu)
print(coordinates1)
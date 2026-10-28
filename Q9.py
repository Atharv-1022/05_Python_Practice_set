'''Create a dictionary of three friends and their phone numbers. Use:

keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them'''

Friends={"Atharv":12131234133,"Om":12313123123,"Raj":1233123431}

print(Friends.keys())

print(Friends.values())

print(Friends.items())

for key,items in Friends.items():
    print(key,items)
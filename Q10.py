# Write a program that takes a list of numbers and removes all duplicates using a set.

num=1
my_list=[]
while num<6:
    a=int(input(f"Enter the numbers {num}:"))
    my_list.append(a)
    num+=1

my_set=set(my_list)

print(my_set)
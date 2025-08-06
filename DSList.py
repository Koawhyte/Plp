# creating an empty list
my_List =[]

#appending elements to the list
my_List.append(10)
my_List.append(20)
my_List.append(30)
my_List.append(40)

#inserting a value at position two
my_List.insert(1,15)

#Extending the list with another list
my_List.extend([50, 60, 70])

#removing the last element from the list
my_List.pop()

#sorting the list
my_List.sort()

#finding the index of 30 from my_list
index = my_List.index(30)

#printing the index
print("index of 30:", index)

#printing my Final list
print(my_List)
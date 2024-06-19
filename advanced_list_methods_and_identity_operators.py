#task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("The following attended and submitted their assignment: ")
if attended[0] == submitted[0] or attended[0] == submitted[1] or attended[0] == submitted[2] or attended[0] == submitted[3]:
    print(submitted[0])

if attended[1] == submitted[0] or attended[1] == submitted[1] or attended[1] == submitted[2] or attended[1] == submitted[3]:
    print(submitted[1])

if attended[2] == submitted[0] or attended[2] == submitted[1] or attended[2] == submitted[2] or attended[2] == submitted[3]:
    print(submitted[2])

if attended[3] == submitted[0] or attended[3] == submitted[1] or attended[3] == submitted[2] or attended[3] == submitted[3]:
    print(submitted[3])


#task 2
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


submitted.sort()
attended.sort()

if submitted == attended: 
    print("The lists are the same")
else:
    print("The lists are not the same")

#task 3 

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

name_one = name_two = name_three = name_four = False

if attended[0] != submitted[0] and attended[0] != submitted[1] and attended[0] != submitted[2] and attended[0] != submitted[3]:
    name_one = True 

if attended[1] != submitted[0] and attended[1] != submitted[1] and attended[1] != submitted[2] and attended[1] != submitted[3]:
    name_two = True 

if attended[2] != submitted[0] and attended[2] != submitted[1] and attended[2] != submitted[2] and attended[2] != submitted[3]:
    name_three = True 

if attended[3] != submitted[0] and attended[3] != submitted[1] and attended[3] != submitted[2] and attended[3] != submitted[3]:
    name_four = True 


if name_one == True :
    attended.remove("Charlie")
if name_two == True :
    attended.remove("Eve")
if name_three == True:
    attended.remove("Alice")
if name_four == True: 
    attended.remove("Frank")
    
print(attended)








    
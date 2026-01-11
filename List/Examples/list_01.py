'''
Perform the following operations on a list of names :
        Create a list of 5 names – 'Anil', 'Amol', 'Aditya', 'Avi', 'Alka'
        Insert a name 'Anuj' before 'Aditya'
        Append a name 'Zulu'
        Delete 'Avi' from the list
        Replace 'Anil' with 'AnilKumar'
        Sort all the names in the list
        Print the reversed sorted list
'''
# 1.
names = ['Anil', 'Amol', 'Aditya', 'Avi', 'Alka']
print(names)
#.2
names.insert(2,'Anuj') 
print(names)
# 3.
names.append('Zulu')
print(names)
# 4.
names.remove('Avi')
print(names)
# 5. 
anil = names.index('Anil') # index()- index() is a list method.#It searches for the value 'Anil' in the list.#It returns the position (index) where 'Anil' is found.
names[anil] = 'AnilKumar'
print(names)
# 6.
names.sort()
print(names)
#7.
names.reverse()
print(names)
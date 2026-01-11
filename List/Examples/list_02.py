'''
Perform the following operations on a list of numbers.
                Create a list of 5 odd numbers
                Create a list of 5 even numbers
                Combine the two lists
                Add prime numbers 11, 17, 29 at the beginning of the combined list
                Report how many elements are present in the list
                Replace last 3 numbers in the list with 100, 200, 300
                Delete all the numbers in the list
                Delete the list
'''
# 1.
odd = [1,3,5,7,9]
print(odd)
# 2.
even= [2,4,6,8,0]
print(even)
# 3.
combine = odd + even
print(combine)
# 4.
combine = [11,17,29] + combine
print(combine)
#5.
present = len(combine)
print(present)
#6.
combine[present - 3 : present] = [100,200,300] # present = 13 -> 13-3= 10 = present[10:13] 
print(combine)
'''
                                                        Index : Value
                                                        10 → 6
                                                        11 → 8
                                                        12 → 10
'''
print(combine)
#7.
combine.clear()
print(combine)
#8.
del present
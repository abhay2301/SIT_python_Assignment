'''Write a program to find the range of a set of numbers.
Range is the difference between the smallest and biggest number in the list?'''


user_array= []
num_element=int(input("Enter the number of element: "))
for i in range(num_element):
    element=input("Enter the element: ")
    user_array.append(element)
smaller=greater=user_array[0]
for j in range(len(user_array)):
    if smaller>user_array[j]:
        smaller=user_array[j]
    if greater<user_array[j]:
        greater=user_array[j]

a=greater
b=smaller
result=a-b
print('Difference in range set is =',result)


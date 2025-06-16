# Write a program that create a dictionary with the frequency of the vowels from an inputted string. For example: input: 'institute".

# Output: ("i":2,'u':1.'e':1}



class frequency:
    def __init__(self):
        self.str=str
        print("Enter the string to count the the vowels: ")
    def countVowel(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for i in self.str:
            if i in vowels:
                count = count + 1
        print("Number of vowels are: ",count)
        count = {}
        for i in vowels:
            if i in self.str:
                count[i] = self.str.count(i)

        print("Frequency of each character in the string is: ",count)
obj1 = frequency()
obj1.str = input()
obj1.countVowel()


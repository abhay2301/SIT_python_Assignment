#   Write a function that takes a string as a parameter and returns a string with every successive repetitive character replaced with a star(*). For example, 'balloon' is returned as "bal*o*n'.



class successiveCharacter:
    def __init__(self, string):
        self.string = string
        
    def repetition(self):
        r=self.string[0]
        for i in range(1,len(self.string)):
            if self.string[i]==self.string[i-1]:
                r+='*'
                
            else:
                r+=self.string[i]
        print("Now the New String is: ",r)
        
character=input("Enter the anme of the String: ")
obj=successiveCharacter(character)
obj.repetition()
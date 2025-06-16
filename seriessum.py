class series:
    def __init__(self,num):
        self.num=num
    def seriessum(self):
        sum=0
        for i in range( self.num + 1):
            sum+=i
        return sum
        
n=int(input("Enter the value of n: "))
s=series(n)
print("Sum of the Series: ",s.seriessum())


            
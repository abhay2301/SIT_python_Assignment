class TowerOfHanoi:
    def __init__(self,num):
        self.num=num

    def TOH(self, n, Beg, Aux, End):
        if n==1:
            print(Beg, "->", End)
            return
        self.TOH(n-1, Beg, End, Aux)
        print(Beg, "->", End)
        self.TOH(n-1,Aux, Beg, End)
    def start(self):
        self.TOH(num, 'A', 'B', 'C')
        

num=int(input("Enter The disc: "))

toh=TowerOfHanoi(num)
toh.start()

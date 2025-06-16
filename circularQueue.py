class circular:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.list=[0 for i in range(size)]
        self.rear=-1
        
    def CQinsertion(self,item):
        if self.front==(self.rear+1)%self.size:
            print("Circular Queue is OverFlow!")
        else:
            self.rear=(self.rear+1)%self.size
            self.list[self.rear]=item
            if self.front==-1:
                self.front=0
        print("List of Circular Queue: ",self.list)
    def traverse(self):
        if self.front == -1:
            print("Circular Queue is Empty")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.list[i], end=" -> ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()  # Move to the next line

        
            
    def CQdeletion(self):
        if self.front==self.rear==-1:
            # print("Circular Queue is UnderFlow! ")
            return
        item=self.list[self.front]
        print(item,'deleted Item')
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        self.traverse()
        
                    
            

s=circular(5)
s.CQinsertion(12)
s.CQinsertion(22)
s.CQinsertion(32)
s.CQinsertion(42)
s.CQinsertion(52)
s.CQinsertion(5)
s.traverse()

# s.CQdeletion()
# s.CQdeletion()
# s.CQdeletion()
# s.CQdeletion()
# s.CQdeletion()

# print("Deletion of Element: ",s.CQdeletion())
# print("Deletion of Element: ",s.CQdeletion())
# print("Deletion of Element: ",s.CQdeletion())
# print("Deletion of Element: ",s.CQdeletion())
# print("Deletion of Element: ",s.CQdeletion())
# print("Circular List: ",s.traverse())


# def traverse(self):
#         if self.rear==self.front==-1:
#             print("Circular Queue is UnderFlow!")
#         # else:
#         #     print("Circular Queue: ",self.list)
#         if self.front!=-1:
#             # print("Remaininng Item: ")
#             while True:
#                 print(self.list[self.front],end=" ")
#                 if self.front==self.rear:
#                     break
#                 self.front=(self.front+1)%self.size
#             print()
#         # else:
#         #     print("Circular Queue is Empty")
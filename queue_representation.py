class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def insertion(self,item):
        nd=Node(item)
        if self.front==None:
            self.front=self.rear=nd
            return None
        else:
            # temp=self.rear
            self.rear.next=nd
            self.rear=nd
            
    def traverse(self):
        if self.front is None:
            print("Queue is Empty")
            return
        temp=self.front
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
        
que=Queue()
que.insertion(10)
que.insertion(20)
que.insertion(30)
que.insertion(40)
que.insertion(50)
que.traverse()
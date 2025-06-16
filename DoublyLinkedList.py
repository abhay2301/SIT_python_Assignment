class node:
    def __init__(self,item):
        self.prev=None
        self.next=None
        self.info=item
class DLinkedList:
    def __init__(self):
        self.start=None
    def insert_at_last(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            
        else:
            temp=self.start
            while temp.next != None:
                temp=temp.next
            temp.next=nd
            nd.prev=temp
            
    def insert_at_beginning(self,item):
        nd=node(item)
        # temp=self.start
        if self.start==None:
            self.start=nd
            nd.next=self.start
        else:    
            nd.next=self.start
            self.start=nd
            # temp=self.start
            # temp.next=nd
            #nd.prev=temp
            # self.start=nd
            
    def traverse(self):
        temp=self.start
        while temp.next != None:
            print(temp.info,end=" -> ")
            temp=temp.next
            if temp==self.start:
                break
        print("Back to start")
        
            
            


ob=DLinkedList()
ob.insert_at_last(10)
ob.insert_at_last(20)
ob.insert_at_last(30)
ob.insert_at_beginning(40)
ob.traverse()

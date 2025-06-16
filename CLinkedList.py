class node:
    def __init__(self,name):
        self.info=name
        self.link=None
class CLinkedlist:
    def __init__(self):
        self.start=None
        
    def insert_at_beginning(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            nd.link=self.start
        else:
            temp=self.start
            while temp.link!=self.start:
                temp=temp.link
            # temp.link=nd
            # nd.link=self.start
            nd.link=self.start
            self.start=nd
            
            
            temp.link=self.start
            
    def insert_at_last(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            nd.link=self.start
        else:
            temp=self.start
            while temp.link !=self.start:
                temp=temp.link
            temp.link=nd
            nd.link=self.start
            
    def traverse(self):
        temp=self.start
        while temp.link !=None:
            print(temp.info,end=" -> ")
            temp=temp.link
            if temp==self.start:
                break
        print(temp.info,"Back to Head")
            
ob=CLinkedlist()
ob.insert_at_beginning(10)
ob.traverse()
ob.insert_at_beginning(20)
ob.insert_at_beginning(30)
ob.insert_at_beginning(40)
ob.insert_at_last(50)
ob.insert_at_last(60)
ob.traverse()

   
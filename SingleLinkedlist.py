class node:
    def __init__(self,name):
        self.info=name
        self.link=None
        
class SLinked_List:
    def __init__(self):
        self.start=None
        
    def insert_at_end(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd                 #insert at end
            return
        else:
            temp=self.start
            while temp.link != None:
                temp=temp.link
                
            temp.link=nd
    def insert_at_Beginning(self,item):
        nd=node(item)
        nd.link=self.start
        self.start=nd
        
    def insert_after_specific_item(self, item,value):
        nd=node(item)
        temp=self.start
        # if self.start==None:
        #     self.start=nd
        #     return
        while temp.info!=value and temp!=None:
            
            
            
            temp=temp.link
        nd.link=temp.link
        temp.link=nd
            
    def Reverse(self):
        # nd=node(item)
        prev=self.start
        current=prev.link
        next=current.link
        while current != None:
            current.link=prev
            prev=current
            current=next
            if current!=None:
                next=current.link
            else:
                next=None
        self.start.link=None
        self.start=prev
        
        
    def traverse(self):
        temp=self.start
        while temp.link!=None:
            print(temp.info,end='->')
            temp=temp.link
        print(temp.info)
    def delete_start_node(self):
        temp=self.start
        self.start=temp.link
        del temp
        
    def delete_last_node(self):
        temp=self.start
        prev=temp
        while temp.link!=None:
            prev=temp
            temp=temp.link
        prev.link=None
        del temp
        
    def delete_specific_item(self,item):
        temp=self.start
        prev=temp.link
        while temp.info!=item:
            prev=temp
            temp=temp.link
        prev.link=temp.link
        del temp
        
ob=SLinked_List()
ob.insert_at_end("ABHAY")
ob.insert_at_end("Sonu")
ob.insert_at_end("ABHA")
ob.insert_at_Beginning("ABHI")
ob.insert_after_specific_item("B","Sonu")
ob.traverse()
# ob.delete_start_node()
# ob.delete_last_node()
# ob.delete_specific_item("B")
ob.Reverse()
ob.traverse()
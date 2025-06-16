class node:
    def __init__(self,name):
        self.info=name
        self.link=None
class ReverseList:
    def __init__(self):
        self.start=None
    def Reverse(self):
        # nd=node(item)
        prev=self.start
        current=prev.next
        next=current.next
        while current != None:
            current.link=prev
            prev=current
            current=next
            next=current.link
        self.start.link=None
        self.start=prev
    def traverse(self):
        temp=self.start
        while temp.link !=None:
            print(temp.info)
            temp=temp.link
        print(temp.info)
ob=ReverseList()
ob.Reverse(ob)
ob.traverse()

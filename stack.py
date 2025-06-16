class stack:
    def __init__(self,size):
        self.size=size
        self.list1=[0 for i in range(size)]
        self.top=-1
        
    def push(self,item):
        # self.item=item
        if self.top==self.size-1 :
            print("Stack overflow")
            exit()
        else:
            self.top+=1
            # self.list.append(item)
            self.list1[self.top]=item
            return
        # print(item)
    def tranverse(self):
         if self.top==-1:
             print("Stack is Empty")
         else:
             print("Stack Element is ",self.list1)
        
    def pop(self):
        # self.item=item
        if self.top==-1:
            print("STACK UNDERFLOW")
            exit()
        else:
            item=self.list1[self.top]
            self.top=self.top - 1
            return item
st=stack(3)
st.push(10)
st.push(29)
st.push(21)
# st.push(244)

print("Traverse Element: ",st.tranverse())
print("Pop the Element: ",st.pop())
print("Pop the Element: ",st.pop())
print("Pop the Element: ",st.pop())
# st.push(244)
# # print(st.pop())





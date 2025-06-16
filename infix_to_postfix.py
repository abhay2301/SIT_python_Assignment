class infix_to_postfix:
    def __init__(self,infix):
        self.infix=infix
        self.postfix=[]
        self.stack=[0]*20
        self.top= -1
        
    def display(self):
        print(self.infix)
        print(self.postfix)
        print(self.stack)
        
    def postfixtoinfix(self):
        
        for i in self.infix:
            print(i)
            print(self.postfix)
            # print(self.stack)
            if i.isalpha():
                self.postfix.append(i)
            if i=='(':
                self.top+=1
                self.stack[self.top]=i
            if i==')':
                while self.stack[self.top]!='(':
                    self.postfix.append(self.stack[self.top])
                    self.top-=1
                self.top-=1
            if i in ['+', '-', '*', '/', '%', '^']:
                if self.stack[self.top]=='(':
                    self.top+=1
                    self.stack[self.top]=i
                else:
                    op1=self.stack[self.top]
                    while op1!='(' and self.precendence(op1)>=self.precendence(i):
                        self.postfix.append(op1)
                        self.top-=1
                        op1=self.stack[self.top]
                    self.top+=1
                    self.stack[self.top]=i    
        while self.top>-1:
            self.postfix.append(self.stack[self.top])
            self.top-=1            
        # print(self.postfix)
        # while (len(self.stack)!=0):
        #     self.postfix.append(self.stack.pop())
        # print(self.postfix)
    
    def precendence(self,op):
        self.op=op
        if op=='^':
            return 3
        elif op=='*' or op=='/' or op=='%':
            return 2
        elif op=='+' or op=='-':
            return 1
        else:
            return 0
        
        
           
        
# list=input("Enter the Input: ").split(sep=',')
list= 'A', '+', '(', 'B', '*', 'C', '-', 'D', '/', 'E', ')', '*', 'G'  
obj=infix_to_postfix(list)
obj.display()
obj.postfixtoinfix()
obj.display()


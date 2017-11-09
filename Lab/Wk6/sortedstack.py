"""Use Stack to sort a list"""
from stackqueue import Stack

class SortedStack(Stack):
    '''It is similar to stack but when pop() (or top()) is called,
    it pops (or returns) the largest and the most resently entered item'''
    
    def __init__(self):
        self.s=Stack() 

    def push(self, val):
        ''' after the item val is pushed in, the stack (self.s)
        is still sorted in a decending order (top to bottom).'''
        SS = Stack()
        Larger = True
        if self.s.isEmpty or (val >= self.s.top()):
          self.s.push(val)  
        else: 
          while Larger:
            SS.push(self.s.pop())
            if (self.s.isEmpty or val >= self.s.top()):
              Larger = False
              self.s.push(val)
          while not SS.isEmpty:
            self.s.push(SS.pop())

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s.top()

    def __str__(self):
        return str(self.s)
        
if __name__=='__main__':
   unsorted_l = [3, 6, 1, 8, 9, 2, 4, 7, 10]
   sstack = SortedStack()
    
   for item in unsorted_l:
       sstack.push(item)

   print(sstack)
       

        

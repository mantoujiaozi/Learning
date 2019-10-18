class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x) 

        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.queue1)-1):
            self.queue2.append(self.queue1[i])
            print(self.queue1[i])
            
        res = self.queue1[-1]
        self.queue1 = self.queue2
        self.queue2 = []
        return res    

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue1) == 0 :
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
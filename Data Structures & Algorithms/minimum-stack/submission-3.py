class MinStack:

    def __init__(self):
      self.stack = []
      self.aux = []

    def push(self, val: int) -> None:
      self.stack.append(val)
      if len(self.aux) == 0:
         self.aux.append(val)
      elif val <= self.aux[-1]:
         self.aux.append(val)

    def pop(self) -> None:
      val = self.stack.pop()
      if len(self.aux) == 0:
         return
      elif val == self.aux[-1]:
         self.aux.pop()
        
    def top(self) -> int:
      return self.stack[-1]

    def getMin(self) -> int:
      if len(self.aux) > 0:
         return self.aux[-1]
      else:
         return None
        

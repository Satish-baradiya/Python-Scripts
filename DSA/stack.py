# Implementing stack 

class Stack:

	def __init__(self):
		self.stack = []


	#using list append method to add element
	
	def add(self,data):

		if data not in self.stack:
			self.stack.append(data)
			return True
		else:
			return False


	#Look at the top of the stack

	def peek(self):
		return self.stack[-1]


	#using list pop to remove element 

	def remove(self):
		if len(self.stack) <=0:
			return ("No element in stack")
		else:
			return self.stack.pop

	#Printing the stack
	def print(self):
		return self.stack

#Inputs

AStack = Stack()

#Adding element to stack.
AStack.add("Monday")
AStack.add("Tuesday")

#Looking at top of the stack

print(AStack.peek())

#Removing element from stack
AStack.remove()

#printing the stack
print(AStack.print())

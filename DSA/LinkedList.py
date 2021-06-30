#Working with linked lists:

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self,head=None):
        self.head = None
        
    #Adding element at the beginning of liked list:-
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
        
    #Inserting element after given node:-
    def InBetween(self,newdata,node):
        NewNode = Node(newdata)
        if node is None:
            return "Node not found"
        NewNode.next = node.next
        node.next = NewNode
    
    #Adding(appending) element at the end of linked list:-
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = newdata
        last = self.head
        while last.next:
            last = last.next  
        last.next = NewNode
        
    #Removing element from a linked list:-
    def RemoveNode(self,removekey):
        HeadVal = self.head
        if HeadVal is not None:
            if HeadVal.data == removekey:
                self.head = HeadVal.next
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.data == removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if HeadVal == None:
            return
        prev.next = HeadVal.next
        HeadVal = None
        
        
    #Printing the linked list:-
    def PrintList(self):
        printval =self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
        
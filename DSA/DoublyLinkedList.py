class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
    def __init__(self,head=None):
        self.head = None
        
    #Adding element at begining of doubly linked list:-
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    
    #Adding element after the given node:-
    def Inbetween(self,newdata,prev_node):
        if prev_node is None:
            return
        NewNode = Node(newdata)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
    
    #Adding element at the end of the doubly linked list:-
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last =self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
    
    #Printing the Doubly linked list:-
    def ListPrint(self,node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next
            
    #Removing the given element from the list:-
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
        

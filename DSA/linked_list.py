class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def insertBeginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  
    
def main():
    head = None 
    head = insertBeginning(head, "Shawn")
    head = insertBeginning(head, "Sean")
    head = insertBeginning(head, "John")
    head = insertBeginning(head, "Zyra")

    print(head.next.next.data)


main()
        

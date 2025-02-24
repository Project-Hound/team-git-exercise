import baselinkedlist

def NodeAtIndex(list1,index):
        current = list1.head
        pointer = 0
        if current:
            while current.next:
                if(pointer == index):
                    return current
                else:
                    pointer = pointer + 1
                    current = current.next
            return -1
        else:
            return 0

#test cases 
node = NodeAtIndex(baselinkedlist.l1, 0)

if node:
    print("Node at index:", node.data)
else:
    print("Index out of range") 
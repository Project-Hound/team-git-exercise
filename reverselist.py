from baselinkedlist import LinkedList, Node, l1

def reversed_list(linked_list):
    previous = None
    current = linked_list.head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    
    linked_list.head = previous
    return linked_list

reversed_list = reversed_list(l1)

# Test case
print('Reversed list:')
reversed_list.printList()
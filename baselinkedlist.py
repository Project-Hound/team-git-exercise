#Added an inline comment


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self,head):
       self.head = head
    def append(self, newNode):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def lengthofList(self):
        current = self.head
        length = 0
        if current:
            while current.next:
                length = length+1
            return length
        else:
            return length

    def printList(self):
        current = self.head
        if current:
            #print("printing data")
            while current.next:
                print(current.data,"->",end=" ")
                current = current.next
        else:
            print("Empty List")
        print(current.data)

        


n1 = Node("Monday")
n2 = Node("Tuesday")
n3 = Node("Wednesday")
n4 = Node("Thursday")
n5 = Node("Friday")
n6 = Node("Saturday")

l1 = LinkedList(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)
l1.append(n5)
l1.append(n6)


l1.printList()
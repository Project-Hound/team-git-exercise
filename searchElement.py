import baselinkedlist

def search_element(list, element):
    current = list.head
    if current:
        while current.next:
            if(current.data == element):
                return True
            else:
                current = current.next
        if current.data == element:
            return True
        else:
            return False
    else:
        return False

#test case to see if monday is in the list
print(search_element(baselinkedlist.l1, "Monday"))

#test case to see if Sunday is in the list
print(search_element(baselinkedlist.l1, "Sunday"))
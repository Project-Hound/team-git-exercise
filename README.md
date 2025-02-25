# Linked List in Python DSA

# Initializing class

I have written a code that intializes a linked list using Nodes as a sub data type , this linked list contains the days of the week and prints then in the format of Monday -> Tuesday -> Wednesday -> Thursday -> Friday -> Saturday


## Search Element

This feature searches the LinkedList to see if there is a specific element. If there is an element, then the result will return true, and vice versa. To use this feature, change the second argument in search_element function to a string. See the below Test Cases for examples.

* Test Case 1:
The feature searches the list for the "Monday" element.
"Monday" element is in the list.
So the result returns True.

* Test Case 2:
The feature searches the list for the "Sunday" element.
"Sunday" element is in the list.
So the result returns False.

## NodeAtIndex

This feature navigates through the linked list and retrieved a node at a specific index. It will return data if the index is valid but out of bound, it will return "Index out of range."

Test Case: node = NodeAtIndex(baselinkedlist.l1, 0)

since 0, is being called, it will navigate and retrieve the corresponding index of node, thus it will return Monday. If it is out of bound, it will return index out of range. 

## Reversedlist

this feature is used to reverse the list. The reversed list feature allows you to view or iterate through a list’s elements in the opposite order. This feature is useful for tasks like backtracking, processing data in reverse, or displaying items from last to first.


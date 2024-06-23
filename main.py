# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# U - Understand
# 1. What should the function return if the linkedlist is empty
# 2. What should we expect the function to output whether it detects a cycle or not?

# P - Plan
# create to pointer variables, slow, and fast, set them equal to head.
# while fast is not None and fast.next is not None:
# slow = slow.next and fast = fast.next.next
# if slow == fast:
# we have found a cycle. return True
# if the while loops ends and we still dont find one, return False

# I - Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

 
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

# Creating the nodes for the first example (circular list)
num1 = ListNode(1)
num2 = ListNode(2)
num3 = ListNode(3)
num1.next = num2
num2.next = num3
num3.next = num1  # Creates the cycle

# Creating the nodes for the second example (non-circular list)
var1 = ListNode(1)
var2 = ListNode(2)
var3 = ListNode(3)
var1.next = var2
var2.next = var3

# Example usage
print(is_circular(num1))  # True
print(is_circular(var1))  # False


# Time Complexity: O(n) - where 𝑛 is the number of nodes in the linked list.
# In the worst case, the slow and fast pointers will traverse the entire list once.
# If there is a cycle, the fast pointer will eventually catch up to the slow pointer.
# If there is no cycle, the fast pointer will reach the end of the list.

# Space Complexity: O(1) -  constant space usage.
# The function only uses two additional pointers, slow and fast, regardless of the size of the input list.
# No additional data structures are used that grow with the size of the input.

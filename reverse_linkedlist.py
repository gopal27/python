#!/usr/bin/python

# Simple recursive program to reverse a linked list

# Node class
class Node:
  
  def __init__(self, data):
      self.data = data
      self.next = None


class LinkedList:

   def __init__(self):
       self.head = None

   def addNode(self, new_data):
       new_node = Node(new_data)
       new_node.next = self.head
       self.head = new_node;


   def display(self):
      itr = self.head
      while (itr != None):
        print itr.data, "-->",
        itr = itr.next
      print "--//"

   def reverse(self):
      if self.head is None:
          return
      self.reverseUtil(self.head, None)

   def reverseUtil(self, curr, prev):
      if curr.next is None:
         self.head = curr

         # Update next to prev node
         curr.next = prev
         return
 
      # Save the curr.next for the recursive call
      next = curr.next
      
      curr.next = prev
      self.reverseUtil(next, curr)
 

#!/usr/bin/python

class LinkedList:

  def __init__(self, data):
    self.data = data
    self.next = None

  def append(self, data):
     curr = self
     while curr.next is not None:
         curr = curr.next

     curr.next = LinkedList(data)


  def display(self):
      # display the first node
      curr = self
      if curr is not None:
        print (str(curr.data) + " --> ")
      
      while curr.next is not None:
        print (str(curr.data) + " --> ")
        curr = curr.next

      # display the end node
      print " None"



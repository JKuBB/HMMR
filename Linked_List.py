
#add comments
#add if statements inindex based methods to increase performance
class Linked_List:

  class __Node:

    def __init__(self, val):
      self.val = val
      self.next = None
      self.prev = None
      self.mmr = None
      
    def __str__(self):
      return str(self.val)

  def __init__(self):
    self.__trailer = Linked_List.__Node(None)
    self.__header = Linked_List.__Node(None)
    #points header to trailer and trailer to header
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0

  def __len__(self):
    return self.__size

  def append_element(self, val):
    #initializes Node
    element = Linked_List.__Node(val)
    #points element at object to left of trailer and object at element
    element.prev = self.__trailer.prev
    self.__trailer.prev.next =  element
    #points trailer at element and element at trailer
    self.__trailer.prev = element
    element.next = self.__trailer
    self.__size+=1

  def insert_element_at(self, val, index):
    #catches special case of an empty list
    if index >= (self.__size) or index < 0:
      raise IndexError("List index out of range.")
    node = Linked_List.__Node(val)
    cur = self.__header.next
    #cur walk
    for item in range(0, index):
      cur = cur.next
    #inserts element and increments size
    cur.prev.next = node
    node.prev = cur.prev
    cur.prev = node
    node.next = cur
    self.__size+=1

  def remove_element_at(self, index):
    #special case of empty list
    if index < 0 or index > (self.__size - 1) or self.__size == 0:
      raise IndexError("List index out of range.")
    elif index <=self.__size//2:
      cur = self.__header.next
    #cur walk
      for item in range(0, index):
        cur = cur.next
    else:
      cur = self.__trailer.prev
      for item in range(index, self.__size - 1):
        cur = cur.prev
    #removes item and decrements size
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    self.__size-=1
    return cur.val

  def get_element_at(self, index):
    #special case of empty list
    if index < 0 or index > (self.__size - 1) or self.__size == 0:
      raise IndexError("List index out of range.")
    #cur walk and return once at the index
    elif index <= self.__size//2:
      cur = self.__header.next
      for item in range(0, index):
        cur = cur.next
    else:
      cur = self.__trailer.prev
      for item in range(index, self.__size - 1):
        cur = cur.prev
    return cur.val


  def rotate_left(self):
    if self.__size == 0:
      return
    #detaches head element and attaches it to end of list
    #to become tail

    self.__header.next.prev = self.__trailer.prev
    self.__trailer.prev.next = self.__header.next
    self.__trailer.prev = self.__header.next
    self.__header.next = self.__header.next.next
    self.__header.next.prev = self.__header
    self.__trailer.prev.next = self.__trailer


  def __str__(self):

    if self.__size == 0:
      return "[ ]"
    #appends each node in the list to the string, then returns the string
    string = "[ "
    cur = self.__header.next
    for item in range(self.__size):
      if item == 0:
        string += str(cur)
      else:
        string += ", "
        string += str(cur)
      cur = cur.next
    string += " ]"
    return string

  def __iter__(self):
    #sets an interation index starting point
    self.__index = self.__header.next
    return self

  def __next__(self):
  #sets rule for how index moves forward
    if self.__index == self.__trailer:
      raise StopIteration
    to_return = str(self.__index)
    self.__index = self.__index.next
    return to_return

if __name__ == '__main__':

  ll = Linked_List()

  ll.rotate_left()
  #test string method pre anything in it
  print(ll)
  #test add and remove methods on an empty list
  try:
    ll.remove_element_at(2)
  except IndexError:
    print("remove_element_at does nothing on an empty list")

  try:
    ll.insert_element_at(4,2)
  except IndexError:
    print("you can't insert an element at an index that doesn't exist")

  try:
    ll.get_element_at(4)
  except IndexError:
    print("you can't get a value from an empty list")
  #print length
  print(str(len(ll)))

  ll.append_element(1)
  ll.append_element(2)
  ll.append_element(3)
  ll.append_element(4)
  print(str(len(ll)))
  print(ll)
  print(ll.get_element_at(2))
  ll.insert_element_at(5,0)
  print(str(len(ll)))
  print(ll)
  ll.remove_element_at(0)
  print(ll)
  print(str(len(ll)))





  try:
    ll.remove_element_at(-1)
  except IndexError:
    print("remove_element_at does nothing on a negative index")

  try:
    ll.insert_element_at(15, -4)
  except IndexError:
    print("you can't insert an element at an index that doesn't exist")

  try:
    ll.get_element_at(-2)
  except IndexError:
    print("you can't get a value from a negative index")

  try:
    ll.remove_element_at(92)
  except IndexError:
    print("remove_element_at does nothing on an index outside list range")

  try:
    ll.insert_element_at(15, 92)
  except IndexError:
    print("you can't insert an element at an index that doesn't exist")

  try:
    ll.get_element_at(92)
  except IndexError:
    print("you can't get a value from an index that is outside of list range")

  ll.remove_element_at(0)
  ll.remove_element_at(len(ll) - 1)

  try:
    ll.insert_element_at(2, (len(ll) - 1))
  except IndexError:
    print("You can't insert element at the tail of the list")

  print(ll)
  print(len(ll))

  ll.insert_element_at(66,0)
  print(len(ll))
  print(ll)

  print(ll.get_element_at(0))
  print(ll.get_element_at(len(ll) - 1))

  for item in ll:
    print(item)
  print(ll)

  ll.rotate_left()

  print(ll)

  ll.insert_element_at(0,0)
  ll.remove_element_at(1)
  ll.append_element(376)
  ll.get_element_at(len(ll)-1)

  print(ll)
  print(len(ll))

  for i in ll:
    print(i)

  array = []
  for i in ll:
    array.append(i)

  print(array)

from queue import Queue
mylist=Queue()
mylist.put("A")
mylist.put("B")
mylist.put("C")
print(mylist)
print(mylist.get())
print(mylist.get())
print(mylist.get())
print(mylist)
print(mylist.get_nowait())


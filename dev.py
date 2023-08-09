# print("Hello World")

ls=["apple", "banana", "cherry", "apple", "cherry"]
print(ls)
print(ls[0])
print(ls[1])
print(ls[2])
print(ls[3])
print(ls[4])
 
 
 # length  of a list
ls = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(ls))

# type of list
ls = ["apple", "banana", "cherry", "apple", "cherry"]
print(type(ls))


# list function to create a list
ls=list(("apple", "banana", "cherry", "apple", "cherry"))
print(ls)
print(ls[0:5])
print(ls[:4])
print(ls[1:])
print(ls[0:6:2])

# change item and insert list item
ls = ["apple", "banana", "cherry", "apple", "cherry"]
ls[0]="orange"
print(ls)
ls[0:4]="a","b","c","d"
print(ls)
ls[-1]="hii"
print(ls)
ls.insert(2,"bye")
print(ls)

# add list item
ls = ["apple", "banana", "cherry", "apple", "cherry"]
ls1=["a","b","c","d"]
ls2=("gauri","dev")
ls.append("hiiii")
print(ls)
ls.insert(2,"bye")
print(ls)
ls.extend(ls1)
print(ls)
ls1.extend(ls2)
print(ls1)


# to delete item from a list
ls = ["apple", "banana", "cherry", "apple", "cherry"]
ls.remove("apple")
print(ls)
 
ls.pop()
print(ls)
ls.pop(2)
print(ls)
del ls[1]
print(ls)

ls.clear()
print(ls)


# list comperhension
ls = ["apple", "banana", "cherry", "apple", "cherry"]
ls1=[]
for x in ls :
  ls1.append(x)
  print(ls1)

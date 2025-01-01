'''
mylist=["banana" ,"cherry ", "apple ",True]
ls2=[x for x in mylist if x =="banana"]
print(ls2)
'''

'''
list=tuple(["hello",28,True])
print(list.count(28))
for i in range(len(list)):
    if list[i]=="hello":
        print(True)
        break
    else: print(False)
  '''  

'''
my_tuple=("a","p","p","l","e")
print(my_tuple.count("e"))
ls=list(my_tuple)
print(ls)
'''

my_tuple=(1,2,3,4,5,6,7,8,9,10)
new=my_tuple[7:0:-1]
print(new)

a="max",28,True
name,age,bool=a
print(name)
print(age)
print(bool)

b=(1,2,3,4,5,6,7,8,9)
i1,i2,*i3=b
print(i1)
x = [1,2,3,]
x.append(4)
print(x)

x = [1,2,3]
x.append("Zeyad")
print(x)

x = [1,2,3,]
x.insert( 1 ,"Zeyad"  )
print(x)

x = [1,2,3]
z = [4,5,6]
x.extend(z)
print(x)

x = [1,2,3]
z = ["Zeyad","Amal","Mahmoud"]
x.extend(z)
print(x)

x = [1,2,4,3,6,7,9,10,8]
x.sort()
print(x)

x = [1,2,4,3,6,7,9,10,8]
x.sort(reverse=True)
print(x)

z = ["Zeyad","Amal","Mahmoud"]
z.remove("Amal")
print(z)

z =["Zeyad","Amal","Mahmoud"]
z.clear()
print(z)
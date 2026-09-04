A={1,2,3}
B={4,5,6}
print(A.union(B))

A={1,2,3}
B={4,5,6}
print(A|B)


A={1,2,3}
A.add(4)
print(A)

A={1,2,3}
A.add(5)
A.add(4)
print(A)

A={1,2,3,"Zeyad"}
A.remove("Zeyad")
print(A)

A={1,2,3,"Zeyad"}
A.discard("Zeyad")
print(A)

A={1,2,3,"Zeyad"}
A.discard(15)
print(A)

A={1,2,3,"Zeyad"}
A.clear()
print(A)
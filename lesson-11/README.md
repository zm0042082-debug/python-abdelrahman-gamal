# اسم الدرس

(string تكملة للنصونص)   

## ماذا تعلمت؟

- لكتابة حروف معينة من الكلمة 

EX:  name=(Z e y a d   m o)         
        0 1 2 3 4 5 6 7
     print(name[اكتب اي رقم])
     = الرقم الحرف الي كتبته

EX1: name="Zeyad mahmoud"
    print (name[0])
    = Z

EX2: name="Zeyad mahmoud"
     print(name[2])
     = y

EX3: x= "Zeyad mahmoud"
     print(x[-1])
     = d 

EX3: x= "Zeyad mahmoud"
     print(x[-5])
     = h

EX2: name="Zeyad mahmoud"
     print(name[0:10])
     = Zeyad mahmo




## أهم الملاحظات

- عند طباعة جزء من الحروف 
name="Zeyad"
      01234 
     print(name[الى:من]) الى+1
يعني لو عايز اطبع كلمة Zeyad كاملة

     print(name[0:4+1])
     print(name[0:5])
     =Zeyad
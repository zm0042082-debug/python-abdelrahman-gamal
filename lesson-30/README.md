# اسم الدرس

**في لغة البايثون (if)  الاداة الشرطية** 

## ماذا تعلمت؟

-  تعني ان لو الشرط دا تحقق نفذهولي لوو متحققش نفذ الشرط التاني ifال 
- (==)بتعني هل الكذا بيساوي كذا

EX1:

egyptian = True
if egyptian == True :
   print("i am egyption")
=i am egyption

egyptian = False
if egyptian == False :
   print("i am not egyption")
i am not egyption

EX2:

egyptian = True
if egyptian :
   print("i am egyption")
=i am egyption

egyptian = False
if not egyptian :
   print("i am not egyption") 
i am not egyption


-  لم يتحقق تطبع الامر التاني (if)تعني ان لو شرط ال (else:)
EX:

* egyptian = True
if   egyptian == True :
     print("i am egyption") 
else: 
     print("i am not egyption")
=i am egyption

* egyptian = True
if   egyptian == False :
     print("i am egyption")
else: 
     print("i am not egyption")
=i am not egyption

*****  *****  *****  *****  *****  ******

*(هنعمل مثال عملي)*

EX1:*(لو الايميل و البسورد صح )*

email = "z@gmail.com"
password = 12345
if    email == "z@gmail.com"  and  password == 12345 :
      print("welcome")

elif  email == "z@gmail.com"  and  password != 12345 :
      print("invalid password")

elif  email != "z@gmail.com"  and  password == 12345 :
      print("invalid email")
else:
      print("invalid email and password")

=welcome

       ******* ******* *******

- EX2: *(لو الباسورد غلط بس)*
email = "z@gmail.com"
password = 123456
if    email == "z@gmail.com"  and  password == 12345 :
      print("welcome")

elif  email == "z@gmail.com"  and  password != 12345 :
      print("invalid password")

elif  email != "z@gmail.com"  and  password == 12345 :
      print("invalid email")
else:
      print("invalid email and password")

= invalid password

       ******  ******  ******

- EX3:  *(لو الاميل غلط بس)*
email = "a@gmail.com"
password = 12345
if    email == "z@gmail.com"  and  password == 12345 :
      print("welcome")

elif  email == "z@gmail.com"  and  password != 12345 :
      print("invalid password")

elif  email != "z@gmail.com"  and  password == 12345 :
      print("invalid email")
else:
      print("invalid email and password")

= invalid email
 
      *******  *******  *******

- EX4: *(لو الباسور و الاميل غلط)* 

email = "a@gmail.com"
password = 123456
if    email == "z@gmail.com"  and  password == 12345 :
      print("welcome")

elif  email == "z@gmail.com"  and  password != 12345 :
      print("invalid password")

elif  email != "z@gmail.com"  and  password == 12345 :
      print("invalid email")
else:
      print("invalid email and password")


*****************************************

## أهم الملاحظات

- (else)تعني اي حاجه بخلاف الاوامر الي فوق يبقى اطبعلي امر دا 

- هناك فرق بين ال(or) & (and)

and  لازم الشرطين يتحققوا 

اااماااا

or يكفي ان شرط واحط بس يتحقق  

## شرح الكود بكلماتك

- لا يوجد

## أمثلة إضافية جربتها

- لا يوجد

## الأخطاء التي واجهتني

- لا يوجد

## كيف قمت بحلها؟

- لا يوجد

## أسئلة أريد البحث عنها لاحقًا

- ازاي استخدم ال (or)
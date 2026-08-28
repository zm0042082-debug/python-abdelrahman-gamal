# اسم الدرس

list 2  بيانات القائمة 

## ماذا تعلمت؟

-  *.append* لو عايز اضيف حاجه داخل اخر اللست    
EX1: x = [1,2,3,]
    x.append(4)
    print(x)
   =[ 1, 2, 3, 4]

EX2: x = [1,2,3]
    x.append("Zeyad")
    print(x)
   =[ 1, 2, 3,'Zeyad']

-  *.insert* لو عايز اضيف حاجه داخل اللست مع تحديد المكان

EX1: x = [1,2,3,]
    x.insert(  1     ,  "Zeyad"  )
            الهيتضاف  ,   المكان  
    print(x)
   =[ 1, Zeyad, 2, 3]

-  *.extend()*لو عايز ادمج لستتين ف لسته واحده 

EX1: x = [1,2,3]
     z = [4,5,6]
    x.extend(z)
    print(x)
   =[ 1, 2, 3, 4, 5, 6]

EX2: x = [1,2,3]
     z = ["Zeyad","Amal","Mahmoud"]
    x.extend(z)
    print(x)
   =[ 1, 2, 3, 'Zeyad', 'amal', 'Mahmoud']


-   *.sort(بدون قيمه)* لو عايزارتب اللسته ترتيب تصاعدي 

EX1: x = [1,2,4,3,6,7,9,10,8]
    x.sort()
    print(x)
   =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

EX2:   z = ["Zeyad","Amal","Mahmoud"]
    z.sort()
    print(z)
   =[ 'amal', 'Mahmoud', 'Zeyad']


-    *.sort(reverse=Ture)* لو عايزارتب اللسته ترتيب تنازلي 

EX1: x = [1,2,4,3,6,7,9,10,8]
    x.sort(reverse=True)
    print(x)
   =[ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

EX2:   z = ["Zeyad","Amal","Mahmoud"]
    z.sort(reverse=Ture)
    print(z)
   =[ 'Zeyad', 'Mahmoud', 'amal']


-  *.remove()*لو عايز احذف كلمة داخل اللسته 

EX1:   z = ["Zeyad","Amal","Mahmoud"]
    z.remove("Amal")
    print(z)
   =[ 'Zeyad', 'Mahmoud']
 

-  *.clear()*لو عايز احذف كل اللسته 

EX1:   z = ["Zeyad","Amal","Mahmoud"]
    z.clear()
    print(z)
   =[ ]

## أهم الملاحظات

-   *.sort(بدون قيمه)*

EX1: x = [1,2,4,3,6,7,9,10,8]
    x.sort()
    print(x)
   =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


## شرح الكود بكلماتك

- لا يوجد

## أمثلة إضافية جربتها

- لا يوجد

## الأخطاء التي واجهتني

- لا يوجد

## كيف قمت بحلها؟

- لا يوجد
# اسم الدرس

dictionary المعاجم

## ماذا تعلمت؟

- ف اي معجم بنلاقي الكلمة قدامها المعنى بتاعها يعني مثلا انا عندي موظف 
هدي للمعجم كل معلوماته بحيث وقت ما احتاج معلومه يطلعهالي 

EX1:  info={ 
     "name"     : "Zeyad" ,
      "age"     :  23  ,
    "country"   : "egypt"
     }
  print(info)
  ={'name' : 'Zeyad' , 'age' : 23 , 'country' : 'egypt' }

EX2:  info={ 
    "name"     : "Zeyad" ,
     "age"     :  23  ,
   "country"   : "egypt"
   }
  print(info["name"])
  =Zeyad


- .get() ممكن استخدم عنصر لطباعة حاجه معينه 

EX3:  info={ 
    "name"     : "Zeyad" ,
     "age"     :  23  ,
   "country"   : "egypt"
   }
  print(info.get("country"))
 = egypt


- طيب انا لو عايز اطبع حاجه والحاجه دي مش قاعده ف المعجم

EX4:  info={ 
    "name"     : "Zeyad" ,
     "age"     :  23  ,
   "country"   : "egypt"
   }
  print(info.get("id"))
 = None

-  .get("--" , "مش قاعده")     طيب انا لو عايز اطبع حاجه والحاجه دي مش قاعده ف المعجم وعايزه يقولي مش قاعده

EX5:  info={ 
    "name"     : "Zeyad" ,
     "age"     :  23  ,
   "country"   : "egypt"
   }
  print(info.get("id","not found"))
 = not found

## أهم الملاحظات

-

## شرح الكود بكلماتك 

- لا يوجد

## أمثلة إضافية جربتها

- لا يوجد

## الأخطاء التي واجهتني

- لا يوجد

## كيف قمت بحلها؟

- لا يوجد

## أسئلة أريد البحث عنها لاحقًا

- لا يوجد
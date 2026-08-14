# اسم الدرس

*(string النصوص)*

## ماذا تعلمت؟

- يمكن كتابة str بعدة طرق 

1-بين singl Quotes ('')
EX:  x='Zeyad'
     print(x)
     =Zeyad

2-بين Double Quotes ("") 
EX:  x="Zeyad"
     print(x)
     =Zeyad

3-بين Triple Quotes ('''  ''') ("""  """)
تستخدم لكتابة نص متعدد الاسطر
EX:  x= """ 'Zeyad'
           "mahmoud" 
           "sayed"
        """
     print(x)
     = 'Zeyad'
       "mahmoud" 
       "sayed"

 - (*استخدامات ال Backslash ف  str ال*)  

1: لو بكتب سطر طويل  وعايز اقسمه بس يبقى تبع بعض   
 بعمل Backslash(\) كدا انا بقله السطرين تبع بعض
EX:  x= "Zeyad\  
          mahmoud" 
     print(x)
     = Zeyadmahmoud 
 
2: لو عايز افصلهم ف الطباعه عن بعض يبقو مثلا تحت بعض 
 بعمل  (\n) كدا بقله اعملي السطريين تحت بعض
EX:  x= "Zeyad\n mahmoud" 
     print(x)
     = Zeyad
       mahmoud 

3: لو عايز اطبع علامتين تنصيص داخل جمله 
  بعمل (\" \")
EX:  x= "Zeyad \"mahmoud\"" 
     print(x)
     = Zeyad"mahmoud" 

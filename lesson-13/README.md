# اسم الدرس

string  تكملة للنصوص جزء 4 

## ماذا تعلمت؟

- لتحويل اي جملة طباعة من بيانات string الى list
  
EX: progaram_lan="['html', 'css', 'javascript', 'php', 'python']"   *جملة string*
     print(progaram_lan)   *جملة string*
     =html css javascript php python    *جملة string*
 
 لتحوبلها الى بيانات list

1- نضع .split() بسبب ان ف سبيس بين الكلام ف اعتبر كل اسبيس وحده جديده او عنصر لوحده 
EX1: progaram_lan="html css javascript php python"
     print(progaram_lan.split())   
     =['html', 'css', 'javascript', 'php', 'python']   

2- نضع .split() وبسبب اننا محطناش قيمه هيعتبرها وحده واحده ، وكمان محطتش سبيس
EX2: progaram_lan2="html_css_javascript-php-python"
     print(progaram_lan2.split())   
     =['html_css_javascript-php-python']   داخل وحده واحده

3- نضع .split("_")  هو اعتبر عن كل اندر سكور وحدة جديده او عنصر لوحده
EX:  progaram_lan2="html_css_javascript_php_python"
     print(progaram_lan2.split("_"))   
     =['html', 'css', 'javascript', 'php', 'python']  


4- نضع .split("h") كدا كل حرف h هيعمله وحده فاضيه     
EX:  progaram_lan2="html_css_javascript_php_python"
     print(progaram_lan2.split("h"))   
     =['', 'tml_css_javascript-p', 'p-pyt', 'on']  

5- نضع .split("_",3) كدا هو هيعمل اول تلت اندر سكور كل واحده فيهم عنصر لوحده والباقي مدمج 
EX:   progaram_lan2="html_css_javascript_php_python"
     print(progaram_lan2.split("_",3))   
     =['html', 'css', 'javascript', 'php_python']  

6- نضع .rsplit("_",3)
EX:  progaram_lan2="html_css_javascript_php_python"
     print(progaram_lan2.rsplit("_",3))   
     =['html_css', 'javascript', 'php', 'python']  

## أهم الملاحظات

- .split() بيبدا يغير من الشمال لليمين
EX: progaram_lan2="html_css_javascript_php_python"
     print(progaram_lan2.split("_",3))   
     =['html', 'css', 'javascript', 'php_python']  

- .rsplit() بيبدا يغير من اليمين للشمال 
EX:  progaram_lan2="html_css_javascript_php_python"
     print(progaram_lan2.rsplit("_",3))   
     =['html_css', 'javascript', 'php', 'python']  

## شرح الكود بكلماتك

- لا يوجد

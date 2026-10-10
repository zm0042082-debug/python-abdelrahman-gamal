## عمل لعبة عن الاسئلة 

EX:

secret_answer = "cairo"     دا فريابول بتاع الاجابه الصحيحه الي عايزها 
answer = ""       دا الفريابول بتاع مكان الاجابه 
while  secret_answer != answer :     هنا بقوله لو الاجابه مختلفه عيد السؤال تاني 
       answer = input ("what is capital of egypt ?")
print("you win")



EX 2:
هنا لو عايز احددله عدد محاولات  

secret_answer = "cairo"     
answer = ""
count = 0
limit = 3
lose = False
while      secret_answer != answer  and  not lose :
     if    count > limit : 
           answer = input ("what is capital of egypt ?")
           count += 1
     else:
           lose = True  

if    lose :
      print("you lose")

else :
      print("you win")



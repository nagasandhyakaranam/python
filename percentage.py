"""below 25-D
25 to 45-C
45 to 50-B
50 to 60-B+
60 to 80-A
above 80-A+"""
pr=int(input("enter your percentage.."))
if pr>20 and pr<=25:
    print("The grade is D..")
elif pr>25 and pr<=45:
    print("The grade is C..")
elif pr>45 and pr<=50:
    print("The grade is B..")
elif pr>50 and pr<=60:
    print("The grade is B+..")
elif pr>60 and pr<=80:
    print("The grade is A..")
elif pr>80:
    print("The grade is A+..")
else:
    print("you are failed")
"""
if condition:
    outer if statements
    if condition:
        inner if statements
    else:
        inner else statements
else:
    outer else statements"""


     #express delivery:

weight=int(input("enter the weight"))
if weight==4:
    print("the delivery can be expected within 24 hours")
    if weight<=10:
         print("need to pay an extra amount for extra weight")
    else:
        print("no need to pay an extra charge.have a great delivery!!")
else:
    print("need to wait 3-5 bussiness days to expect the delivery")
    
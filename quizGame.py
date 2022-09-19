print("welcome to the quiz")

x = input("do you want to play? ")
if x != "yes":
    quit()

print("lets play!")
score = 0
ans1 = input("what is 2+2? ")
if ans1 == "4":
    print("correct")
    score += 1
else:
    print("incorrect")

ans1 = input("what does cpu stand for ")
if ans1.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

ans1 = input("what is 2+1? ")
if ans1 == "3":
    print("correct")
    score += 1
else:
    print("incorrect")

ans1 = input("what is 2+4? ")
if ans1 == "6":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " +str(score) +" correct.")
print("your percentage is "+ str(score/4*100) + "%")
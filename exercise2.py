grade= float(input('Give a grade between 0 and 100.'))

while(grade<0 or grade>100):
    print("The grade is not between 0 and 100. Please give another grade.")
    grade=float(input())

if(grade>=90):
    print("A")
elif(grade>=80):
    print("B")
elif(grade>=70):
    print("C")
elif(grade>=60):
    print("D")
else:
    print("F")
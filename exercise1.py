print ("give a year")
year=int(input())
if(year%400==0):
    print("it s a leap year")
elif(year%4==0):
    if(year%100!=0):
        print("it s a leap year")
    else:
        print("it s not a leap year")
else:
    print("it s not a leap year")
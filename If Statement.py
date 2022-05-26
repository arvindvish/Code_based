#1

num = input ("Enter a Number")
num= int(num)
if num%2==0:
    print("Number is Even: ")
else:
    print("Number is odd")
#2

indian=["samosa", "daal","naan"]
chinese=["egg role","fried rice", "pot sticker"]
italian=["pasta","pizza","risotto"]
dish=input("Enter a dish name: ")

if dish in indian:
    print(indian)
elif dish in chinese:
    print(chinese)
elif dish in italian:
    print(italian)
else:
    print("base little knowledge i have i dont know which cuisine is",dish)

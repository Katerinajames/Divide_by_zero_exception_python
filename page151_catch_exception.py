try:
 n=int(input("Enter a number\n"))
 n1=int(input("Enter a second number\n"))

 print(n/n1)
except ZeroDivisionError:
	print("The second number can't be zero")

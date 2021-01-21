# method to print the factors
printDivisors=int(input("Enter the number "))
def printDivisors(n) : 
	i = 1
	while i <= n : 
		if (n % i==0) : 
			print(" ",i) 
		i = i + 1
		

printDivisors(100) 


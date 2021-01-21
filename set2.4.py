# Function to print all the perfect squares from the given range 
def perfectSquares(l, r): 
	for i in range(l, r + 1): 
# If current element is a perfect square 
		if (i**(.5) == int(i**(.5))): 
			print(i, end=" ") 

# Driver code 
l = 2
r = 150

perfectSquares(l, r) 


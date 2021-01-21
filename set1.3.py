def Check_Vowels(string, vowels): 
	final = [each for each in string if each in vowels] 
	print(len(final)) 
	print(final) 
	
# Driver Code 
string = "she is beautiful"
vowels = "AaEeIiOoUu"
Check_Vowels(string, vowels); 

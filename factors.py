from os import system,name

def clear():
	if name == 'nt':
		system('cls')
	elif name == 'posix':
		system('clear')

def factors(n):
	results = []
                for k in range(1,n+1):
		if n % k == 0:
			results.append(k)
	return results

clear()
number = 0
while number <= 0:
	try:	
		response = input("Enter a positive integer number: ")
		number = int(response)
		if number <= 0:
			raise ValueError
	except ValueError:
		clear()
		print(f"\'{response}\' is not a valid input.")
		print("Enter a nonzero and non-negative number.")
	except EOFError:
		clear()
		print("Invalid Input")
		raise

clear()
print(f"Factors of {number} are", factors(number))

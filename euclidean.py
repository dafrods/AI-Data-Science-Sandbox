def euclidean(a,b):
	if a < b:
		z = a
		a = b
		b = z
		
	while b != 0:
		print(a, " mod ",b)
		z = a % b
		a = b
		b = z
	
	print("GCF: ", a )

a = int(input("Value for a: "))
b = int(input("Value for b: "))
euclidean(a,b)

		
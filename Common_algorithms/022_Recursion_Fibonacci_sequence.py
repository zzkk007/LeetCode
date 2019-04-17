def Fibonacci_sequence(num):

	if num <= 1:
		return num
	else:
		return (Fibonacci_sequence(num-1) +  Fibonacci_sequence(num-2))

if __name__ == "__main__":
	nterms = int(input("您要输出几项? "))
	list1 = []
	for i in range(nterms):
		list1.append(Fibonacci_sequence(i))
	print(list1)
N = int(input())
grades = input()

gpa = 0
for grade in grades:
	if grade == 'A':
		num = 4
	elif grade == 'B':
		num = 3
	elif grade == 'C':
		num = 2
	elif grade == 'D':
		num = 1
	elif grade == 'F':
		num = 0
	
	gpa += num

print(gpa/N)
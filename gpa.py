per = int(input("User enters a grade: "))
if per < 0 or per > 100 :
	print('Incorrect grade!')
if per >= 0 and per < 60:
    print("F", str(0.0))
if per >= 60 and per < 70:
	print('D', str(1.0))
if per >= 70 and per <= 77:
	print('C', str(2.0))
if per >= 77 and per <= 79:
	print('C+', str(2.33))
if per >= 80 and per <= 82:
	print('B-', str(2.67))
if per >= 83 and per <= 86:
	print('B', str(3.0))
if per >= 87 and per <= 89:
	print('B+', str(3.33))
if per >= 90 and per <= 92:
	print('A-', str(3.67))
if per >= 93 and per <= 100:
	print('A', str(4.0))
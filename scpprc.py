p1 = input()
p2 = input()
if p1 == "sc" and  p2 == "pp":
    print('Winner is Player1')
elif p1 == 'pp'  and  p2 == 'sc':
	print("Winner is Player2")
elif p1 == 'pp'  and  p2 == 'rc':
	print("Winner is Player1")
elif p1 == 'rc'  and  p2 == 'pp':
	print('Winner is Player2')
elif p1 == 'rc'  and  p2 == 'sc':
	print('Winner is Player1')
elif p1 == 'sc' and  p2 == 'rc':
	print('Winner is Player2')
else:
	print('Draw')

prime_list = []

with open('primenumbers.txt') as primesfile:
	line = primesfile.readline()
	while line:
		prime_list.append(int(line))
		line = primesfile.readline()

happie_list = []

with open('happynumbers.txt') as happiesfile:
	line = happiesfile.readline()
	while line:
		happie_list.append(int(line))
		line = happiesfile.readline()

overlap_list = []

for i in primeslist:
	if i in happieslist:
		overlap_list.append(i)
		
print(overlap_list)
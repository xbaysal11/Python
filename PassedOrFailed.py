# LS2-Q1:Passed or failed
# Write a program that outputs the message “passed” or “failed” based on user’s input. If the user enters the number in range [50,100] program must print out message “passed”, if number is in the range [0, 50) program prints out the message “failed”, otherwise program must print out “Incorrect grade!”. 

users_grade = input("Enters his/her grade: ")
if users_grade >= 50:
  if users_grade <= 100:
      print("Passed")
else:
  if users_grade >= 0:
  	print("Failed")
if users_grade > 100:
    print("Incorrect grade!")
if users_grade  < 0:
    print("Incorrect grade!")

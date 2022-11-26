user = "Vincent"
age = 30

if age >= 20 and age <= 40:
  print('Age is between 20 and 40')
elif age > 20:
  print('Age is less than 20')
elif age > 40:
  print('Age is greater than 40')

if user == 'Vincent' and age > 25 or age < 30:
  print('Vincent is either older than 29 or younger than 20')

if user == 'Vincent' and (age > 25 or age < 30):
  print('Vincent is either older than 29 or younger than 20 - 2nd version of conditional statement')

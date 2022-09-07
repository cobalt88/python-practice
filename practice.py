# print("Hello world!")
# print(5+5)
# print(5-5)
# print(5*5)
# print(5/5)
# print(5%5)
# print(5**5)
# print(5//5)
# print(5==5)
# print(5!=5)
from datetime import date

fruits = ["apple", "banana", "cherry"]
nums = [1, 2, 3, 4, 5]

for x in range(25): 
  if x%2 == 0:
    print(x, "even")
  else:
    print(x, "odd")

print("done")

print(date.today())

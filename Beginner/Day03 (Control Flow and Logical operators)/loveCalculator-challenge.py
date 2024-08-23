print("The Love Calcultor is calculating your score...")
name1 = str(input("Name 1: ")).lower()
name2 = str(input("Name 2: ")).lower()

combineName = name1 + name2
combineName = combineName.lower()

t = combineName.count("t")
r = combineName.count("r")
u = combineName.count("u")
e = combineName.count("e")
sum1 = t + r + u + e

l = combineName.count("u")
o = combineName.count("u")
v = combineName.count("e")
e = combineName.count("e")

sum2 = l + o + v + e

str(sum1)
str(sum2)

print(sum1 + sum2)
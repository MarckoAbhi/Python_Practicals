# symmetric = difference between s1, s2
s1 = {"Abhi", "Radha", "Chandani", "143"}
s2 = {"Radha", "Love", "143"}
s = s1.symmetric_difference(s2)
print(s)

#other way to find symmetric

s = s1 ^ s2
print(s)
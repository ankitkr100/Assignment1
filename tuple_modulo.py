from operator import mod
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)
print("The original tuple : " + str(test_tup1))
print("The original tuple : " + str(test_tup2))
res = tuple(map(mod, test_tup1, test_tup2))
print("The modulus tuple : " + str(res))
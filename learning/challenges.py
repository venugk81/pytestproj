d = {"a": 1, "b": 2}
for k in d:
    print(k, d[k])
    print(k)

# in caes of defaul parameters:

sq = lambda x: x**x
print(sq(2))

num =[1,2,4]
x = list(map(lambda x: x*2 if x>1 else x, num))
print(x)
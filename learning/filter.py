num = [1,3,6,3,9,7,5,8,64]
vals = filter(lambda x: x % 2 == 0, num)
print(list(vals))


num = [1,3,6,3,9,7,5,8,64]
def evn(num):
    if num % 2 == 0:
        return num

print(list(filter(evn, num)))


names = ["Arushi","Aaina","Yash","Ragini"]
val = filter(lambda nm: nm.startswith("A"), names)
print(list(val))

nums = list(range(1,50))
fil = filter(lambda x: x%3==0 and x%5==0, nums)
print(list(fil))


st = "innomatics research and labs"
print(st[:4] + st[-4:])


print()

st = "Andaman"
vowels = str(["a", "e", "i", "o", "u"]).lower()
non_vowels = filter(lambda x: x.lower() not in vowels, st)
print(list(non_vowels))


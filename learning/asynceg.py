import asyncio

async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 end")

async def task2():
    print("Task 2 start")
    await asyncio.sleep(1)
    print("Task 2 end")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Task 1 start
# Task 2 start
# Task 2 end
# Task 1 end

a = {"a": 1, "b": 2, "z": 3}
print(a.get("p", 5))

d = {"a": 1, "b": 2}
d["d"]=40
d["a"]=100
print(d)
sum =0
for i in d.values():
    sum += i

x= 10
def task3():
    global x
    x= x+5
    return x
print(task3())
def f():
    global s
    s+=1
    print(s)

s = 0
while True:
    x = input()
    if x == 0:
        break
    f()
    


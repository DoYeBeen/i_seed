def myFunc(p1=1, p2=2, p3=3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==>", myFunc())
print("매개변수가 1개로 호출 ==>", myFunc(1))
print("매개변수가 2개로 호출 ==>", myFunc(1, 2))
print("매개변수가 3개로 호출 ==>", myFunc(1, 2, 3))
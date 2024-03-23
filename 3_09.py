
num = 0

for i in range(3333, 10000):
    # 1234의 배수가 아니라면 continue를 사용하여 건너뛴다
    if i % 1234 != 0:
        continue
    
    # 현재 합계에 다음 배수를 더했을 때 100000을 넘으면 break를 사용하여 반복문을 종료한다
    if num + i > 100000:
        break
    
    # 합계에 현재 숫자를 더한다
    num += i

print(num)

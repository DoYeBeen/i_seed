n = 1234
hap = 0

while n <= 4567:  
    if n % 444 == 0:
        hap += n
    n += 1

print(hap)
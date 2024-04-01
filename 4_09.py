inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr += inStr[strLen - (i+1)]

print('내용을 거꾸로 출력 --> %s' % outStr)
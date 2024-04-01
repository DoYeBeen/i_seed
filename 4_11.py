outStr = ''

inStr = input('문자열 : ')

for char in inStr:
    if '가' <= char <= '힣':
        outStr += char
    elif char.isalpha():
        outStr += char
   

print('한글과 영문자만 : ', outStr)

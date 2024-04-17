#파일 복사 코드
inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.write(inStr)

inFp.close()
outFp.close()
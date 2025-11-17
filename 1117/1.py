# 求最小公倍数最大公约数
a,b = map(int,input().split(','))
#********** Begin *********#
if a>b:
    c=a
    d=b
else:
    c=b
    d=a
while True:
    s1 = c%d
    if s1 == 0:
        global result1
        result1 = d
        break
    c = d
    d = s1 
result2 = int(a*b/result1)
print(f"{result1},{result2}")
        
#********** End **********#
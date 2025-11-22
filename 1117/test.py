s = list(map(str,input().split("")))
s1=list(s)
print(s)
while "-" in s:
    s.remove("-")
or_re = s[9]
re=0
for i in range(1,9):
    re = int(s[i-1])*i+re
re = re%11
if re == 10 and or_re == "X":
    print("Right")
    exit()
else:
    s1.remove("X")
    s1.append(re)
    r_re="".join(s1)
    print(r_re)
    exit()
if re == or_re:
    print("Right")
    exit()
else: 
    s1.pop()
    s1.append(re)
    r_re="".join(s1)
    print(r_re)
    exit()
    
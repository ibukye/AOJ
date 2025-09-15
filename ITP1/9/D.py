str=list(input())
ope_num=int(input())
for _ in range(ope_num):
    ope=input().split()
    if ope[0]=="replace":
        #print(f'ope1: {ope[1]}\nope2: {ope[2]}\nope3: {ope[3]}')
        str[int(ope[1]):int(ope[2])+1]=ope[3]
        #str[int(ope[1]):int(ope[2])]=ope[3]
        #print("str: ",str)
    elif ope[0]=="reverse":
        reversed_part=(str[int(ope[1]):int(ope[2])+1])[::-1]
        str[int(ope[1]):int(ope[2])+1]=reversed_part
        #print("str: ",str)
    else:#print(f"{str[int(ope[1]):int(ope[2])+1]}")
        print("".join(str[int(ope[1]):int(ope[2])+1]))

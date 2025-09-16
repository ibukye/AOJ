while 1:
    h,w=map(int,input().split())
    if h==0 and w==0:break
    print("#"*w)
    for _ in range(h-2):
        print("".join(["#","."*(w-2),"#"]))
    print("#"*w)
    print("")
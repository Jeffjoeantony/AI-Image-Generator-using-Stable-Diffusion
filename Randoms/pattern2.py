def pat(n):
    for i in range(n):
        for j in range(n-i,n):
            print(j , end = "")
        print()
        
    for i in range(n):
        for j in range(i,n):
            print(j , end = "")
        print()
        
pat(5)
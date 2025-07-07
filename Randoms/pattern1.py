def pat(n):
    for i in range(n):
        for j in range(n-i):
            print("* ", end = "")
        print()
        
pat(10)



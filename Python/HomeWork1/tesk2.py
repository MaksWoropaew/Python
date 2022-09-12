def table():
    print("-"*15)
    print("X","Y","Z", "result", sep="  ")
    print("-"*15)
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                result=not(X or Y or Z)==(not(X) and not(Y) and not(Z))
                print(f"{X}  {Y}  {Z}  {result}")
table()
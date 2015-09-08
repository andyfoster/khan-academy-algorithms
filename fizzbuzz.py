def fb():
    for x in range(1,101):
        if (x % 5==0) & (x % 3==0):
            print("Fizz Buzz (",x,")")
        elif(x%3==0):
            print("Fizz (",x,")")
        elif(x%5==0):
            print("Buzz (", x, ")")
        else:
            print(x)
fb()

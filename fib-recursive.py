#fibonacci recursive function
# finds the nth term in the fibonacci sequence
#but the recursive way!!


def fibonacci(n):
    print("ficonacci: "+str(n))
    # base case
    #if n == 0 or n == 1:
    #if n<2:
    if n == 0:
        return 0
    elif n==1:
        return 1

    else:
        return (fibonacci(n-1)+fibonacci(n-2))
        
    #eg 8
    # 7+6

##    if n == 0:
##        return 0
##    elif n==1:
##        return 1

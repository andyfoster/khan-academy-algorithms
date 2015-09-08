#fibonacci function
# finds the nth term in the fibonacci sequence


 #repeats until it has gone through n times
def fib(n):

    #creates a list with [0,1]
    terms = [0, 1]

    # already defined 2 items in the list, so sets i to 2
    # we want to enter the 2nd term when we enter the list
    i = 2
    
    while i <= n:
        print("fib while: "+str(i))

         #appends a new value that is the sum of the previous 2 terms
        terms.append(terms[i-1]+terms[i-2])
        ### the first time, i=2, so get L[1] and L[0]

        i = i + 1

    #prints all the terms so you can see it works
    print(terms)

     # terminates and returns the n term
    return terms[n]

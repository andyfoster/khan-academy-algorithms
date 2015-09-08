## recursion

def factorial(number):

    #base case
    if number <= 1:
        return 1
    else:
        return number*factorial(number-1)

#       return 4 * fac(4-1) *  

        #2 -> 2*(2-1)
        #3-> 3*2
        #4 ->4*(4-1)*




user_input = eval(input("Enter a non-neg int to take the factorial of: "))
print(factorial(user_input))

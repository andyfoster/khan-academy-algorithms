##def fact(num):
##    sum = num
##
###we need to multiply each number by the number less than it
##    
##    for i in range(num):
##        print(i)
##        sum = sum * i
##    print(sum)



def ask():
    number = eval(input("Enter a non-neg int to take the factorial of: "))
    return number


def factorial(number):
    
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return product

user_input = eval(input("Enter a non-neg int to take the factorial of: "))
print(factorial(user_input))

def fizzbuzz(num):
    while num >= 15:
        if num % 3 == 0:
            return('Fizz')
        elif num % 5 == 0:
            return ('Buzz')
        elif num % 15 == 0:
            return ('FizzBuzz')
        else:
            return(num)



def welcome(name):
    print(f"Welcome {name} to my repo!")

print(welcome("Aimee"))
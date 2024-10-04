FizzBuzz = int(1)
i =int(input())
while FizzBuzz <= i:
    if FizzBuzz % 3 == 0:
        if FizzBuzz %5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif FizzBuzz % 5 == 0:
        print("Buzz")
    else:
        print(FizzBuzz)
    FizzBuzz = FizzBuzz + 1
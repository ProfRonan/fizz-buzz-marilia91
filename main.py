número = input("Digite um número: ")
número = int(número)

if número % 3 == 0 and número % 5 == 0:
    print("FizzBuzz")
else: 
    if número % 3 == 0:
        print("Fizz")
    elif número % 5 == 0:
        print("Buzz")
    else: 
        print(número)

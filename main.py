"""i = int(input("Enter number: "))

for x in range(1):
    if x % 3 == 0 and x % 5 != 0:
        print("Fizz!")
    elif x % 5 == 0 and x % 3 != 0:
        print("Buzz!")
    elif x % 3 == 0 and x % 5 == 0:
        print("Fizzbuzz!")
    else:
        print(x)
"""

"""
for x in range(10):
    for y in range(10):
        print(str(x) + " " + str(y))
"""

print("FizzBuzz game")

end = input("Enter number: ")
end = int(end)

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
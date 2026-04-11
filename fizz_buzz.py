print("Wlcome to Fizz Buzz!")
def fizzbuzz(n):
        i=1
        while i <= n:
                if i % 3 == 0 and i % 7 == 0:
                        print("FizzBuzz")
                elif i % 3 == 0:
                        print("Fizz")
                elif i % 7 == 0:
                        print("Buzz")
                elif "3" in str(i):
                        print(" Almost Fizz")
                else:
                        print(str(i))
                i += 1
n = int(input())
fizzbuzz(n)
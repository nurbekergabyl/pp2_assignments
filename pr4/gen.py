# generators.py

# 1. Simple Iterator Example
numbers = [1, 2, 3, 4, 5]
my_iter = iter(numbers)

print("Iterator example:")
print(next(my_iter))
print(next(my_iter))


# 2. Custom Iterator Class
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current


print("\nCustom Iterator:")
for num in CountDown(5):
    print(num)


# 3. Generator Function
def square_numbers(n):
    for i in range(n):
        yield i * i


print("\nGenerator function:")
for square in square_numbers(5):
    print(square)


# 4. Generator Expression
gen_exp = (x * 2 for x in range(5))
print("\nGenerator expression:")
for value in gen_exp:
    print(value)
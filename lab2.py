def prime_num_generator():
    num = 0
    while True:
        yield num
        num += 1


generator = prime_num_generator()

print(next(generator))
print(next(generator))
print(next(generator))

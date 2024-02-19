from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print("Evens:", evens)
print("Odds:", odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))
print(evens & squares)

# Pass an iterable to the method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)

# Numbers that are odd but not prime
# Set difference is non-commutative
print(odds.difference(primes))
print(odds - primes)
print(primes - odds)
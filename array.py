numbers = [34, -12, 2]

print("lista01")
for i in numbers:
    print(i)

numbers.append(333)

print("\n")
print("lista02")
for i in numbers:
    print(i)

numbers.insert(1, 24)

print("\n")
print("lista03")
print(numbers[:])

numbers.remove(333)

print(numbers[:])
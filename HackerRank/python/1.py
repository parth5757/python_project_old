# Write a Python program that takes an input value n and displays the squares of all numbers from 0 to n - 1 on separate lines. Can you explain how the program works, and what happens if you input a value of 5 for n?

# if __name__ == '__main__':
#     n = int(input("Enter number: "))
#     s = [i **  2 for i in range(n)]
#     print(s)


# n = int(input("Enter a value for n: "))

# squares = [i ** 2 for i in range(n)]

# print("The squares of numbers from 0 to", n - 1, "are:", squares)

n = int(input())

for i in range(n):
    s = i ** 2
    print(s)


# n = int(input("Enter a value for n: "))

# for i in range(n):
#     square = i ** 2
#     print(square)

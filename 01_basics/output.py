# Arithmetic
x, y = 7, 3
print(x + y, x - y, x * y, x / y)    # 10 4 21 2.333...
print(x // y, x % y, x ** y)         # 2 1 343

# Comparison
print(x > y, x == y, x != y)         # True False True

# Assignment
x += 2   # same as x = x + 2
print(x)  # 9

# Logical
a, b = True, False
print(a and b, a or b, not b)        # False True True

# Membership
s = "hello"
print("h" in s, "z" not in s)        # True True

# Identity
lst1 = [1,2]
lst2 = [1,2]
lst3 = lst1
print(lst1 is lst2, lst1 is lst3)    # False True

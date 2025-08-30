# 대입 연산자
x = 6
y = 4

# 조건 연산자
z = x == y
print("x == y : ", z)
z = x != y
print("x != y : ", z)
z = x > y
print("x > y : ", z)
z = x >= y
print("x >= y : ", z)
z = x < y
print("x < y : ", z)
z = x <= y
print("x <= y : ", z)

z = x + y
print("x + y", z)
z = x - y
print("x - y", z)
z = x * y
print("x * y", z)
z = x / y
print("x / y", z)

z = x % y
print("x % y", z)
z = x // y
print("x // y", z)

z = x ** y
print("x ** y", z)

str_x = "hello"
str_y = "python"

str_z = str_x + str_y
print("str_x + str_y", str_z)

# unsupported operand type(s) for -: 'str' and 'str'
# str_z = str_x - str_y
# print("str_x - str_y:", str_z)

str_z = str_x * 2
print("str_x * 2", str_z)

array_x = [3, 6]
array_y = [4, 5]

array_z = array_x + array_y
print("array_x + array_y : ", array_z)

array_z = array_x * 2
print("array_x * 2 : ", array_z)

array_z = array_x * array_y[0] # 해당 인덱스에 있는 요소가 정수형일때만 가능
print("array_x * array_y[0] : ", array_z)
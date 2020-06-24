n1 = int(input("첫 번째 정수:  "))
n2 = int(input("두 번째 정수: "))
m = input("연산자: ")

if m == '+':
    print(n1, '+', n2, '=', n1+n2)

elif m == '-':
    print(n1, '-', n2, '=', n1-n2)

elif m == '*':
    print(n1, '*', n2, '=', n1 * n2)

else:
    print(n1, '%', n2, '=', n1 % n2)


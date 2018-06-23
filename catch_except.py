def dividedby(num):
    try:
        return 42/num
    except ZeroDivisionError: 
        print('Error divided by zero')

print(dividedby(2))
print(dividedby(12))
print(dividedby(0))
print(dividedby(1))

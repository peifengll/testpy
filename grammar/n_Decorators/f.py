'''
count = 2
total = 2


def averager(new_value):
    # nonlocal count, total
    count += 1
    total += new_value
    return total / count

print(averager(1))

# ╰─ python f.py
# Traceback (most recent call last):
#   File "D:\code\py\tests\grammar\n_Decorators\f.py", line 12, in <module>
#     print(averager(1))
#   File "D:\code\py\tests\grammar\n_Decorators\f.py", line 8, in averager
#     count += 1
# UnboundLocalError: local variable 'count' referenced before assignment

'''
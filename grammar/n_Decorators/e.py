count = 0
total = 0

def make_averager():
    # count = 1
    # total = 5
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager
print(make_averager()(0))

# ╰─ python e.py
#   File "D:\code\py\tests\grammar\n_Decorators\e.py", line 8
#     nonlocal count, total
#     ^
# SyntaxError: no binding for nonlocal 'count' found
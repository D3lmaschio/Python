# Handling DivisionByZeroException:

try:
    print(5/0)
except ZeroDivisionError as error:
    error.with_traceback()

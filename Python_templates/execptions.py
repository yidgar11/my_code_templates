__author__ = 'yidgar'

# General exception - almost all
try :
    x = 1 / 0
except Exception:
    print('Oops, we divided by zero!')

# Specific exeption , all the rest will not be caought
try :
    x = 1 / 0
except ZeroDivisionError:
    print('Oops, we divided by zero!')

# exception as
try :
    x = 1 / 0
except ZeroDivisionError as e:
    print(e.message)

## Several exception types
try :
    x = 1 / 0
except (ZeroDivisionError, KeyError):
    print('Oops, we divided by zero!')

## Multiple exception types
try :
    x = 1 / 0
except (ZeroDivisionError):
    print('Oops, we divided by zero!')
except (KeyError):
    print('Oops, we key errror')
else:
    print ("there was no exception")

## use finally - for cleanup - do something before the exception
try:
    x = 1 / 0
finally:
    print('Cleanup, even if there was an exception.')


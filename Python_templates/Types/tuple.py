__author__ = 'yidgar'

# https://www.w3schools.com/python/python_tuples.asp

## tuple is an immutable list

# list:
l = [1 ,2 , 3 ]
print (l)
print(len(l))
l.append(5)
del l[1]
print (l)

#tuple
t = (1 ,2, 3)
print(len(t))
## no option to append , remove etc'


## get many args - no linit
def filter_even_numbers(*args):
    return [number for number in args if number % 2 == 0]

filter_even_numbers(1, 3, 8) ## will return [8]
filter_even_numbers(3, 77, 89, 20, 100)  # will return [20, 100]



# get many key,val - no limit
def build_html_tag(tag, **kwargs):
    return '<{} {}>'.format(
        tag,
          ' '.join(
             '{}="{}"'.format(key, value) for key, value in kwargs.items()
         )
     )

print(build_html_tag('a', href='google.com'))
print(build_html_tag('div', id='content', style='float: left;'))

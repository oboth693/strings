my_string ='hello, world , !'
#default implicit order
print('{} {} {}' .format('hello','world', '!'))
#position arguments
print('{2} {0} {1}'.format('hello', 'world','!'))
#keyword arguments
print('{greeting} {name}'.format(greeting='hello', name ='world'))


#formating integers
print('{:d}'.format(10))
#formating binary
print('{:b}'.format(10))
#formating hexadecimal
print('{:x}'.format(10))
#formating floating point numbers
print('{:.2f}'.format(10.12345))
#formating exponent
print('{:e}'.format(10.12345))
#string alignment
print('{:<30}'.format('hello'))
print('{:>30}'.format('hello'))
print('{:^30}'.format('hello'))


#lower()
print('hello'.lower())
#upper
print('hello'.upper())
#join
print(''.join(['hello','world']))
#spirit
print('hello world'.split())
#find
print('hello world'.find('world'))
#replace
print('hello world'.replace('world','universe'))
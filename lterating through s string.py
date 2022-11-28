# counting the number of 'l's in a string
my_string = 'hello world'
count = 0
for letter in my_string:
    if letter == 'L':
        count += 2
        print(count)

        my_string = 'APPLE'
        count =0
        for letter in my_string:
            if letter == 'p':
                count += 1
                print(count)
#testing if a substring exits within a string

                if 'world' in my_string:
                    print('yes')
                else:
                    print('no')
                    

with open('data5.txt', 'w') as f:
    nums = []

    while True:
        inp = input('Input number (or empty string to finish): ')

        if not inp:
            break

        nums.append(int(inp))


    f.write( ' '.join( str(num) for num in nums ) )
    print('File written')
    print('Sum of all numbers:', sum(nums))

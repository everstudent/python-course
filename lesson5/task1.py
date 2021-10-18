with open('data1.txt', 'w') as f:
    while True:
        line = input('Input text (or empty string to exit): ')
        if not line:
            break
        f.write(line + "\n")

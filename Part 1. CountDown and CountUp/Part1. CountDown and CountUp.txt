def my_function(n):
    if n == 0:
        print('Blastoff!')
    elif n > 0:
        def countdown(n):
            if n > 0:
                print(n)
                countdown(n - 1)
            elif n == 0:
                print('Blastoff')
        my_function(countdown(n))
    elif n < 0:
        def countup(s, n):
            if n < 0:
                print(n)
                countup(s, n + 1)
            elif n == 0:
                print("Blastoff")
        my_function(countup(-1, n))

my_function(int(input(("number:"))))
try:
    n = int(input('Enter the number of terms in the Fibonacci sequence: '))

    if n <= 0:
        print('Please enter a positive integer.')

    else:
        fibonacci_sequence = [0, 1]

        for _ in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)

        print(f'Fibonacci sequence up to {n} terms: {fibonacci_sequence}')

except ValueError:
    print('Invalid input. Please enter a valid integer.')

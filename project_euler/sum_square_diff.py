def sum_sqaure_diff(n):

    sum_of_squares = (n * (n+1) * (2*n + 1))//6

    sum_of_numbers = (n * (n + 1))//2

    square_of_sum_of_numbers = sum_of_numbers ** 2

    diff = square_of_sum_of_numbers - sum_of_squares

    print diff


sum_sqaure_diff(100)

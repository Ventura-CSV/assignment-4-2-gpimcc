def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    for _ in range(2,N):
        nextnum = result[-1] + result[-2]
        result.append(nextnum)
    print("The sequence is", result)
    main()
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()

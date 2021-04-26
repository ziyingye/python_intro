if __name__ == '__main__':
    pass

    # Given a sequence of numbers, find the all odd number and between [-5, 5]
    # Using a while loop
    # Using a for loop
    # Using list comprehension
    # Given a sequence of numbers, find the all odd number and between [-5, 5]
    # Using a while loop
    # Using a for loop
    # Using list comprehension
    # Hint1: In part 1 you should initiate i as index of seq and increment it at the end of each loop iteration
    #       extract the element by call seq[INDEX]

    # Hint2: In part 2 you can use the same strategy as 1 but a better way is to directly extract the value
    #       # e.g. for i in seq: ... Note here i is not the index of seq, instead it is the value of seq at that index

    # Hint3: IN part 3 if you implementation is same as described as in part2 you can simply convert it into
    #       List comprehension as we shown in Lecture 2

    # End Notes: Always check back on Lecture covered. Google is your Friend!!
    seq = list(range(-20, 20, 3))
    print(seq)

    '''1. While Loop'''
    # ...
    i: int = 0
    lst: list = []
    # [-5,5] -> seq[i] < -5
    while i < len(seq):
        # if seq[i] % 2 != 0 and -5 <= seq[i] <= 5:
        #     lst.append(seq[i])
        if (seq[i] % 2 == 0) or (seq[i] < -5) or (seq[i] > 5):
            i += 1
            continue
        lst.append(seq[i])
        i += 1
    print(lst)

    '''2. For Loop'''
    ...
    lst = []
    for i in seq:
        if not i % 2 == 0 and -5 <= i <= 5:
            lst.append(i)
    print(lst)

    '''3. List Comprehension'''
    # ...
    lst = [i for i in seq if i % 2 != 0 and -5 <= i <= 5]
    print(lst)

# import required packages
#     deque
from collections import deque


if __name__ == '__main__':
    pass

    # ''' 1.Summation: '''
    # # TODO:
    # # Write a program to perform summation over `lst` and print the results and store in variable ans
    # lst1 = list(range(0, 10, 2))
    # # ...
    # # ans1 =
    # print(lst1)
    # a=0
    # for i in lst1:
    #     a=i+a
    # print(a)
    #
    #
    # # ''' 2. Indexing and Sorting '''
    # # # TODO:
    # # # Write a program to sorting the list in descending order
    # # # and inset a list of string in begin, middle and end
    # # # use both list and deque to solve the problem
    # # lst2 = [1, 50, 21, -6, 128, 10]
    # # str_lst = ["Hello", "python", "world"]
    # # # ...
    # # # ans2 =
    # #
    # lst2 = [1, 50, 21, -6, 128, 10]
    # ans2=sorted(lst2,reverse=True)
    # print(f"ans2 = {ans2}")
    # ans2.append ("world")
    # print(f"ans2 = {ans2}")
    # ans2.insert (3,"python")
    # print(f"ans2 = {ans2}")
    # ans2.insert (0,"Hello")
    # print(f"ans2 = {ans2}")
    # print(len(ans2))
    #
    # q = deque(sorted(lst2,reverse=True))
    # print(q)
    # q.appendleft("Hello")
    # q.append("world")
    # q.insert (3,"python")
    # print(q)
    # # # done
    # #
    # ''' 3. Even Numbers '''
    # # TODO:
    # # Given a tuple of integers, extract the even elements and sum them up
    # # Hint 1: Iterate through tuple use for loop
    # # Hint 2: Check even number by `%2 == 0`
    # # Hint 3: Either use variable addition in each iteration ,
    # #         or store even value first and perform summation same as in Part 1
    # # ...
    # # tup3 = (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, tuple(range(6)))
    # # # Hint use for loop to check type:
    # # #   E.g for i in ...:
    # # #             if isinstance(object , type):
    # # #                 do ...
    # # # ans3 =
    # # # a2 =0
    # # for i in tup3:
    # #     if isinstance(i, tuple):
    # #         a1 =0
    # #         for n in i:
    # #             if n%2 ==0:
    # #                 a1 =n+a1
    # #     else:
    # #         a2 =0
    # #         if i%2 ==0:
    # #             a2 =i+a2
    # #         print(a2)
    # # ans= a1 + a2
    # # print(ans)


    ''' 4. Create an Immutable Tuple of Element from List'''
    # Hint: extract every element and convert nested list(list of list or ...) in to a single list
    #       ans should be a single tuple contain all element in lst 4 and ensure nothing is mutable
    lst4 = ["Hi", [1, 2, 3], 1.5,  'a', ("Today", "2", 30)]
    # ans4 =
    # b= lst4[1]
    # print(b)
    # b=tuple(b)
    # print(b)
    ans = []
    for i in lst4:
        if isinstance(i, list):
            ans.extend(i)
        elif isinstance(i, tuple):
            for j in i:
                ans.append(j)
        else:
            ans.append(i)
    print(tuple(ans))


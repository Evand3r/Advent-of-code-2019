input = [int(x) for x in open('5.in').read().split(',')]

# def program(input):
#     length = len(input)
#     for i in range(0, length-1, 4):
#         one = input[i]
#         two = input[i+1]   #Set two as first argument, 1 position after i
#         three = input[i+2]   #Set three as second argument, 2 positions after i
#         four = input[i+3] #Get index for positioning the result
#
#         if one == 1:
#             input[four] = input[two] + input[three] #Sum to given index two and three
#         elif one == 2:
#             input[four] = input[two] * input[three] #Multiply to givenindex two and three
#         elif one == 99:
#             break   #if given index is 99: halt
#
#     return input[0] #return only the first value of the set
#
# def find_pair(input, num):
#     for noun in range(100):
#         for verb in range(100):
#             arr = input.copy()
#             arr[1] = noun
#             arr[2] = verb
#             if program(arr) == num:
#                 return [noun,verb]
#
# print(find_pair(data,19690720))

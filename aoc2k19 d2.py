data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
def program(input):
    length = len(input)
    for i in range(0, length-1, 4):
        one = input[i]
        two = input[i+1]   #Set two as first argument, 1 position after i
        three = input[i+2]   #Set three as second argument, 2 positions after i
        four = input[i+3] #Get index for positioning the result

        if one == 1:
            input[four] = input[two] + input[three] #Sum to given index two and three
        elif one == 2:
            input[four] = input[two] * input[three] #Multiply to givenindex two and three
        elif one == 99:
            break   #if given index is 99: halt

    return input[0] #return only the first value of the set

def find_pair(input, num):
    for noun in range(100):
        for verb in range(100):
            arr = input.copy()
            arr[1] = noun
            arr[2] = verb
            if program(arr) == num:
                return [noun,verb]

print(find_pair(data,19690720))
# print(program([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]))

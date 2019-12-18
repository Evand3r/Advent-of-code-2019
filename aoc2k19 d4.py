sum = 0

for passw in range(246540,787419+1):
    digits = str(passw)
    #Tue if it has a pair and is not part of trio
    pair = any([(i == 0 or digits[i]!= digits[i-1]) and digits[i] == digits[i+1] and (i == len(digits)-2 or digits[i] != digits[i+2]) for i in range(len(digits)-1)])
    #True if the number decreases
    decre = any([digits[i] > digits[i+1] for i in range(len(digits)-1)])
    if pair and not decre:
        sum += 1

print(sum)

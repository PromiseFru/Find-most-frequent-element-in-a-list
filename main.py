def mod(input):
    counter = 2
    num = []

    for i in input:
        currentCounter = input.count(i);
        if(currentCounter >= counter):
            counter = currentCounter
            num.append(i)
    
    if(num == input):
        return "no mod found"

    num = list(set(num))

    if(len(num) < 1):
        return "no mod found"

    return num

input = [1,1, 2,2,2, 3]
print(mod(input))
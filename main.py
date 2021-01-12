def mod(input):
    counter = 0
    num = []

    for i in input:
        currentCounter = input.count(i);
        if(currentCounter > counter):
            counter = currentCounter
            num = []
            for j in input:
                if(input.count(j) == counter):
                    num.append(j)
    
    if(num == input):
        return "no mod found"

    num = list(set(num))

    if(len(num) < 1):
        return "no mod found"

    return num

input = [1,1, 2,2,2, 3, 5,5,5,5]

print(mod(input))
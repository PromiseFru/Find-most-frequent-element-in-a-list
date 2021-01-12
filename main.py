def mostFrequentNumber(input):
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
        return "All numbers have same frequency"
    else:
        num = list(set(num))

    return num

input = [1,2,3,3,4,2]

print(mostFrequentNumber(input))
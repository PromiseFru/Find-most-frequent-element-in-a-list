def mostFrequentNumber(input):
    # counter holds highest frequency
    # num holds numbers with highest frequency
    counter = 0
    num = []

    # loop through input array to find number with highest frequency
    for i in input:
        # currentCounter holds frequency for each element in the array
        # count method looks for the frequency of each element in the array
        currentCounter = input.count(i);
        # if any frequency(currentCounter) higher than the highest frequency(counter) is found, change the highest value(currentCounter) to the current value(counter)
        if(currentCounter > counter):
            counter = currentCounter
            # for every new highest value found, clear list of number(s) with highest frequency
            num = []
            # loop through input array and find all numbers with the current highest frequency(counter) 
            for j in input:
                if(input.count(j) == counter):
                    num.append(j)
    
    # if list of numbers with highest frequency(num) is same as input list, then all numbers have the same frequency
    if(num == input):
        return "All numbers have same frequency"
    else:
        # the set function removes all duplicates from the num variable, the list function converts the set function output back to an array
        num = list(set(num))

    return num

# test
input = [1,2,3,3,4,2]

print(mostFrequentNumber(input))
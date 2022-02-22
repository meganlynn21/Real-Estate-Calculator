# Real Estate Calculator

listOfNums = []

#This function recieves the value from salesPrice and returns a float
def getFloatInput():
    while True:
        try:
            salesPrice = float(input("Enter property sales value: "))
            if salesPrice > 0:
                return salesPrice
                break
            print("Enter a numeric value greater than 0")
        except ValueError:
            print("Input must be a numeric value")

# This function gets the median of the list
def getMedian(medianOfList):
    listOfNums.sort()
    if len(listOfNums) % 2 != 0:
        middle_index = int((len(listOfNums) - 1) / 2)
        listOfNumsFormatted = format(listOfNums[middle_index],"5,.2f")
        return listOfNumsFormatted
    elif len(listOfNums) % 2 == 0:
        middle_index_1 = int(len(listOfNums) / 2)
        middle_index_2 = int((len(listOfNums) / 2) - 1)
        sumOfIndex1And2 = listOfNums[middle_index_1] + listOfNums[middle_index_2]
        averageOfIndex = sumOfIndex1And2 / 2
        averageFormatted = format(averageOfIndex, "5,.2f")
        return averageFormatted
   
# This function uses a list to store the salesPrice values in it and also asks user if they want to add another value.
def main():
    while True:
        listOfNums.append(getFloatInput())
        repeat = str(input("Enter another value Y or N: "))
        repeat = repeat.lower()
        while True:
            if repeat == "y":
                break
            elif repeat == "n":
                printValues()
                break
            else:
                repeat = str(input("Enter another value Y or N: "))
                repeat = repeat.lower()
                repeat

#Get minimum of list
def sort_Min(lst):
    lstSorted = sorted(lst)
    minOfList = min(lstSorted)
    minOfListFormatted = format(minOfList,"5,.2f")
    return minOfListFormatted

# Get maximum of list
def sort_Max(lst):
    lstSorted = sorted(lst)
    maxOfList = max(lstSorted)
    maxOfListFormatted = format(maxOfList,"5,.2f")
    return maxOfListFormatted

# Gets total
def totalValue(lst):
    lstSorted = sorted(lst)
    sumOfList = sum(lstSorted)
    sumOfListFormatted = format(sumOfList,"5,.2f")
    return sumOfListFormatted

# Gets average of list
def averageValue(lst):
    lstSorted = sorted(lst)
    averageOfList = sum(lstSorted) / len(listOfNums)
    averageOfListFormatted = format(averageOfList,"5,.2f")
    return averageOfListFormatted

# Gets commision Value
def commisionValue(lst):
    lstSorted = sorted(lst)
    total = sum(lstSorted)
    commission = total * .03
    commissionFormatted = format(commission,"5,.2f")
    return commissionFormatted

# This function prints values on screen of min, max, total, average, median, and commission 
def printValues():
    for i in range (0, len(listOfNums)):
        listOfNumsRounded = format(listOfNums[i], "15,.2f")
        print(f"Property {i + 1} ${listOfNumsRounded}")
    print(format("Minimum: $","25s"),sort_Min(listOfNums))
    print(format("Maximum: $","25s"),sort_Max(listOfNums))
    print(format("Total:  $","25s"),totalValue(listOfNums))
    print(format("Average:  $","25s"),averageValue(listOfNums))
    print(format("Median: $","25s"),getMedian(listOfNums))
    print(format("Commission: $","25s"),commisionValue(listOfNums))
    exit()                    

main()

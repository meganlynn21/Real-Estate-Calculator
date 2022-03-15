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
def getMedian():
    if len(listOfNums) % 2 != 0:
        return listOfNums[int((len(listOfNums)-1)/2)]
    else:
        return (listOfNums[int(len(listOfNums)/2)])
        + (listOfNums[int((len(listOfNums)/2)-1)])/2
   
# This function uses a list to store the salesPrice values in it and also asks user if they want to add another value.
def main():
    while True:
        listOfNums.append(getFloatInput())
        repeat = str(input("Enter another value Y or N: ")).lower()
        if repeat == "y":
            continue
        elif repeat == "n":
            listOfNums.sort()
            printValues()
            break
        else:
            repeat = str(input("Enter another value Y or N: "))

#Get minimum of list
def sort_Min():
    return min(listOfNums)

# Get maximum of list
def sort_Max():
    return max(listOfNums)

# Gets total
def totalValue():
    return sum(listOfNums)

# Gets average of list
def averageValue():
    return sum(listOfNums)/len(listOfNums)

# Gets commision Value
def commisionValue():
     return sum(listOfNums) * .03

# This function prints values on screen of min, max, total, average, median, and commission
def printValues():
    for i in range (0, len(listOfNums)):
       print(f"Property {i + 1} $" + format(listOfNums[i], "15,.2f"))
    print(format("Minimum: ", "25s"), "$", format(sort_Min(), "5,.2f"))
    print(format("Maximum: ", "25s"), "$", format(sort_Max(), "5,.2f"))
    print(format("Total:  ", "25s"), "$", format(totalValue(), "5,.2f"))
    print(format("Average:  ", "25s"), "$", format(averageValue(), "5,.2f"))
    print(format("Median: ", "25s"), "$", format(getMedian(), "5,.2f"))
    print(format("Commission: ", "25s"), "$", format(commisionValue(), "5,.2f"))

            
main()

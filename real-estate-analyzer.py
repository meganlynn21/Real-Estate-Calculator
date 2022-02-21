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

def main():
    addToList = []
    while True:
        addToList.append(getFloatInput())
        print(addToList)
        repeat = str(input("Enter another value Y or N: "))
        repeat = repeat.lower()
        while True:
            if repeat == "y":
                break
            elif repeat == "n":
                exit()
            else:
                repeat = str(input("Enter another value Y or N: "))
                repeat = repeat.lower()
                repeat
                        
main()
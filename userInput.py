
def userInput(rangeType: str):
    while True:
        try:
            numStr = input(f"\nPlease choose a {rangeType} non-negative number.\n{rangeType.capitalize()} Number: ")
            
            # Check if input contains only digits
            if not numStr.isdigit():
                print("Try Again. Only digits allowed")
                continue
                
            num = int(numStr)
            
            if num < 0:
                print("Try Again! Only positive numbers are allowed")
                continue
                
            return num
            
        except ValueError:
            print("Try Again. Please enter a valid number")
            continue
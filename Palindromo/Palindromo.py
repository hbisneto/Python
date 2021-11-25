def sumNumbers(number):
    reverse = str(number)[::-1]
    sumarise = int(number) + int(reverse)
    return sumarise

def checkPalindrome(number):
    reverse = str(number)[::-1]

    if(int(number) == int(reverse)):
        print(f'{number} it is a palindrome')
    else:
        print(f'{number} it is not a palindrome')
        newNumber = sumNumbers(number)
        checkPalindrome(newNumber)

number = input("What is the number? ")
try:
    int(number)
    checked = True
except ValueError:
    checked = False

if(checked == True):
    print(checkPalindrome(number))
else:
    print("This is not a number")
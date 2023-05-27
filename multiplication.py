
x = 5678
y = 1234
 
#This is a regular multiplication that recives two arrays wich are a numbers and outputs the result.
#O^n
def schoolmultiplication(x, y):
    numy_str = str(y)
    result = 0
    counter = 0
    adition = 0
    multiplication = 0
    for digit in reversed(numy_str): 
        multiplication = int(numy_str) * x
    adition = multiplication  + (10 ** counter)
    print(multiplication)
    return result

def ordinarymultiplication(x,y):
    numXStr = str(x)
    numYStr = str(y)
    multiplication = 0

    for yDigit in reversed (numYStr):
        for xDigit in reversed (numXStr):
            multiplication =  yDigit * xDigit
            



    return 0
      

print(schoolmultiplication(x,y))
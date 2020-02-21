# first to solve but could use some cleanup
def isPolyDivisible(num):
    string = str(num)
    counter = 1
    value = ""
    passed = 0
    for number in string:
        value = value + number
        x = int(value)/counter
        if (x % 1 == 0.0):
            print("number / counter = ", value, "/",
                  counter, int(value)/counter, "// works")
            passed = passed + 1
        else:
            print("number / counter = ", value, "/", counter,
                  int(value)/counter, "// does not work")
        counter = counter + 1
    if (passed == len(string)):
        print(string, "is a divisible number", passed, len(string))
    else:
        print(string, "is not adivisible number", passed, len(string))

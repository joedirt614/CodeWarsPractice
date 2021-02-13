# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def find_smallest_int(arr):
    arr.sort()
    return(arr[0])

def longest(a1,a2):
    newstr = a1+a2
    return(''.join(sorted(set(newstr))))
    """print("Concatenate the string: " + newstr)
    newstr = set(newstr) #convert to set - unordered, unique items
    print("Set: ",newstr)
    newstr=sorted(newstr)
    print("Sorted list: ",newstr)
    newstr=''.join(newstr)
    print("Converted back to string",newstr)"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    print(longest(a, b))

    """ print_hi('PyCharm')
    array1 = [34,15,88,2]
    array2 = [34, -345, -1, 100]
    print(find_smallest_int(array2)) """



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

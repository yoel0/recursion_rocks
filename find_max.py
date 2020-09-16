# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(L):
    # Write code here
    length = len(L)
    if length == 1:
        return L
    elif L[length-1] >= L[length-2]:
        del L[length-2]
    elif L[length-1] <= L[length-2]:
        del L[length-1]
    return find_max(L)


print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45

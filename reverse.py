# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    # Write code here
    if len(ss) == 0:
        return ""
    else:
        return reverse(ss[1:]) + ss[0]
        # return ss[-1] + reverse(ss[:-1])


print(reverse(str(input('reverse string: '))))

# print(reverse(""))
# => ""
# print(reverse("a"))
# => "a"
# print(reverse("ab"))
# => "ba"
# print(reverse("computer"))
# => "retupmoc"
# print(reverse(reverse("computer")))
# => "computer"

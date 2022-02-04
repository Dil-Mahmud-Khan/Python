is_male = False
is_tall = True
if is_male and is_tall:
    print("Your are a tall mail")
elif is_male and not(is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are a  not male but tall")
else:
    print("You are neither male nor tall")

print("\n")

print("New lesson\n")
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3 :
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


print(max_num(2, 5, 8))






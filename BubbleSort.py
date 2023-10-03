def swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2
ran = int(input("Enter the range of numbers : "))
l1 = []
print("Enter the numbers : ")
for i in range(ran):
    l1.append(int(input()))
dup_ran = ran
for count in range(ran - 1):
    for i in range(dup_ran - (count + 1)):
        j = i + 1
        if(l1[i] > l1[j]):
            l1[i], l1[j] = swap(l1[i], l1[j])
print(l1)
        
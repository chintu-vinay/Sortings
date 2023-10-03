def swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2
ran = int(input("Enter the range of numbers : "))
l1 = []
print("Enter the numbers : ")
for x in range(ran):
    l1.append(int(input()))
i = 0
for count in range(ran - 1):
    j = i + 1
    while(i < j):
        if(l1[i] > l1[j]):
            l1[i], l1[j] = swap(l1[i], l1[j])
        j = i
        while((j - 1) >= 0 and l1[j - 1] > l1[j]):
            l1[j - 1], l1[j] = swap(l1[j - 1], l1[j])
            j -= 1
        i += 1
print(l1)
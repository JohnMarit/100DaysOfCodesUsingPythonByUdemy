target = int(input("Enter the numbers you want to claculate the range from \n")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)
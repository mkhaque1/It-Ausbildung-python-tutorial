# This is a simple while loop that prints numbers from 1 to 5. 
# The loop continues as long as the condition (i < 6) is true. 
# Inside the loop, it prints the current value of i and then increments i by 1.
# += increments the value of i by 1 in each iteration of the loop.
# continue statement , break statement

i = 1
while i < 5:
  print(i)
  if i == 3:
    break  # This will exit the loop when i equals 3
  i += 1

# for loop

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for x in fruits:
  if x == "cherry":
    continue  # This will skip the rest of the loop for "cherry" and move to the next iteration
  print(x)





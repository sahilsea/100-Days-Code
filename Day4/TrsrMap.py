line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
#print(f"{line1}\n{line2}\n{line3}")

ls_pos = list(position)
if ls_pos[0] == "A":
  ls_pos[0] = 0
elif ls_pos[0] == "B":
  ls_pos[0] = 1
elif ls_pos[0] == "C":
  ls_pos[0] = 2

if ls_pos[1] == "1":
  ls_pos[1] = 0
elif ls_pos[1] == "2":
  ls_pos[1] = 1
elif ls_pos[1] == "3":
  ls_pos[1] = 2


map[ls_pos[1]][ls_pos[0]] = "X"
print(f"{line1}\n{line2}\n{line3}")
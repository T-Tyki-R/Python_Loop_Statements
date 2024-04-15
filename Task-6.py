# Advancced Looping Techniques

# Task 1
# Use genre list from aissignment 5
# Store sliced items in a new list (2, 3, 4)
# Loop through new list

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genresList = genres[1:4]
for i in genresList:
  print(i)
   

# Task 2
# Use genre list from assignment 5
# Loop through list
# append music at the end of each genre

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
musicList = [i + " music" for i in genres if i in genres]

print(musicList)


# Task 3
# Loop through a range from 0 - 10
# Decrement from 10
# print comment after 1

for i in range(10, 0, -1):
   print(i) 
   if i == 1:
    print("The beat drops now!")
    

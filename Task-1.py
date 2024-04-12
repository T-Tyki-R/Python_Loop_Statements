import random
# The Range Riddle 

# initialize a list that stores moods
# initialize a list that store the days of the week
# loop through a week list using range and len methods
# apply random method on the mood list
# print the day of the week with the randomized mood

moodsList = ["Happy", "Sad", "Neutral", "Upset", "Calm", "Energetic"]
weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(len(weekList)):
    randMood = random.choice(moodsList).lower()
    print(f"On {weekList[day]}, you were feeling {randMood}.")
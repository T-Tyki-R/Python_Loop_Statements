import random
# The Double Scoop w/ Nested Loops

# initialize a list that stores moods
# initialize a list that store the days of the week
# loop through a week list 
# loop through a time list 
# loop through a mood list 
# apply random method on the mood and time lists
# print the day of the week with the randomized mood and time

moodsList = ["Happy", "Sad", "Neutral", "Upset", "Calm", "Energetic"]
weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
timeList = ["Morning", "Afternoon", "Night"]

for day in range(len(weekList)):
    for time in range(len(timeList)): 
        for mood in range(len(moodsList)):
            randMood = random.choice(moodsList).lower()
            randTime = random.choice(timeList).lower()   
            print(f"On {weekList[day]} {randTime}, you were feeling {randMood}.") # Is this the expected result?

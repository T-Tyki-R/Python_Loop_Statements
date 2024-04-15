import random
# Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    track = random.randint(1, 21)
    if genres[i] =='Jazz':
        print(f"Track #{track}: Right Time")
    elif genres[i] =='Rock':
        print(f"Track #{track}: Karma")
    elif genres[i] =='Hip-hop':
        print(f"Track #{track}: Love Me Like No Other")
    elif genres[i] =='Classical':
        print(f"Track #{track}: Luxuriate Waltz")

# Task 2
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']   
i = 0

while(i < len(genres)):
    track = random.randint(1, 21)
    if genres[i] =='Jazz':
        print(f"Track #{track}: Right Time")
    elif genres[i] =='Rock':
        print(f"Track #{track}: Karma")
    elif genres[i] =='Hip-hop':
        print(f"Track #{track}: Love Me Like No Other")
        break
    elif genres[i] =='Classical':
        print(f"Track #{track}: Luxuriate Waltz")
    i += 1

# Task 3
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']   

for i in (range(len(genres))):
    track = random.randint(1, 21)
    if genres[i] =='Jazz':
        print(f"Light show is ready for track #{track}")
    elif genres[i] =='Rock':
        print(f"Light show is ready for track #{track}")
    elif genres[i] =='Hip-hop':
        print(f"Light show is ready for track #{track}")
    elif genres[i] =='Classical':           
        break

import time
starttime=time.time()
with open('p6.pgn', 'r') as file:
    lines = file.readlines()
tournament_count = 0
for i in range(len(lines)):
    if 'Event' in lines[i] and 'tournament' in lines[i]:
        tournament_count += 1
tournament=tournament_count
endtime=time.time()
duration=starttime-endtime
with open("output.txt","w") as file:
    file.write(f"{tournament}\n{duration}")

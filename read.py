import time
starttime=time.time()
with open('C:\\Users\\vejam\\tournament-counter\\p6.pgn','r') as file:
    s=file.read()
    count1=s.count("tournament")
    time1=time.time()-starttime
with open("output.txt","w") as file:
    file.write(f"{count1}\n{time1}")
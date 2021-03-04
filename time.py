
from datetime import datetime
curr_time = datetime.now()

Mtime = int(curr_time.strftime('%M'))
Stime = int(curr_time.strftime('%S'))

Strat = str(Mtime)+str(Stime)

Stime = Stime+10
# if Stime+10 > 60:
#     Mtime+1

# End = Stime*2 + 10 - 60

End = str(Mtime)+str(Stime+10)
print("Start time : " +str(Mtime)+":"+str(Stime))
print("End time : " +str(Mtime)+":"+str(Stime))
while True:
    # print(str(Mtime)+":"+str(Stime))
    if str(Mtime)+str(Strat) == End:
        break
    
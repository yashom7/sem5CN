# window = 4
# win=0
# frame =9
# i=-1
# prev=0
# ans = []

# err=[0,1,0,0,0,1,0,0,0,0]
# frame =9

# while i < frame:
#     i += 1

#     print("i=",i)


#     if win == 4:
#         win =0

#     win += 1
#     print("sending: ",i) 
#     ans.append(i)

#     if err[i] == 1:
#         print("NACK sent for ",i)
#         ans.pop(i)
#         prev = i
#     elif prev!=0 and win==1:
#         print('sending frame: ',prev)
#         ans.append(prev)    
#         prev=0
#         err[prev]=0
#     # else:
#     #     print("recv:",ans.pop(0))

# print(ans)

import time

window = 4
win = 0
prev = 0
frame = 9
i = -1
ans = []

err = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]

while i < frame:
    i += 1
    
    print("i = ", i)
    
    if win == 4:
        win = 0
    
    win += 1

    print("Sending : ", i)
    ans.append(i)

    if err[i] == 1:
        print("NACK sent for : ", i)
        ans.pop(i)
        prev = i
    
    elif prev != 0 and win == 1:
        print("Sending Frame : ", prev)
        ans.append(prev)
        prev = 0
        err[prev] = 0

    time.sleep(0.25)

print(ans)
 
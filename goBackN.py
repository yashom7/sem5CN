import time
import random

t = 5
window = 3
prev = -1
ans = []

while t > 0:
    t -= 1
    if prev ==  window - 1:
        prev -= 1
    time.sleep(0.5)
    i  = -1
    while i < window - 1:
        i += 1
        time.sleep(0.25)
        send =  i
        print("Sending ", send, end=" ")
        err = random.randint(0, window)
        if err == send:
            print("**ERROR** sending NAK for  ", send)
        else:
            print("Received ", send)
            if send != 0 and prev + 1 != send:
                print("Go Back", send)
                ans.append(-1 * send)
                i = prev
            else:
                ans.append(send)
                prev = send

print(ans)
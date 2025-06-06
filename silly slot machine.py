import random
import time
w = 2
e = input("say slot to use the silly slot machine he he answer: ")
bal = 0
while w == 2:
    if e == "slot":
        pass
    else:
        print("nu")
        quit()
    s = input("type spin to spin answer:")
    if s == "spin":
        pass
    else:
        print("ill let you do it anyways")
    print("let's go GAMBLING")
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    print(f"number 1:{a}")
    time.sleep(1)
    print(f"number 2:{b}")
    time.sleep(1)
    print(f"number 3:{c}")
    v = a + b + c
    v = v / 3
    if a == b:
        bal = bal + 15
        print("noice")
    elif c == b:
        bal = bal + 15
        print("noice")
    elif c == a:
        bal = bal + 15
        print("noice")
    elif c == v:
        bal = bal + 100
        print("jackput baby")
    else:
        bal = bal - 2
        print("womp womp")
    print(f"balance:{bal}")





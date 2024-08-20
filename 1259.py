while(True):
    text = input()

    if text == "0": exit()
    elif text == text[::-1]: print("yes")
    else: print("no")
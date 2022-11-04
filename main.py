def gettime():
    starttime = str(input("Enter start time: "))
    endtime = str(input("Enter end time: "))
    print("")

    if checklen(starttime) and checklen(endtime) is True:
        sh, sm = splithm(starttime)
        eh, em = splithm(endtime)

        if verify(sh, sm) and verify(eh, em) is True:
            x = sh*60+sm
            y = eh*60+em
            return x, y


def splithm(x):
    hourslice = slice(2)
    minslice = slice(2, 4)

    a = int(x[hourslice])
    b = int(x[minslice])

    return a, b


def checklen(a):
    if len(a) != 4:
        t = str(input("Invalid entry, try again? "))

        if t.upper() == "Y" or t.upper() == "YES":
            print("")
            main()
        else:
            print("Goodbye!")
            exit()
    else:
        return True


def verify(hour, mins):
    h = hour
    m = mins

    if 0 <= h <= 23 and 0 <= m <= 59:
        return True
    else:
        t = str(input("Invalid entry, try again? "))

        if t.upper() == "Y" or t.upper() == "YES" or t == "1":
            print("")
            main()
        else:
            print("Goodbye!")
            exit()


def timemathtime(s, e):
    dif = float((e - s) / 60)
    flath = math.floor((e - s) / 60)
    remmin = (e - s) % 60

    print(round(dif, 2), "hours")
    print(flath, "hours and", remmin, "minutes")
    print("")


def main():
    while True:
        start, end = gettime()
        timemathtime(start, end)

        again = str(input("Run again? "))
        if again.upper() != "Y" and again.upper() != "YES" and again != "1":
            print("Goodbye!")
            exit()
        else:
            print("")


if __name__ == '__main__':
    import math
    main()

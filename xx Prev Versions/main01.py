def gettime():
    starttime = str(input("Enter start time: "))
    endtime = str(input("Enter end time: "))
    print("")

    checklen(starttime, endtime)

    hourslice = slice(2)
    minslice = slice(2, 4)

    sh = int(starttime[hourslice])
    sm = int(starttime[minslice])

    eh = int(endtime[hourslice])
    em = int(endtime[minslice])

    if verify(sh, sm) and verify(eh, em) is True:
        x = sh*60+sm
        y = eh*60+em
        return x, y


def checklen(a, b):
    if len(a) != 4 or len(b) != 4:
        t = str(input("Invalid entry, try again? "))

        if t.upper() == "Y" or t.upper() == "YES":
            print("")
            gettime()
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

        if t.upper() == "Y" or t.upper() == "YES":
            print("")
            gettime()
        else:
            print("Goodbye!")
            exit()


if __name__ == '__main__':
    import math

    while True:
        start, end = gettime()

        dif = float((end - start)/60)
        flath = math.floor((end - start)/60)
        remmin = (end - start) % 60

        print(round(dif, 2), "hours")
        print(flath, "hours and", remmin, "minutes")
        print("")

        again = str(input("Run again? "))
        if again.upper() != "Y" and again.upper() != "YES":
            print("Goodbye!")
            break
        else:
            print("")

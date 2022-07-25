'''iwannadie'''

def  main():
    '''pen-ngong'''
    fromm = input()
    too = input()
    time = input()
    hour = int(time[0:2])
    natee = int(time[3:5])
    time2 = time[6:8]
    if too == "To Sydney (SYD)":
        if time2 == "AM":
            print("BKK - SYD")
            print(time[0:5], "PM")
        else:
            print("BKK - SYD")
            print(time[0:5], "AM")
    elif too == "To Ho Chi Minh (SGN)":
        hour += 1
        natee += 50
        if hour >= 12 and time2 == "AM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
                print("BKK - SGN")
                print("%02d"%hour+":"+str(natee)+"PM")
        elif hour >= 12 and time2 == "PM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
                print("BKK - SGN")
                print("%02d"%hour+":"+str(natee)+"AM")
        else:
            if natee >= 60:
                natee -= 60
                hour += 1
                print("BKK - SGN")
                print("%02d"%hour+":"+str(natee), time2)
    elif too == "To Atlanta Georgia  (ATL)":
        hour += 9
        natee += 55
        if hour >= 12 and time2 == "AM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - ATL")
            print("%02d"%hour+":"+str(natee)+"PM")
        elif hour >= 12 and time2 == "PM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - ATL")
            print("%02d"%hour+":"+str(natee), "AM")
        else:
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - ATL")
            print("%02d"%hour+":"+str(natee), time2)
    elif too == "To Vancouver Canada(YVR)":
        hour += 2
        natee += 20
        if hour >= 12 and time2 == "AM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - YVR")
            print("%02d"%hour+":"+str(natee)+"PM")
        elif hour >= 12 and time2 == "PM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - YVR")
            print("%02d"%hour+":"+str(natee), "AM")
        else:
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - YVR")
            print("%02d"%hour+":"+str(natee), time2)
    elif too == "To Kathmandu (KTM)":
        hour += 23
        natee += 45
        if hour >= 12 and time2 == "AM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - KTM")
            print("%02d"%hour+":"+str(natee)+"PM")
        elif hour >= 12 and time2 == "PM":
            hour -= 12
            if natee >= 60:
                natee -= 60
                hour += 1
                print(hour)
            print("BKK - KTM")
            print("%02d"%hour+":"+str(natee), "AM")
        else:
            if natee >= 60:
                natee -= 60
                hour += 1
            print("BKK - KTM")
            print("%02d"%hour+":"+str(natee), time2)


main()





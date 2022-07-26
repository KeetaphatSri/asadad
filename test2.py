"""Prepro"""

def main():
    """Prepro"""
    numlist = []
    ans = 0
    while True:
        num = input()
        numlist.append(num)
        if num == "+" or num == "-" or num == "*" or num == "/":
            break
    if numlist[len(numlist)-1] == "+":
        numlist.pop(len(numlist)-1)
        for i in numlist:
            ans += int(i)
    elif numlist[len(numlist)-1] == "-":
        numlist.pop(len(numlist)-1)
        ans = int(numlist[0])
        numlist.pop(0)
        for i in numlist:
            ans -= int(i)
    elif numlist[len(numlist)-1] == "*":
        numlist.pop(len(numlist)-1)
        ans = int(numlist[0])
        numlist.pop(0)
        for i in numlist:
            ans *= int(i)
    elif numlist[len(numlist)-1] == "/":
        numlist.pop(len(numlist)-1)
        ans = int(numlist[0])
        numlist.pop(0)
        for i in numlist:
            ans /= int(i)
    print("%.2f" %ans)
main()

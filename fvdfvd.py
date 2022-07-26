"""ตัวเลขที่มีอยู่"""


def main():
    """ print sum """
    length = int(input())
    pop = 0
    if length <= 0:
        return print("No Tape Measure")
    while True:
        text = input()
        if text == "No more!":
            break
        if int(text) <= length  and text.isnumeric():
            pop += int(text)
    if pop == 0:
        print("Not Found Number")
    else:
        print("Sum of Found Number = "+str(pop))


main()

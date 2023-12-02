import re

NUMBERS_STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def calibration():
    sum = 0
    with open("./Day_One/calibration_document.txt") as doc:
        for line in doc:
            found_str = False

            for num in NUMBERS_STRINGS:
                if num in line:
                    found_str = not found_str
                    break
            
            if found_str:
                print("need to do new calibrating")
            else:
                print(find_calibration_val(line))
                sum += int(find_calibration_val(line))


    print(sum)


def find_calibration_val(txt):
    num = ""

    for _ in txt:
        if is_Int(_):
            num += _
            break

    txt = txt[::-1]

    for _ in txt:
        if is_Int(_):
            num += _
            break

    return num

def split(s):
    head = s.rstrip('0123456789')



def is_Int(a):
    try:
        temp = int(a)
        return True
    except:
        return False

if __name__ == "__main__":
    calibration()

    #match = re.split(r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)', 'zoneight234')

    #print(match)
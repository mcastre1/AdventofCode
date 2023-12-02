import re

NUMBERS_STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

NUMBER_STRINGS_BACKWARDS = [item[::-1] for item in NUMBERS_STRINGS]

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
                 sum += int(new_calibration(line))
             else:
                 #print(find_calibration_val(line))
                 sum += int(find_calibration_val(line))


    print(sum)
    # text = "sixgtxr2fourrdkjg"
    # found_str = False

    # for num in NUMBERS_STRINGS:
    #     if num in text:
    #         found_str = not found_str
    #         break

    # if found_str:
    #     sum += int(new_calibration(text))
    # else:
    #     #print(find_calibration_val(line))
    #     sum += int(find_calibration_val(text))

    print(sum)





def switch(item):
    if item == 'one':
        return 1
    elif item == 'two':
        return 2
    elif item == 'three':
        return 3
    elif item == 'four':
        return 4
    elif item == 'five':
        return 5
    elif item == 'six':
        return 6
    elif item == 'seven':
        return 7
    elif item == 'eight':
        return 8
    else:
        return 9

def new_calibration(txt):
    print(txt)
    cal_list = re.split(r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)', txt)
    new_list = [item for item in cal_list if not item == '']
    new_list = new_list[:-1]
    num = ''

    for item in new_list:
        if item in NUMBERS_STRINGS:
            num += f"{switch(item)}"
            break
        else:
            if is_Int(item):
                num += item
                break
    txt = [c for c in txt[::-1]]
    txt.pop(0)
    txt = ''.join(txt)

    print("- " + txt)

    cal_list = re.split(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9)', txt)
    new_list = [item for item in cal_list if not item == '']
    new_list = new_list[:-1]
    print(new_list)


    for item in new_list:
        if item in NUMBER_STRINGS_BACKWARDS:
            num += f"{switch_backwards(item)}"
            break
        else:
            if is_Int(item):
                num += item
                break

    print(num)

    return num

def switch_backwards(item):
    if item == 'eno':
        return 1
    elif item == 'owt':
        return 2
    elif item == 'eerht':
        return 3
    elif item == 'ruof':
        return 4
    elif item == 'evif':
        return 5
    elif item == 'xis':
        return 6
    elif item == 'neves':
        return 7
    elif item == 'thgie':
        return 8
    else:
        
        print(f"{item} got here somehow?")
        return 9



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
CARDS = []
CARDS.append("-")
NUMBER_CARDS = {}

def part_one():
    sum = 0

    with open("./Day_Four/input.txt") as file:
        for line in file:
            winning_numbers = line.split("|")[0].split(":")[1].strip().split(" ")
            temp = []
            for num in winning_numbers:
                if not num == '':
                    temp.append(num)

            winning_numbers = temp
            print(winning_numbers)

            numbers = line.split("|")[1].strip().split(" ")
            matches = 0
            for number in numbers:
                if number in winning_numbers:
                    matches += 1

            print(matches)

            points = 0
            if matches > 0:
                points += 1
            if matches > 1:
                for i in range(matches - 1):
                    points = points * 2

            sum += points
    
    print(sum)

def part_two():
    sum = 0
    with open("./Day_Four/input.txt") as file:
        for line in file:
            CARDS.append(line.split(":")[1].strip())

    for i, card in enumerate(CARDS):
        if i == 0:
            continue
        NUMBER_CARDS[i] = 1 

    for key in NUMBER_CARDS.keys():
        winning_numbers = CARDS[key].split("|")[0].split(' ')
        temp = []
        for num in winning_numbers:
            if not num == '':
                temp.append(num)

        winning_numbers = temp

        numbers = CARDS[key].split("|")[1].strip().split(' ')
        matches = 0
        for number in numbers:
            if number in winning_numbers:
                matches += 1
        for i in range(NUMBER_CARDS[key]):
            for i in range(key+1, key+matches+1):
                NUMBER_CARDS[i] += 1

    
    for key in NUMBER_CARDS.keys():
        sum += NUMBER_CARDS[key]

    print(sum)


if __name__ == "__main__":
    part_two()
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






if __name__ == "__main__":
    part_one()
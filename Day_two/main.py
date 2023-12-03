def part_one():
    sum = 0

    with open("./Day_two/games.txt") as file:
        for line in file:
            game_id = int(line.split(':')[0].split(' ')[1].strip())
            sub_games = line.split(':')[1].strip().split(";")
            valid = True

            for sub_game in sub_games:
                red = 0
                green = 0
                blue = 0
                for pull in sub_game.split(','):
                    pull = pull.strip()
                    num = int(pull.split(' ')[0].strip())
                    color = pull.split(' ')[1].strip()
                    
                    if color == 'red':
                        red += num
                    elif color == 'green':
                        green += num
                    elif color == 'blue':
                        blue += num
                if red > 12 or green > 13 or blue > 14:
                    valid = False
                    break
                    
            if valid:
                sum += int(game_id)
    
    print(sum)


def part_two():
    sum = 0

    with open("./Day_two/games.txt") as file:
        for line in file:
            game_id = int(line.split(':')[0].split(' ')[1].strip())
            sub_games = line.split(':')[1].strip().split(";")
            valid = True
            min_red = 0
            min_green = 0
            min_blue = 0

            for sub_game in sub_games:
                red = 0
                green = 0
                blue = 0
                for pull in sub_game.split(','):
                    pull = pull.strip()
                    num = int(pull.split(' ')[0].strip())
                    color = pull.split(' ')[1].strip()
                    
                    if color == 'red':
                        red += num
                    elif color == 'green':
                        green += num
                    elif color == 'blue':
                        blue += num

                if red >= min_red:
                    min_red = red
                
                if green >= min_green:
                    min_green = green
                
                if blue >= min_blue:
                    min_blue = blue
            
            print(f"red: {min_red}, green: {min_green}, blue: {min_blue}")
            sum += min_red * min_green * min_blue

    print(sum)

if __name__ == "__main__":
    part_two()



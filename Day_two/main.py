if __name__ == "__main__":
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

            #pulls = [pull.strip() for pull in pulls]
            #print(pulls)
            # for pull in pulls:
            #     num = int(pull.split(' ')[0].strip())
            #     color = pull.split(' ')[1].strip()

            

            # print(game_id)
            # print(f"red: {red}, green: {green}, blue: {blue}")
            # if red <= 12 and green <= 13 and blue <= 14:
            #     print(".")
            #     sum += game_id

    
    print(sum)



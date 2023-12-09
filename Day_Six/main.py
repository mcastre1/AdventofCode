def part_one():
    times = []
    distances = []

    with open("./Day_Six/example1.txt") as file:
        for line in file:
            if "Time" in line:
                times = line.split(":")[1].strip().split(" ")
            if "Distance" in line:
                distances = line.split(":")[1].strip().split(" ")

    times = [time for time in times if not time == ""]
    distances = [distance for distance in distances if not distance == ""]

    suc_races = []    

    for i, val in enumerate(times):
        time = int(times[i])
        distance = int(distances[i])
        win_ways = 0

        print(f"Time: {times[i]}, Distance: {distances[i]}")

        for i in range(time + 1):
            total_time = time - i
            distance_moved = 0
            for j in range(total_time):
                distance_moved = distance_moved + i

            if distance_moved >= distance:
                win_ways += 1
                print(f"{distance_moved}, {i}, {total_time}")

        suc_races.append(win_ways)

    print(suc_races)



part_one()
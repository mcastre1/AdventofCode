


def part_one():
    seed_soil = {}
    soil_fertilizer = {}
    fertilizer_water = {}
    water_light = {}
    light_temperature = {}
    temperature_humidity = {}
    humidity_location = {}
    seeds = ""
    step = ""


    with open("./Day_Five/big.txt") as file:
        for line in file:
            if "seeds" in line:
                seeds = line
            elif "seed-to-soil" in line:
                step = "seed to soil"
            elif "soil-to-fertilizer" in line:
                step = "soil to fertilizer"
            elif "fertilizer-to-water" in line:
                step = "fertilizer to water"
            elif "water-to-light" in line:
                step = "water to light"
            elif "light-to-temperature" in line:
                step = "light to temperature"
            elif "temperature-to-humidity" in line:
                step = "temperature to humidity"
            elif "humidity-to-location" in line:
                step = "humidity to location"
            else:
                if not line.strip() == "":
                    if step == "seed to soil":
                        seed_soil.update(create_range_dict(line))
                    if step == "soil to fertilizer":
                        soil_fertilizer.update(create_range_dict(line))
                    if step == "fertilizer to water":
                        fertilizer_water.update(create_range_dict(line))
                    if step == "water to light":
                        water_light.update(create_range_dict(line))
                    if step == "light to temperature":
                        light_temperature.update(create_range_dict(line))
                    if step == "temperature to humidity":
                        temperature_humidity.update(create_range_dict(line))
                    if step == "humidity to location":
                        humidity_location.update(create_range_dict(line))

    for seed in seeds.split(":")[1].strip().split(" "):
        find_location(seed)

def create_range_dict(line):
    temp = {}
    data = line.strip().split(" ")
    source_range = int(data[1])
    destination_range = int(data[0])
    steps = int(data[2])
    count = 0
    for val in range(source_range, source_range + steps):
        temp[val] = destination_range + count
        count += 1
    return temp

def find_location(seed):
    seed_soil = {}
    soil_fertilizer = {}
    fertilizer_water = {}
    water_light = {}
    light_temperature = {}
    temperature_humidity = {}
    humidity_location = {}
    seed = int(seed)
    soil = seed_soil.get(seed, seed)
    fertilizer = soil_fertilizer.get(soil, soil)
    water = fertilizer_water.get(fertilizer, fertilizer)
    light = water_light.get(water, water)
    temperature = light_temperature.get(light, light)
    humidity = temperature_humidity.get(temperature, temperature)
    location = humidity_location.get(humidity, humidity)
    print(location)


def part_one_half():
    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []

    ss_map = []
    sf_map = []
    fw_map = []
    wl_map = []
    lt_map = []
    th_map = []
    hl_map = []

    maps = [[], ss_map, sf_map, fw_map, wl_map, lt_map, th_map, hl_map]

    seeds = ""

    count = 0
    with open("./Day_Five/big.txt") as file:
        for line in file:
            if "seeds" in line:
                seeds = line.split(":")[1]
            elif ":" in line:
                count+= 1
            else:
                line = line.strip()
                if line == '':
                    pass
                maps[count].append(line)

    for s in seeds.strip().split(" "):
        seed = int(s)
        for map in maps:
            if map == []:
                continue
            seed = convert_to(map, seed)
        print(seed)
        
    


def convert_to(map, seed):
    for ins in map:
        if ins == '':
            continue
        
        conversion = seed
        destination = int(ins.strip().split(' ')[0])
        source = int(ins.strip().split(' ')[1])
        _range = int(ins.strip().split(' ')[2])

        if seed in range(source, source + _range):
            diff = seed - source
            conversion = destination + diff
            return conversion
        
    return seed


if __name__ == "__main__":
    part_one_half()
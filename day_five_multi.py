from multiprocessing import Pool

def part_one_half():
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
    with open("./Day_Five/example1.txt") as file:
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

def part_two():
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

    seeds = seeds.strip().split(" ")
    lowest_location = 0
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seeds_start = int(seeds[i])
        seeds_range = int(seeds[i + 1])
        seeds_end = seeds_start + seeds_range 
        print(range(seeds_start, seeds_end))
        parts = 1000
        seed_ranges = list(split(range(seeds_start, seeds_end), parts))
        
        args = [(seed_ranges,maps)]

        with Pool(50) as p:
            p.starmap(print_ranges, args)
        # p = Pool()
        # p.map(print_ranges, seed_ranges)
    
def print_ranges(r, maps):
    lowest_location = 0
    for i in r:
        for s in i:
            seed = int(s)
            for map in maps:
                if map == []:
                    continue
                seed = convert_to(map, seed)
            
            if lowest_location == 0:
                lowest_location = seed
            else:
                lowest_location = seed if seed < lowest_location else lowest_location

        print(lowest_location) 

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    

if __name__ == "__main__":
    part_two()
def read_input_file():
    with open("5\input_5.1.txt", "r") as file:
        return file.readlines()

def process_seeds_line(line): 
    seedList = line.split(": ")[1].split(" ")   
    for attribute in seedList:
        attribute = int(attribute)
    return seedList

def process_map_lines(lines, map_start:str):
    mappings = []
    findStartIndex = 0
    index = 0
    while findStartIndex < len(lines):
        current_line = lines[findStartIndex].strip()
        if current_line.strip() == map_start:
            index = findStartIndex + 1
            break 
        findStartIndex += 1
    
        
    while index < len(lines):    
        line = lines[index]
        if not line.strip():
            break  # Stop processing when an empty line is encountered
        
        line = line.split()
        attributes = []
        for attribute in line:
            attribute = int(attribute)
            attributes.append(attribute)    
        mappings.append(attributes)
        index += 1
        

    return mappings

def find_lowest_location(seed: int, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map,
                         water_to_light_map, light_to_temperature_map, temperature_to_humidity_map,
                         humidity_to_location_map):
    # destination range start, source range start, range length.
    soil = find_corresponding_destination(seed_to_soil_map, seed)
    fertilizer = find_corresponding_destination(soil_to_fertilizer_map, soil)
    water = find_corresponding_destination(fertilizer_to_water_map, fertilizer)
    light = find_corresponding_destination(water_to_light_map, water)
    temperature = find_corresponding_destination(light_to_temperature_map, light)
    humidity = find_corresponding_destination(temperature_to_humidity_map, temperature)
    location = find_corresponding_destination(humidity_to_location_map, humidity)
        
    return location


def find_corresponding_destination(map, source):
    destination = "not assigned"
    for list in map:
        sourceRangeMin = int(list[1])
        sourceRangeMax = int(list[1])+int(list[2])
        destinationRangeMax = int(list[0])+int(list[2])
        source = int(source)
        if sourceRangeMin <= source and sourceRangeMax >= source:
            # print(str(source)+ " between "+ str(sourceRangeMin)+" and "+str(sourceRangeMax))
            destination = destinationRangeMax - (sourceRangeMax - int(source))
            # print(str(destination) + "=" + str(source))
            return destination
    if destination == "not assigned":
        destination = source    
        return destination
        

def main():
    lines = read_input_file()
    seed_list = process_seeds_line(lines[0])
    
    # Start index for each map
    seed_to_soil = "seed-to-soil map:"
    soil_to_fertilizer = "soil-to-fertilizer map:"
    fertilizer_to_water = "fertilizer-to-water map:"
    water_to_light = "water-to-light map:"
    light_to_temperature = "light-to-temperature map:"
    temperature_to_humidity = "temperature-to-humidity map:"
    humidity_to_location = "humidity-to-location map:"

    seed_to_soil_map = process_map_lines(lines, seed_to_soil)
    soil_to_fertilizer_map = process_map_lines(lines, soil_to_fertilizer)
    fertilizer_to_water_map = process_map_lines(lines, fertilizer_to_water)
    water_to_light_map = process_map_lines(lines, water_to_light)
    light_to_temperature_map = process_map_lines(lines, light_to_temperature)
    temperature_to_humidity_map = process_map_lines(lines, temperature_to_humidity)
    humidity_to_location_map = process_map_lines(lines, humidity_to_location)
        
    lowest_location = 999999999999  # Initialize with positive infinity

    for seed in seed_list:
        result = find_lowest_location(seed, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map,
                                      water_to_light_map, light_to_temperature_map, temperature_to_humidity_map,
                                      humidity_to_location_map)
        lowest_location = min(lowest_location, result)

    print("Lowest Location Number Corresponding to Seeds:", lowest_location)

main()
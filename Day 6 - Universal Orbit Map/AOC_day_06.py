import re


def count_orbits(map, layout=False):
    orbit_dict = {}
    orbit_counter = {'COM': 0}
    
    for orbit in map:
        objs = re.split('\)', orbit)
        orbit_dict[objs[1]] = objs[0]
    
    print(f'Object orbit dict: {orbit_dict}')
    
    def count_by_value(values):
        if len(orbit_dict) == 0:
            return
        temp_values = []
        for value in values:
            for key, val in orbit_dict.items():
                if val == value:
                    orbit_counter[key] = orbit_counter[val] + 1
                    temp_values.append(key)
        for key in temp_values:
            orbit_dict.pop(key)
        count_by_value(temp_values)

    def orbit_layout(obj):
        if obj[-1] == 'COM':
            return obj
        obj.append(orbit_dict[obj[-1]])
        return orbit_layout(obj=obj)
    
    if layout:
        layout_YOU = orbit_layout(['YOU'])
        print(f'YOU orbital layout: {layout_YOU}')
        layout_SAN = orbit_layout(['SAN'])
        print(f'SAN orbital layout: {layout_SAN}')
        
        for com in layout_YOU:
            if com in layout_SAN:
                transfers = layout_YOU.index(com) + layout_SAN.index(com) - 2
                print(f'Number of transfers: {transfers}')
                return transfers
    
    count_by_value(values=['COM'])
    
    print(f'Object orbit counts: {orbit_counter}')
    
    orbits_sum = sum([v for v in orbit_counter.values()])
    print(f'Total orbit count: {orbits_sum}')
    
    return orbits_sum


if __name__ == '__main__':
    
    with open('./input.txt', 'r') as f:
        inputs = f.readlines()
    map_data = [i.strip() for i in inputs]
    print(f'Initial map data: {map_data}')
    
    print('\n' + '--- Part One ---')
    count_orbits(map_data)                  # count: 247089
    
    print('\n' + '--- Part Two ---')
    count_orbits(map_data, layout=True)     # transfers: 442

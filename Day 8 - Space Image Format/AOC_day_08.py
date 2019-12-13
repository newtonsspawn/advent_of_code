def password_decoder(img_inp: list, img_size: list, final_decode=False):
    layers = []
    p_loc = 0
    while p_loc < len(img_inp):
        rows = []
        row_counter = 0
        while row_counter < img_size[1]:
            rows.append([p for p in img_inp[p_loc:p_loc + img_size[0]]])
            p_loc += img_size[0]
            row_counter += 1
        layers.append(rows)
    
    count_0 = img_size[0] * img_size[1]
    output = 0
    for l_loc in range(len(layers)):
        count_0_row, count_1_row, count_2_row = 0, 0, 0
        for row in layers[l_loc]:
            count_0_row += row.count('0')
            count_1_row += row.count('1')
            count_2_row += row.count('2')
        if count_0_row < count_0:
            output = count_1_row * count_2_row
            count_0 = count_0_row
    
    if final_decode:
        img_final = []
        for y in range(img_size[1]):
            for x in range(img_size[0]):
                grid_pos = []
                for layer in layers:
                    grid_pos.append(layer[y][x])
                for gp in grid_pos:
                    if gp in ['0', '1']:
                        img_final.append(gp)
                        break
        temp = []
        p_loc = 0
        while len(temp) < img_size[1]:
            temp.append(''.join(img_final[p_loc:p_loc+img_size[0]]) \
                        .replace('1', '#').replace('0', ' '))
            p_loc += img_size[0]
        img_final = temp
        
    
    if final_decode:
        print(f'Final image:')
        for row in img_final:
            print(row)
        return img_final
    else:
        print(f'# of `1`s x # of `2`s: {output}')
        return output


if __name__ == '__main__':
    inputs = '123456789012'
    image = list(inputs)
    password_decoder(image, [3, 2])                     # 1
    
    inputs = '0222112222120000'
    image = list(inputs)
    password_decoder(image, [2, 2], final_decode=True)  # 0110
    
    with open('./input.txt', 'r') as f:
        inputs = f.readline()
    image = list(inputs)
    password_decoder(image, [25, 6])                    # 2356
    password_decoder(image, [25, 6], final_decode=True) # PZEKB

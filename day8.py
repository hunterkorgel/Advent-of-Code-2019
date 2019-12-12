# Advent of Code 2019
# Day 8

# Store the photo as a list of values and split by layer
# Then simply count the zeroes to find the layer with the least

with open('day8.txt') as file_object:
    contents = str(file_object.read())

picture = [int(digit) for digit in contents]

def divide_chunks(given_list):
    for i in range(0, len(given_list)):
        yield given_list[i:i + 150]

layers = [picture[i * 150:(i+1) * 150] for i in range(0,100)]

smallest = 150
wanted_layer = 0
layer_index = 0
for layer in layers:
    sum = 0
    for pixel in layer:
        if pixel == 0:
            sum += 1
    if sum < smallest:
        smallest = sum
        wanted_layer = layer_index
    layer_index += 1

ones = layers[wanted_layer].count(1)
twos = layers[wanted_layer].count(2)

#print(ones*twos)

def render(image_data):
    image = [2] * 150
    for layer in image_data:
        index = 0
        for pixel in layer:
            if image[index] == 2:
                image[index] = pixel
            index += 1

    return image

rendered_image = ''.join([('▣' if pixel == 0 else '▢') for pixel in render(layers)])
rendered_image = '\n'.join(rendered_image[i:i+25] for i in range(0, len(rendered_image), 25))

print(rendered_image)
import png
import random
import utils

file_name = 'coloredImage'
test_png = []
png_size = 512
color = [random.randint(0, 255),
         random.randint(0, 255),
         random.randint(0, 255)]

for_loop_iterations = 0
for i in range(0, png_size):
    test_png.append([])  # creating rows

    # add RGB pixels for row (will be based on png_size)
    for e in range(0, png_size):

        # adds each RBG value to the row
        for y in range(0, len(color)):

            test_png[i].append(color[y])
            # for_loop_iterations++ as python doesn't support ++
            for_loop_iterations += 1


png.from_array(test_png, 'RGB').save(file_name + '.png')

utils.printFace("when I wasted my sunday morning doing this...")

print('%s.png of size %dx%d was create after %d iterations' %
      (file_name, png_size, png_size, for_loop_iterations))

print('\n')

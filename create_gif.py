import imageio.v3 as iio
import os 

folder_path = "images/"
extensions = ('.png', '.jpg', 'jpeg')

filenames = [os.path.join(folder_path, f) for f in sorted(os.listdir(folder_path)) if f.endswith(extensions)]
images = [iio.imread(filename) for filename in filenames]

iio.imwrite('auto.gif', images, duration = 500, loop = 0)    
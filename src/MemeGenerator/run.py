from .MemeGenerator import MemeGenerator

path = 'src/_data/photos/dog/xander_1.jpg'
path_out = 'src/MemeGenerator/new_pic.jpg'

text = 'hi'
author = 'peter'

x = MemeGenerator(path_out)
print(x.make_mem(path, text, author))

#TODO: delet it
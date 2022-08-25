from .MemeGenerator import MemeEngine

path = 'src/_data/photos/dog/xander_1.jpg'
path_out = 'src/MemeGenerator/new_pic.jpg'

text = 'hi'
author = 'peter'

x = MemeEngine(path_out)
print(x.make_meme(path, text, author))

#TODO: delet it
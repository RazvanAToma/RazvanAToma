
magicians = ["houdini", "howard", "blacky"]
great_magicians = []

def make_great(name):
    while magicians:
        name = magicians.pop()
        name = name.title() + " the Great!"
        great_magicians.append(name)

def show_magicians():
    for name in great_magicians:
        print(name)


make_great(magicians)
show_magicians()
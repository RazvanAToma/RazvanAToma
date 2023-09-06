import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print(f"Found it! {os.path.join(root, name)}")
            os.remove(os.path.join(root, name))
            break
            
find("Riot.txt", "C:/")
print("Aaaand it's gone")
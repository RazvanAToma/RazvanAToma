

start = 130306

x = 10000

file = open("salarprsnnummer.txt", "w")


while x < 99999:
    x += 1
    file.write(f"{start}{x}\n")

file.close()

print("done")
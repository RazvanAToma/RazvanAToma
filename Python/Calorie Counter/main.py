import ast

with open('dict.txt') as dict:
    database = dict.read

database = ast.literal_eval(database)

print(database)
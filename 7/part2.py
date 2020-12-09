import re
import time

with open("input.txt", "r") as file:
    rules = [line.replace("\n", "") for line in file.readlines()]

bags = {"no other": []}
regex = "[0-9] "

for rule in rules:
    split = rule.split(" bags contain ")
    bag, contents = split
    bags[bag] = []
    contents = contents.replace(".", "").split(", ")
    for i in range(len(contents)):
        if contents[i][-1] == "s":
            contents[i] = contents[i][:-1]
    for content in contents:
        if "no other" not in content:
            sp = content.split(" ")
            n = int(sp[0])
            bag_color = " ".join(sp[1:]).replace(" bag", "")
            bags[bag] += [bag_color for i in range(n)]


inner_bags = []


def count(color: str):
    contents = bags[color]
    for bag in contents:
        inner_bags.append(bag)
        count(bag)


count("shiny gold")

result = len(inner_bags)
print(result)

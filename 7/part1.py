# bags can be lists
# and then the shiny gold bag can be a 1
# then, for example:
# dull blue bags contain 2 dotted green bags, 1 dull brown bag, 3 striped tomato bags, 5 muted blue bags
# all we care about is that dull blue bags can carry:
#  dotted green bags
#  dull brown bags
#  striped tomato bags
#  muted blue bags.
# dull blue bag = ['dotted green', 'dull brown', 'striped tomato', 'muted blue']
# capacity = {
#   'dull blue': dull blue dag
# }
import re
import time

with open("input.txt", "r") as file:
    rules = [line.replace("\n", "") for line in file.readlines()]

bags = {"no other": []}

for rule in rules:
    split = rule.split(" bags contain ")
    bag, contents = split
    color = bag.replace(" bags", "")
    regex = "[0-9] "
    contents = re.split(regex, contents)
    contents = [x.replace(", ", "") for x in contents if len(x) > 0]
    contents = [x.replace(" bag", "").replace(".", "") for x in contents]
    contents = [x[:-1] if x[-1] == "s" else x for x in contents]
    bags[color] = contents

target = "shiny gold"
good_bags = set()


def search(color: str, tree: list):
    contents = bags[color]
    for bag in contents:
        if target in contents:
            for node in tree:
                good_bags.add(node)
        else:
            search(bag, tree=tree + [bag])


start = time.process_time()

for bag in bags:
    search(bag, tree=[bag])


print(len(good_bags))

end = time.process_time()

print(f"ran in {end - start} seconds")

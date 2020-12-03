from utils import count_trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

tree_counts = []

for slope in slopes:
    right = slope[0]
    down = slope[1]
    tree_count = count_trees(right=right, down=down)
    tree_counts.append(tree_count)
product = 1
for count in tree_counts:
    product *= count

result = product
print(result)

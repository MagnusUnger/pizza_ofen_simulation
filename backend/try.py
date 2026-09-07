
class Node():

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.right = None
        self.left = None
        self.up = None
        self.down = None


def build_hashmap(x_len, y_len):
    hashmap = {(x, y): Node(x, y) for x in range(x_len) for y in range(y_len)}
    return hashmap


def connect_hashmap(hashmap):
    for (x, y), node in hashmap.items():
        node.right = hashmap.get((x + 1, y))
        node.left = hashmap.get((x - 1, y))
        node.up = hashmap.get((x, y - 1))
        node.down = hashmap.get((x, y + 1))
    return hashmap


def gen_hashmap(x_len: int, y_len: int):
    hashmap = build_hashmap(x_len=x_len, y_len=y_len)
    hashmap = connect_hashmap(hashmap)
    return hashmap


def print_hashmap(hashmap, x_len, y_len):
    for y in range(y_len):
        row = []
        for x in range(x_len):
            node = hashmap.get((x, y))
            row.append(f"({node.x},{node.y})" if node is not None else ".")
        print("\t".join(row))


def main():
    x, y = 10, 10
    hashmap = gen_hashmap(x_len=x, y_len=y)
    print_hashmap(hashmap, x_len=x, y_len=y)


main()

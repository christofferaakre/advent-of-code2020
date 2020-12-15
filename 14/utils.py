import itertools


def get_binary_permutations(length: int):
    return [''.join(seq) for seq in itertools.product('01', repeat=length)]

def get_occurences(element, arr):
    indices = [i for i, x in enumerate(arr) if x == element]
    return indices

def mask_string(string, mask):
    masked = list(string)
    for i, bit in enumerate(mask):
        if bit != '0':
            masked[i] = bit

    return ''.join(masked)


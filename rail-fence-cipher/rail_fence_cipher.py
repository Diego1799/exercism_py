from itertools import cycle


def pattern(rails, width):
    n = 2 * (rails - 1)
    positions = (min(x, n - x) for x in cycle(range(n)))
    return sorted(zip(positions, range(width)))


def encode(message, rails):
    positions = pattern(rails, len(message))
    return ''.join(message[i] for _, i in positions)


def decode(encoded_message, rails):
    positions = pattern(rails, len(encoded_message))
    rectified = sorted(enumerate(positions), key=lambda t: t[1][1])
    return ''.join(encoded_message[i] for i, _ in rectified)

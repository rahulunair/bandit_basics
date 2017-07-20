from __future__ import print_function
import random

def draw(prb):
    """In the long run this method will
    return index with highest value in `prb`."""
    r = random.random()
    cumil = 0
    for i, v in enumerate(prb):
        cumil += v
        if cumil > r:
            return i
    return len(prb) - 1

if __name__ == '__main__':

    p = [random.random() for _ in range(4)] # random probability
    p_list = {0:0, 1:0, 2:0, 3:0}

    for i in range(1000):
        d = draw(p)
        p_list[d] += 1
    print("Prob distribution: {}".format(p))
    print(p_list)
    print("The value chosen most times is at index: {}".format(
        max(p_list,key=p_list.get
                                                                )))

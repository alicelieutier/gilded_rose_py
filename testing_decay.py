def backstage_passes_decay_rate_for_sell_in(sell_in):
    if sell_in >= 10:
        return 1
    if sell_in in range(5, 10):
        return 2
    if sell_in in range(0, 5):
        return 3

def test_a():
    for i in range(0,50):
        if (a(i) != backstage_passes_decay_rate_for_sell_in(i)):
            print("Failed for i = {}".format(i))
            return False
    return True


a = lambda x : 3 - min(10, x)/5

test_a()

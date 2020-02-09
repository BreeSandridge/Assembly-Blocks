import pickle


def load_data():
    try:
        with open("bin.dat") as f:
            x, y = pickle.load(f)
    except:
        x, y = [], []
    return x, y

def save_cache(root):
    cache = []
    node = root
    if node is not None:
        while node.below is not None:
            cache.append(node)
            node = node.below

        cache.append(node)



#   with open("bin.dat", "wb") as f:
#     pickle.dump(cache, f)



   """ x, y = load_data()
    print x, y
    x.append(random.randint(1, 10))
    y.append(random.randint(1, 10))
    save_data([x, y])"""
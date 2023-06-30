import pickle

rb = "rb"
wb = "wb"


def CreateFile(filename):
    pickle.dump([], open(filename, wb))
    pickle.dump([], open(f"contents of {filename}", wb))


def SaveToFile(filename, filecontent, contentname):
    file = pickle.load(open(filename, rb))
    filenames = pickle.load(open(f"contents of {filename}", rb))
    filenames.append(contentname)
    file.append(filecontent)
    pickle.dump(file, open(filename, wb))
    pickle.dump(filenames, open(f"content of {filename}", wb))


def LoadFromFile(filename, contentname):
    loadedfile = pickle.load(open(filename, "rb"))
    contentval = loadedfile[0].index(contentname)
    content = loadedfile[1][contentval]
    return content

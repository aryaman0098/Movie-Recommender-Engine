import ast
from nltk.stem.porter import PorterStemmer

def convertGenres(data):
    genresList = []
    for i in ast.literal_eval(data):
        genresList.append(i["name"])
    return genresList


def convertCast(data):
    castList = []
    count = 0
    for i in ast.literal_eval(data):
        castList.append(i["name"])
        count+=1
        if count == 3:
            break
    return castList


def getDirector(data):
    directorList = []
    for i in ast.literal_eval(data):
        if i["job"] == "Director":
            directorList.append(i["name"])
    return directorList


def stem(text):
    ps = PorterStemmer()
    stemList = []
    for i in text.split():
        stemList.append(ps.stem(i))
    return " ".join(stemList)


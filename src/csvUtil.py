import random
import string
import csv


def readAllKeys():
    with open("redirectionConfig.csv") as f:
        keys = [row.split(',')[0] for row in f]
        return keys

def keyGen(len=6):
    keyExistsList = []
    keyExistsList = readAllKeys()
    newKey = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len))
    while newKey in keyExistsList:
        newKey = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len))
    return newKey

def readCSVByline():
    with open('./redirectionConfig.csv', 'r', encoding="utf-8") as f:
        data = list(csv.reader(f))
        del(data[0])
        return data

def addRecord(url):
    key = keyGen()
    text = "\n" + key + "," + url 
    with open("./redirectionConfig.csv", "a+", encoding="utf-8") as f:
        f.write(text)

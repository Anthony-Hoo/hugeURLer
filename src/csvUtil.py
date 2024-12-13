import random
import string
import csv


def read_all_keys():
    with open("redirectionConfig.csv") as f:
        keys = [row.split(",")[0] for row in f]
        return keys


def key_gen(key_len=6):
    key_exists_list = read_all_keys()
    new_key = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(key_len)
    )
    while new_key in key_exists_list:
        new_key = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(key_len)
        )
    return new_key


def read_csv_byline():
    with open("./redirectionConfig.csv", "r", encoding="utf-8") as f:
        data = list(csv.reader(f))
        del data[0]
        return data


def add_record(url):
    key = key_gen()
    text = "\n" + key + "," + url
    with open("./redirectionConfig.csv", "a+", encoding="utf-8") as f:
        f.write(text)

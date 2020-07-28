import os
import json

from nltk import word_tokenize


def parse_file(file_):
    with open(file_) as f:
        data = json.load(f)

    rset = []
    c = 0
    for d in data:
        c += 1
        text = d["text"]
        id_ = d["id"]
        opinions = []
        for o in d["opinions"]:
            sentiment = o["sentiment"]
            aspect = o["aspect"]
            target = o["target_entity"]
            opinions.append((target, aspect, sentiment))
        rset.append((id_, text, opinions))
    print(c)
    return rset


def convert_input(data, all_aspects):
    rset = []
    for id_, text, opinions in data:
        for target_entity, aspect, sentiment in opinions:
            if aspect not in all_aspects:
                continue
            rset.append((id_, text, target_entity, aspect, sentiment))
        targets = ["LOCATION1"]
        if "LOCATION2" in text:
            targets.append("LOCATION2")
        for target in targets:
            aspects = set([a for t, a, _ in opinions if t == target])
            none_aspects = [a for a in all_aspects if a not in aspects]
            for aspect in none_aspects:
                rset.append((id_, text, target, aspect, "None"))
    return rset


def get_aspects(data):
    rset = {}
    for _, _, opinions in data:
        for _, aspect, _ in opinions:
            if aspect in rset.keys():
                rset[aspect] += 1
            else:
                rset[aspect] = 1
    return rset


def tokenize(data):
    rset = []
    for id_, text, target, aspect, sentiment in data:
        text = word_tokenize(text)
        rset.append((id_, text, target, aspect, sentiment))
    return rset


def parse_train_data():
    data = parse_file("./data/sentihood-train.json")

    all_aspects = get_aspects(data)
    data = convert_input(data, all_aspects)
    data = tokenize(data)
    return data


def parse_val_data():
    data = parse_file("./data/sentihood-dev.json")

    all_aspects = get_aspects(data)
    data = convert_input(data, all_aspects)
    data = tokenize(data)
    return data


def parse_test_data():
    data = parse_file("./data/sentihood-test.json")

    all_aspects = get_aspects(data)
    data = convert_input(data, all_aspects)
    data = tokenize(data)
    return data

import json
from collections import defaultdict, OrderedDict

total_acc = 0
total_aspects = 0
total_sentiments = 0

file_ = "trained-top4.jsonl"

with open(file_, "r") as f:
    jsonl_content = list(f)
    total = len(jsonl_content)
    for l in jsonl_content:
        j = json.loads(l)
        o = j["opinions"]
        p = j["model_pred"]
        if o == p:
            total_acc += 1
        for o in j["opinions"]:
            aspect = o["aspect"]
            sent = o["sentiment"]
            if aspect in [d["aspect"] for d in p]:
                total_aspects += 1
            if sent in [d["sentiment"] for d in p]:
                total_sentiments += 1
    print(total_acc / total)
    print(total_aspects / total)
    print(total_sentiments / total)


with open(file_, "r") as f:
    jsonl_content = list(f)
    total = len(jsonl_content)
    original_aspect = defaultdict()
    pred_aspect = defaultdict()
    for l in jsonl_content:
        j = json.loads(l)

        for o in j["opinions"]:
            if o["aspect"] in original_aspect:
                original_aspect[o["aspect"]] += 1
            else:
                original_aspect[o["aspect"]] = 1

        for p in j["model_pred"]:
            if p["aspect"] in pred_aspect:
                pred_aspect[p["aspect"]] += 1
            else:
                pred_aspect[p["aspect"]] = 1

    print(OrderedDict(sorted(original_aspect.items())))
    print(OrderedDict(sorted(pred_aspect.items())))

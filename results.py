import json
import pandas as pd


def parse_file(file_):
    with open(file_) as f:
        data = json.load(f)

    df = pd.read_csv("trained-top4.csv")

    rset = []
    for d in data:
        id_ = d["id"]
        model_pred = []

        res = df[df["id"] == id_]
        for i, row in res.iterrows():
            pred = {}
            pred["aspect"] = row["aspect"]
            pred["sentiment"] = row["sentiment"]
            pred["target_entity"] = row["target"]
            model_pred.append(pred)
        d["model_pred"] = model_pred
    return data


data = parse_file("./data/sentihood-test.json")

with open("trained-top4.jsonl", "w") as outfile:
    for d in data:
        json.dump(d, outfile)
        outfile.write("\n")

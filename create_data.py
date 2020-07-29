from visualise import parse_train_data, parse_val_data, parse_test_data

train_data = parse_train_data()
val_data = parse_val_data()
test_data = parse_test_data()

top_aspects = ["general", "price", "safety", "trans-location"]

with open("QA_pairs/train-QA.csv", "w") as f:
    for td in train_data:
        if td[3] in top_aspects:
            id_ = td[0]
            ans = " ".join(td[1])
            q = f"what do you think about the {td[3]} of {td[2]} ?"
            sentiment = td[4]
            f.write("\t".join([str(id_), q, ans, sentiment]))
            f.write("\n")

with open("QA_pairs/val-QA.csv", "w") as f:
    for td in val_data:
        if td[3] in top_aspects:
            id_ = td[0]
            ans = " ".join(td[1])
            q = f"what do you think about the {td[3]} of {td[2]} ?"
            sentiment = td[4]
            f.write("\t".join([str(id_), q, ans, sentiment]))
            f.write("\n")

with open("QA_pairs/test-QA.csv", "w") as f:
    for td in test_data:
        if td[3] in top_aspects:
            id_ = td[0]
            ans = " ".join(td[1])
            q = f"what do you think about the {td[3]} of {td[2]} ?"
            sentiment = td[4]
            f.write("\t".join([str(id_), q, ans, sentiment]))
            f.write("\n")

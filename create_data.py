from visualise import parse_train_data

train_data = parse_train_data()

print(train_data[0])
print(len(train_data))

with open("QA_pairs/train-QA.csv", "w") as f:
    for td in train_data:
        id_ = td[0]
        ans = " ".join(td[1])
        if td[3] == "general":
            q = f"what do you think about {td[2]} in general ?"
        else:
            q = f"what do you think about the {td[3]} of {td[2]} ?"
        sentiment = td[4]
        f.write("\t".join([str(id_), q, ans, sentiment]))
        f.write("\n")
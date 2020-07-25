import argparse

import pandas as pd
from tqdm import tqdm

import torch
import transformers as optimus


def load_train_data(input_dir):
    df = pd.read_csv(input_dir + "train-QA.csv", sep="\t")
    return df


def hyper_params():
    BATCH_SIZE = 32

    return BATCH_SIZE


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input_dir", default="./QA_pairs/", type=str, help="Input data directory",
    )

    parser.add_argument(
        "--output_dir", default="./artifacts/", type=str, help="Output data directory",
    )

    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_class, tokenizer_class, predtrain_weights = (
        optimus.BertForSequenceClassification,
        optimus.BertTokenizer,
        "bert-base-uncased",
    )
    train_data = load_train_data(args.input_dir)

    batch_size = hyper_params()
    num_training_steps = int(len(train_data) / batch_size)
    print(len(train_data))

    for row in tqdm(train_data):
        print(row)
        break


if __name__ == "__main__":
    main()

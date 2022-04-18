import os
import re

import pandas as pd

import config


def prepare_dataset(
    subset: str = "train",
    interim_dir: str = os.path.join("../", config.INTERIM_DIR),
) -> pd.DataFrame:
    """
    Extract all elements from text files to prepare a .csv file with the question, its corresponding answer,
    and the image it's referring to

    :param subset: Subset of all data to prepare
    :param interim_dir: Directory in which to save interim data
    :return: DataFrame for prepared dataset
    """
    qa_lines = open(
        os.path.join("../", config.RAW_DIR, f"{subset}_qa.txt")
    ).readlines()
    questions = qa_lines[::2]
    answers = qa_lines[1::2]

    data = []

    for q, a in zip(questions, answers):
        row = {}
        normalized_q = "".join(re.split(r"\b(in|on)\b", q)[:-2]).strip()
        row["question"] = normalized_q
        row["answer"] = a.strip()
        row["image"] = q.split()[-2]

        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(interim_dir, f"{subset}.csv"))
    return df

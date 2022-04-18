import os
import re

import pandas as pd

import src.config as config


def interim(
    subset: str = "train",
    raw_dir: str = config.RAW_DIR,
    interim_dir: str = config.INTERIM_DIR,
) -> pd.DataFrame:
    """
    Extract all elements from text files to prepare a .csv file with the question, its corresponding answer,
    and the image it's referring to

    :param subset: Subset of all data to prepare
    :param raw_dir: Directory from which to extract raw data
    :param interim_dir: Directory in which to save interim data
    :return: DataFrame for prepared dataset
    """
    if not os.path.isdir(interim_dir):
        os.system("mkdir -p " + config.INTERIM_DIR)

    qa_lines = open(os.path.join(raw_dir, f"{subset}_qa.txt")).readlines()
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

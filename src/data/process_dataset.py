from typing import Dict

import pandas as pd
import torch.utils.data as data


class QADataset(data.Dataset):
    def __init__(self, data_fp: str):
        self.data = pd.read_csv(data_fp)
        self.data_len = len(self.data)

    def __getitem__(self, item: int) -> Dict:
        assert (
            0 <= item < self.data_len
        ), "Specified index is out of range for this dataset"
        row = self.data.iloc[item]
        return {
            "Question": row["question"],
            "Answer": row["answer"],
            "Image": row["image"],
        }

    def __len__(self) -> int:
        return self.data_len

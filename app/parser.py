import pandas as pd
import numpy as np


class Parser:

    def __init__(self, csv, chunk_size):
        self.csv = csv
        self.chunk_size = chunk_size

    def get_stats(self):
        return pd.read_csv(csv, chunksize=self.chunk_size)

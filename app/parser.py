import pandas as pd
import numpy as np
from process import Process


class Parser:
    def __init__(self, csv, chunk_size):
        self.csv = csv
        self.chunk_size = chunk_size

    def get_stats(self):
        chunks = pd.read_csv(csv, chunksize=self.chunk_size)
        for chunk in chunks:
            process = Process(chunk)
            return process.get_result()

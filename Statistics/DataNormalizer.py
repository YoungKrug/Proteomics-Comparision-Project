import pandas
import math
import numpy as np
class DataNormalizer:
    def __init__(self, data):
        self.data = data
    def ReadTSV(self, file_name):
        columns = ["iBAQ"] #Calculating Z Scores
        pandas.set_option('display.max_columns', 40)
        df = pandas.read_csv(self.data, delimiter="\t")
        df = df[["Protein IDs", "Majority protein IDs", "iBAQ", "Peptide sequences", "Fasta headers"]]
        df["iBAQ_log"] = df["iBAQ"].map(self.LogNormalization)
        self.mean = df["iBAQ_log"].mean()
        self.std = df["iBAQ_log"].std()
        df["iBAQ_log"] = df["iBAQ_log"].map(self.CalculateZScoreNormalization)
        df.to_csv(file_name, sep='\t')
        print(df)

    def LogNormalization(self, val):
        try:
            return math.log(val, 2)
        except:
            return 0
    def CalculateZScoreNormalization(self, val):
        temp_val = val
        temp_val -= self.mean
        return temp_val / self.std


file_path = input("Where is your file located?\n")
file_name = input("What would you like your file to be named?\n")
dr = DataNormalizer(file_path)
dr.ReadTSV(file_name=f"{file_name}.txt")



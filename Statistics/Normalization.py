import math
from DataReader import DataReader
import os
class Normalization:
    def __init__(self, column_values):
        self.column_values = column_values
    def LogNormalization(self):
        values = self.column_values
        new_values = []
        for val in values:
            new_values.append(math.log(val), 2)
        return new_values


data = "C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/proteinGroups_Salmonella.tsv"
dr = DataReader(data)
dr.ReadTSV()
import pandas
class DataReader: # beta actin
    def __init__(self, data):
        self.data = data
    def ReadTSV(self):
        columns = ["iBAQ"]
        pandas.set_option('display.max_columns', 40)
        df = pandas.read_csv(self.data, delimiter="\t")
        #df = pandas.DataFrame(self.data, names=columns, sep="\t", header=None)
        df = df[["iBAQ", "Majority protein IDs"]]
        print(df)

        # print(df)





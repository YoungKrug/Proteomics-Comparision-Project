import pandas

class FindDups:
    def __init__(self, data):
        self.data = data
    def ReadTSV(self, file_name):
        pandas.set_option('display.max_columns', 40)
        df = pandas.read_csv(self.data, delimiter="\t")
        df.to_csv(file_name, sep='\t')
        print(df)

df = FindDups()
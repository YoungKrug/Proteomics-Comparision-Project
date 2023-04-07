from pymsfilereader import MSFileReader
import subprocess,os
class RawToMZMLConverter:
    rawfile = []
    def __init__(self, rawfile):
        if isinstance(rawfile, list):
            self.rawfile = self.rawfile + rawfile
        else:
            self.rawfile.append(rawfile)
    def ConvertToMZML(self, output_file, filename):
        my_env = os.environ.copy()
        path = input("Enter the path to your proteowizard install...")
        while(not os.path.exists(path)):
            path = input("Path does not exist, please re-enter it")
        my_env["PATH"] = f"{path};"
        index = 0
        for files in self.rawfile:
            filename = filename.split(" ", 1)[0]
            filename = f"{filename}_{index}"
            commandline = f"MSConvert {files} -o{output_file} --outfile {filename}"
            print(f"Running command...\n{commandline}")
            subprocess.run(commandline, shell=True, stdout=True, stderr=True, env=my_env)
            index = index + 1
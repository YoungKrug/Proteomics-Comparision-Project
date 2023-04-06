from pymsfilereader import MSFileReader
import subprocess,os
class RawConverter:
    rawfile = []
    def __init__(self, rawfile):
        if isinstance(rawfile, list):
            self.rawfile = self.rawfile + rawfile
        else:
            self.rawfile.append(rawfile)
    def ConvertToMZML(self, output_file, filename):
        my_env = os.environ.copy()
        my_env["PATH"] = "C:/Users/gregj/AppData/Local/Apps/ProteoWizard 3.0.23072.5333f49 64-bit;"
        index = 0
        for files in self.rawfile:
            filename = f"{filename}_{index}"
            commandline = f"MSConvert {files} -o{output_file} --outfile {filename}"
            print(f"Running command...\n{commandline}")
            subprocess.run(commandline, shell=True, stdout=True, stderr=True, env=my_env)
            index = index + 1
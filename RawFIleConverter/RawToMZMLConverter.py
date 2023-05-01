import ursgal
import glob
import os
import shutil
class RawToMZMLConverter:
    rawfile = []
    mzml_path = "PrideResources/ConvertedData"
    def __init__(self):
        pass
    def ConvertToMZML(self, raw_folder, bacteria_name):
        R = ursgal.UController()
        # Check if single file or folder.
        # Collect raw files if folder is given
        # Convert raw file(s)
        new_directory = bacteria_name[:5]
        new_path = os.path.join(self.mzml_path, new_directory)
        if(not os.path.exists(new_path)):
            os.mkdir(new_path)
        for raw_file in glob.glob(os.path.join(raw_folder, "*.raw")):
            self.rawfile.append(raw_file)
        input_file_list = self.rawfile
        for raw_file in input_file_list:
            mzml_file = R.convert(
                input_file=raw_file,
                engine="thermo_raw_file_parser_1_1_2"
            )
            newPath = f"{new_path}/{os.path.split(mzml_file)[1]}"
            print(f"New path: {newPath} ")
            if(not os.path.exists(newPath)):
                print("Path does not exist, creating file...")
                shutil.copyfile(mzml_file, newPath)
            else:
                print("File already exist...")
            current_folder = os.path.dirname(mzml_file)
            print(current_folder)
        return new_path


print(os.path.abspath("PrideResources/ConvertedData"))
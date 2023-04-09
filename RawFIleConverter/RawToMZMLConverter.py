import ursgal
import glob
import os
class RawToMZMLConverter:
    rawfile = []
    def __init__(self, rawfile):
        if isinstance(rawfile, list):
            self.rawfile = self.rawfile + rawfile
        else:
            self.rawfile.append(rawfile)
    def ConvertToMZML(self, output_file, filename):
        R = ursgal.UController()

        # Check if single file or folder.
        # Collect raw files if folder is given
        input_file_list = self.rawfile
        # Convert raw file(s)
        index = 0
        current_folder = ""
        for raw_file in input_file_list:
            mzml_file = R.convert(
                input_file=raw_file,
                engine="thermo_raw_file_parser_1_1_2",
                output_file_name=f"{filename}_{index}"
            )
            index += 1
            current_folder = os.path.dirname(mzml_file)
        return current_folder

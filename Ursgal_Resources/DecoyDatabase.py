import ursgal
import os

class DecoyDB:
    def __init__(self, inputFile):
        self.inputFile = inputFile
    def CreateFile(self, outputfileName):
        """
           Simple example script how to generate a target decoy database.

           Note:
               By default a 'shuffled peptide preserving cleavage sites' database is
               generated. For this script a 'reverse protein' database is generated.

           usage:

               ./target_decoy_generation_example.py

           """
        params = {
            "enzyme": "trypsin",
            "decoy_generation_mode": "reverse_protein",
        }
        uc = ursgal.UController(params=params)

        new_target_decoy_db_name = uc.execute_misc_engine(
            input_file=self.inputFile,
            engine="generate_target_decoy_1_0_0",
            output_file_name=f"{outputfileName}.fasta",
        )
        print("Generated target decoy database: {0}".format(new_target_decoy_db_name))
        return new_target_decoy_db_name
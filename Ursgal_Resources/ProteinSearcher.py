#!/usr/bin/env python3
# encoding: utf-8
import ursgal
import sys
import glob
import os

class Searcher:
    def __init__(self):
        self.outputfile = ""
    def Search(self, folder, target_decoy_database, profile="QExactive+"):
        """
           An example test script to search all mzML files which are present in the
           specified folder. The search is currently performed on 4 search engines
           and 2 validation engines.
           The machine profile has to be specified as well as the target-decoy
           database.
           usage:
               ./do_it_all_folder_wide.py <mzML_folder> <profile> <target_decoy_database>
           Current profiles:
               * 'QExactive+'
               * 'LTQ XL low res'
               * 'LTQ XL high res'
           """
        # define folder with mzML_files as sys.argv[1]
        mzML_files = []
        for mzml in glob.glob(os.path.join("{0}".format(folder), "*.mzML")):
            mzML_files.append(mzml)
        print(mzML_files)
        mass_spectrometer = profile

        # We specify all search engines and validation engines that we want to use in a list
        # (version numbers might differ on windows or mac):
        search_engines = [
            # "omssa",
            # "xtandem_vengeance",
            #"msgfplus_v2019_07_03",
            # 'msamanda_1_0_0_6300',
            "myrimatch_2_2_140"
        ]

        validation_engines = [
            "percolator_3_4_0",
            "percolator_3_4_0",
            "percolator_3_4_0"
        ]

        # Modifications that should be included in the search
        all_mods = [
            "C,fix,any,Carbamidomethyl",
            "M,opt,any,Oxidation",
            # 'N,opt,any,Deamidated',
            # 'Q,opt,any,Deamidated',
            # 'E,opt,any,Methyl',
            # 'K,opt,any,Methyl',
            # 'R,opt,any,Methyl',
            "*,opt,Prot-N-term,Acetyl",
            # 'S,opt,any,Phospho',
            # 'T,opt,any,Phospho',
            # 'N,opt,any,HexNAc'
        ]

        # Initializing the Ursgal UController class with
        # our specified modifications and mass spectrometer
        params = {
            "database": target_decoy_database,
            "modifications": all_mods,
            "csv_filter_rules": [
                ["Is decoy", "equals", "false"],
                ["PEP", "lte", 0.01],
            ],
        }

        uc = ursgal.UController(profile=mass_spectrometer, params=params)

        # complete workflow:
        # every spectrum file is searched with every search engine,
        # results are validated (for each engine seperately),
        # validated results are merged and filtered for targets and PEP <= 0.01.
        # In the end, all filtered results from all spectrum files are merged
        merged_csv = ""
        for validation_engine in validation_engines:
            result_files = []
            for spec_file in mzML_files:
                validated_results = []
                for search_engine in search_engines:
                    unified_search_results = uc.search(
                        input_file=spec_file,
                        engine=search_engine,
                    )
                    validated_csv = uc.validate(
                        input_file=unified_search_results,
                        engine=validation_engine,
                    )
                    validated_results.append(validated_csv)

                validated_results_from_all_engines = uc.execute_misc_engine(
                    input_file=validated_results,
                    engine="merge_csvs_1_0_0",
                )
                filtered_validated_results = uc.execute_misc_engine(
                    input_file=validated_results_from_all_engines,
                    engine="filter_csv_1_0_0",
                )
                result_files.append(filtered_validated_results)

            results_all_files = uc.execute_misc_engine(
                input_file=result_files,
                engine="merge_csvs_1_0_0",
                output_file_name="Protein_Searcher_"
            )
            merged_csv = results_all_files
        return merged_csv
    def CountPeptides(self, csvFile):
        file = open(csvFile)
        num = 0
        for line in file:
            num = num + 1
        print(f"number of peptides: {num}")
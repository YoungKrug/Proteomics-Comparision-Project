#!/usr/bin/env python
import sys
import ursgal
import os
import glob

class Quantification:
    CreatedExperimentNumber = 1
    def CreateExperimentSetup(self, filename, condition="Exponential", biorep=1, fraction=1, techrep=1):

        return {
                "FileName": filename,
                "Condition": condition,
                "Biorep": biorep,
                "Fraction": fraction,
                "Techrep": techrep,
                }

    def AbsoluteQuantification(self, mzml_folder, merged_result):
        params = {
            "isotopic_distribution_tolerance": 5,
            "normalize_intensities": True,
            "integrate_peak_areas": False,
            "only_precursor_charge": False,
            "match_between_runs": True,
            "match_between_runs_RT_window": 0.5,
            "require_msms_id": False,
            "bayesian_fold_change": True,
            "bayesian_fold_change_control_condition": "Exponential",
            "fold_change_cutoff": 0.1,
            "markov_chain_iterations": 3000,
            "markov_chain_burn_in_iterations": 1000,
            "use_shared_peptides": True,
            "random_seed": 200,
        }
        uc = ursgal.UController(
            verbose=True,
            params=params,
            profile="QExactive+",
        )
        mzml_files = []
        filenames = []
        for mzml in glob.glob(os.path.join(mzml_folder, "*.mzML")):
            mzml_files.append(mzml)
            filenames.append(os.path.basename(mzml).split(".")[0])
        experiment_setup = {}
        conditions = ["Exponential", "Sample", "Anything"]
        counter = 0
        for files in filenames:
            experiment = self.CreateExperimentSetup(filename=files, condition=conditions[counter])
            # experiment_setup.__setitem__(f"{self.CreatedExperimentNumber}", experiment)
            experiment_setup = {**experiment_setup, **{f"{self.CreatedExperimentNumber}": {**experiment}}}
            self.CreatedExperimentNumber += 1
            counter += 1

        # If you want to define your own experimental setup, you must uncomment this and comment the above block
        # experiment_setup = {
        #     "1": {
        #         "FileName": "Salmonella_enterica_serotype_typhi_0",
        #         "Condition": "Exponential",
        #         "Biorep": 1,
        #         "Fraction": 1,
        #         "Techrep": 1,
        #     },
        #     "2": {
        #         "FileName": "Salmonella_enterica_serotype_typhi_1",
        #         "Condition": "Sample",
        #         "Biorep": 1,
        #         "Fraction": 1,
        #         "Techrep": 1,
        #     },
        #     "3": {
        #         "FileName": "Salmonella_enterica_serotype_typhi_2",
        #         "Condition": "Anything",
        #         "Biorep": 1,
        #         "Fraction": 1,
        #         "Techrep": 1,
        #     }
        # }

        uc.params["experiment_setup"] = experiment_setup
        uc.params["quantification_evidences"] = merged_result


        quantified_peaks = uc.quantify(
            input_file=mzml_files, multi=True, engine="flash_lfq_1_1_1"
        )
        return quantified_peaks


dir = 'PrideResources/ConvertedData/ExperimentalDesign.tsv'
print(os.path.basename(dir).split(".")[0])
#!/usr/bin/env python
import sys
import ursgal
import os
import glob

class Quantification:
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

        experiment_setup = {
            "1": {
                "FileName": "WT_L-1C",
                "Condition": "Exponential",
                "Biorep": 1,
                "Fraction": 1,
                "Techrep": 1,
            },
            "2": {
                "FileName": "WT_L-1M",
                "Condition": "Exponential",
                "Biorep": 1,
                "Fraction": 2,
                "Techrep": 1,
            },
            "3": {
                "FileName": "WT_L-2C",
                "Condition": "Exponential",
                "Biorep": 2,
                "Fraction": 1,
                "Techrep": 1,
            },
            "4": {
                "FileName": "WT_L-2M",
                "Condition": "Exponential",
                "Biorep": 2,
                "Fraction": 2,
                "Techrep": 1,
            },
            "5": {
                "FileName": "WT_L-3C",
                "Condition": "Exponential",
                "Biorep": 3,
                "Fraction": 1,
                "Techrep": 1,
            },
            "6": {
                "FileName": "WT_L-3M",
                "Condition": "Exponential",
                "Biorep": 3,
                "Fraction": 2,
                "Techrep": 1,
            },
            "7": {
                "FileName": "WT_S-1C",
                "Condition": "Stationary",
                "Biorep": 1,
                "Fraction": 1,
                "Techrep": 1,
            },
            "8": {
                "FileName": "WT_S-1M",
                "Condition": "Stationary",
                "Biorep": 1,
                "Fraction": 2,
                "Techrep": 1,
            },
            "9": {
                "FileName": "WT_S-2C",
                "Condition": "Stationary",
                "Biorep": 2,
                "Fraction": 1,
                "Techrep": 1,
            },
            "10": {
                "FileName": "WT_S-2M",
                "Condition": "Stationary",
                "Biorep": 2,
                "Fraction": 2,
                "Techrep": 1,
            },
            "11": {
                "FileName": "WT_S-3C",
                "Condition": "Stationary",
                "Biorep": 3,
                "Fraction": 1,
                "Techrep": 1,
            },
            "12": {
                "FileName": "WT_S-3M",
                "Condition": "Stationary",
                "Biorep": 3,
                "Fraction": 2,
                "Techrep": 1,
            },
            "13": {
                "FileName": "WT_EXP1_botttom20",
                "Condition": "Exponential",
                "Biorep": 4,
                "Fraction": 1,
                "Techrep": 1,
            },
            "14": {
                "FileName": "WT_EXP1_top20",
                "Condition": "Exponential",
                "Biorep": 4,
                "Fraction": 2,
                "Techrep": 1,
            },
            "15": {
                "FileName": "WT_EXP2_botttom20",
                "Condition": "Exponential",
                "Biorep": 5,
                "Fraction": 1,
                "Techrep": 1,
            },
            "16": {
                "FileName": "WT_EXP2_top20",
                "Condition": "Exponential",
                "Biorep": 5,
                "Fraction": 2,
                "Techrep": 1,
            },
            "17": {
                "FileName": "WT_EXP3_botttom20",
                "Condition": "Exponential",
                "Biorep": 6,
                "Fraction": 1,
                "Techrep": 1,
            },
            "18": {
                "FileName": "WT_EXP3_top20",
                "Condition": "Exponential",
                "Biorep": 6,
                "Fraction": 2,
                "Techrep": 1,
            },
            "19": {
                "FileName": "WT_ST1_botttom20",
                "Condition": "Stationary",
                "Biorep": 4,
                "Fraction": 1,
                "Techrep": 1,
            },
            "20": {
                "FileName": "WT_ST1_top20",
                "Condition": "Stationary",
                "Biorep": 4,
                "Fraction": 2,
                "Techrep": 1,
            },
            "21": {
                "FileName": "WT_ST2_botttom20",
                "Condition": "Stationary",
                "Biorep": 5,
                "Fraction": 1,
                "Techrep": 1,
            },
            "22": {
                "FileName": "WT_ST2_top20",
                "Condition": "Stationary",
                "Biorep": 5,
                "Fraction": 2,
                "Techrep": 1,
            },
            "23": {
                "FileName": "WT_ST3_botttom20",
                "Condition": "Stationary",
                "Biorep": 6,
                "Fraction": 1,
                "Techrep": 1,
            },
            "24": {
                "FileName": "WT_ST3_top20",
                "Condition": "Stationary",
                "Biorep": 6,
                "Fraction": 2,
                "Techrep": 1,
            },
        }

        uc.params["experiment_setup"] = experiment_setup
        uc.params["quantification_evidences"] = merged_result

        mzml_files = []
        for mzml in glob.glob(os.path.join(mzml_folder, "*.mzML")):
            mzml_files.append(mzml)

        quantified_peaks = uc.quantify(
            input_file=mzml_files, multi=True, engine="flash_lfq_1_1_1"
        )
        return quantified_peaks
from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase
from Ursgal_Resources.DecoyDatabase import DecoyDB
from Ursgal_Resources.ProteinSearcher import Searcher
from Ursgal_Resources.CSVSanitize import SanitizeCSV
from Ursgal_Resources.QuantifyData import Quantification
class PipelineBuilder:
    output_dir = ""
    pride_search_bacteria = ""
    fasta_dir = ""
    decoyDB_name = ""
    def __init__(self):
        pass
    def RunPipeline(self):
        # Step 1, Search The Pride database
        print("Searching Pride Database...")
        prideDB = PrideDatabase(self.pride_search_bacteria,
                                output_folder=self.output_dir,
                                amount_to_download=1)
        # Step 2, Download the raw files from the pride database
        print("Downloading Pride Files...")
        resourceDownloader = ResourceDownloader(prideDB)
        resourceDownloader.DownloadResources()
        # Step 3, Convert .raw files to MZML files
        print("Converting Raw Files...")
        mzmlFiles_Dir = resourceDownloader.ConvertToDataReadableFiles()
        # Step 4, Generate a Decoy DB
        print("Generating Decoy Database...")
        bacteria_name = self.pride_search_bacteria.replace(" ", "_")
        decoy_db = DecoyDB(self.fasta_dir)
        # Step 5, Conduct a protein search
        print("Conducting Protein Search...")
        protein_search = Searcher()
        protein_search_mzml = protein_search.Search(folder=mzmlFiles_Dir,
                                                    target_decoy_database=decoy_db.CreateFile(
                                                        outputfileName=bacteria_name + "_DecoyDB"))
        # Step 6, Sanitize Data
        print("Sanitizing Data in csv...")
        SanitizeCSV().Sanitize(protein_search_mzml)
        # Step 7, Quantify Data
        print("Quantification of data...")
        Quantification.AbsoluteQuantification(mzml_folder=mzmlFiles_Dir, merged_result=protein_search_mzml)
    def Build(self):
        self.RunPipeline()
    def OutputDirectoryAt(self):
        self.output_dir = input("Where would you like your output directory for mzml files to be?\n")
        return PipelineBuilder
    def WithFastaFile(self):
        self.fasta_dir = input("Please give me the path to your reference fasta file")
        return PipelineBuilder
    def AsBacteria(self):
        self.pride_search_bacteria = input("what bacterial would you like to analyze?")
        return PipelineBuilder

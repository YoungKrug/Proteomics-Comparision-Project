from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase
from Ursgal_Resources.DecoyDatabase import DecoyDB
from Ursgal_Resources.ProteinSearcher import Searcher
from Ursgal_Resources.CSVSanitize import SanitizeCSV
from Ursgal_Resources.QuantifyData import Quantification
import os
# The main pipeline builder interface, uses all the ursgal engine pieces to construct a flow
class PipelineBuilder:
    output_dir = ""
    pride_search_bacteria = ""
    fasta_dir = ""
    decoyDB_name = ""
    def __init__(self):
        pass
    def RunPipeline(self): # The function to start the pipeline
        # Step 1, Search The Pride database
        print("Searching Pride Database...")
        prideDB = PrideDatabase(self.pride_search_bacteria,
                                output_folder=self.output_dir,
                                amount_to_download=1,
                                filterList=self.pride_accession_list)
        # Step 2, Download the raw files from the pride database
        print("Downloading Pride Files...")
        resourceDownloader = ResourceDownloader(prideDB)
        resourceDownloader.DownloadResources()
        # Step 3, Convert .raw files to MZML files
        print("Converting Raw Files...")
        mzmlFiles_Dir = resourceDownloader.ConvertToDataReadableFiles()
        print(mzmlFiles_Dir + "\n")
        mzmlFiles_Dir = os.path.relpath(mzmlFiles_Dir)
        print(mzmlFiles_Dir + "\n")
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
        sanitize = SanitizeCSV()
        s_protein_search_mzml = sanitize.Sanitize(infile=protein_search_mzml)
        # Step 7, Quantify Data
        print("Quantification of data...")
        absQuant = Quantification()
        absQuant.AbsoluteQuantification(mzml_folder=mzmlFiles_Dir, merged_result=s_protein_search_mzml)
        print("Done!!!")
    def Build(self): # Call this function after you declare you variables in order to run the pipeline
        self.RunPipeline()
    def OutputDirectoryAt(self, directory=""): # This is where you input your output directory, it returns self so
        # you can call the other functions to continue the chain.
        if (directory != ""):
            self.output_dir = directory
        else:
            self.output_dir = input("Where would you like your output directory for mzml files to be?\n")
        return self
    def WithFastaFile(self, directory=""): # Same thing as above, you can declare where your fastA file is
        if (directory != ""):
            self.fasta_dir = directory
        else:
            self.fasta_dir = input("Please give me the path to your reference fasta file")
        return self
    def AsBacteria(self, bacteria=""): # Like above, but instead for your bacteria
        if(bacteria != ""):
            self.pride_search_bacteria = bacteria
        else:
            self.pride_search_bacteria = input("what bacterial would you like to analyze?")
        return self
    def WithPrideNumbers(self, pride_accession_list = []): # This function allows you to create a list for pride IDs
        # you want to filter for in the pride archive
        self.pride_accession_list = pride_accession_list
        return self
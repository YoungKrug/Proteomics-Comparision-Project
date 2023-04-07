from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase

outputDir = input("Where would you like your output directory for mzml files to be?\n")
pride_search = input("what bacterial would you like to analyze?")
prideDB = PrideDatabase(pride_search,
                   output_folder=outputDir,
                   amount_to_download=1)
resourceDownloader = ResourceDownloader(prideDB)
resourceDownloader.DownloadResources()
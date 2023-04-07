from RawFIleConverter.RawToMZMLConverter import RawToMZMLConverter
from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase

# Change this location, (For some reason it wouldn't work via relative location?? Lmk on your end)
fasta = input("Please give me the path to your reference fasta file")
outputDir = "C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/ConvertedData"
prideDB = PrideDatabase("Salmonella enterica serotype typhi",
                   output_folder="C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/RawFiles",
                   amount_to_download=1)
resourceDownloader = ResourceDownloader(prideDB)
resourceDownloader.DownloadResources()
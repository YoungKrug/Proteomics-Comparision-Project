from RawFIleConverter.RawConverter import RawConverter
from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase

#Change this location, (For some reason it wouldnt work via relative location?? Lmk on your end)
rawfileDir = "C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/RawFiles/89be958c243a1ba43d34a0b4d5bec4dbff8f416686fb6e8a58d4a2f8f6ec7ec3-Serum_3.raw"
outputDir = "C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/ConvertedData"
prideDB = PrideDatabase("meningitis",
                   output_folder="PrideResources/RawFiles",
                   amount_to_download=1)
resourceDownloader = ResourceDownloader(prideDB)
# resourceDownloader.DownloadResources() #uncomment to download files
rawfile = RawConverter(rawfileDir)
rawfile.ConvertToTSV(outfileDirectory=outputDir, filename="Serum_3.11")
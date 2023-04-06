from RawFIleConverter.RawConverter import RawConverter
from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase

#Change this location, (For some reason it wouldnt work via relative location?? Lmk on your end)
rawfileDir = "C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/RawFiles/86dc7dda90091317c1e43baa97b36d9e187cca9f51a8fab47dfce2adf6e91bc6-20170112_L_MaD_ColC4_Ecoli20161108-24_01.raw"
outputDir = "C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/ConvertedData"
prideDB = PrideDatabase("Salmonella enterica serotype typhi",
                   output_folder="C:/Users/gregj/Documents/ProteomicsGroupProj/Proteomics-Comparision-Project/PrideResources/RawFiles",
                   amount_to_download=1)
resourceDownloader = ResourceDownloader(prideDB)
resourceDownloader.DownloadResources() #uncomment to download files
#rawfile = RawConverter(rawfileDir)
#rawfile.ConvertToMZML(output_file=outputDir, filename="ConvertedFile")
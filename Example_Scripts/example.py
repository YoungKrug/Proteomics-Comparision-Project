from RawFIleConverter.RawToMZMLConverter import RawToMZMLConverter
from Resources.ResourceDownloader import ResourceDownloader
from Resources.Databases.PrideDatabase import PrideDatabase
from Ursgal_Resources.ProteinSearcher import Searcher

search = Searcher()
search.Search(folder="D:/ProteomeClassAssignments/Proteomics-Comparision-Project/PrideResources/ConvertedData",
              target_decoy_database="PrideResources/Fasta/Salmonella_enterica_serotype_typhi_DecoyDB.fasta")
# Change this location, (For some reason it wouldn't work via relative location?? Lmk on your end)

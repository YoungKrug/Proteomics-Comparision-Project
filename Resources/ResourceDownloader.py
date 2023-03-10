from pridepy import Project
from files.files import  Files
class ResourceDownloader: # Will be the downloader method for the pride datasets
    def __init__(self):
        self.accessionData = []
    def SearchDatabase(self):
        project = Project()
        # Staphylococcus aureus is our prokaryote
        results = project.search_by_keywords_and_filters(
            str(self.search),  # search for a specific species
            "filter",  # you can define a filter here, but you don't need to
            1000,  # maximum number of results
            0,  # pages - no need to change this
            10,  # date gap - no need to change this
            "DESC",  # order in which results are sorted
            "submission_date",  # sorting criterium
        )
        for val in results["_embedded"]["compactprojects"]:
            self.accessionData.append(val["accession"])
            print(project.get_files_by_accession(val["acceession"], filter,
                                                 10, 2))

    def DownloadResources(self):
        pass
    def ImportResources(self):
        pass
    def download_files_by_name(self, accession, file_name, ftp_download_enabled, input_folder, output_folder):
        """
        This script download files from FTP or copy from the file system
        """

        raw_files = Files()

        print("accession: " + accession)

        if ftp_download_enabled:
            print("Data will be download from ftp")
            raw_files.download_file_from_ftp_by_name(accession, file_name, output_folder)
        else:
            print("Data will be copied from file system " + output_folder)
            raw_files.copy_file_from_dir_by_name(accession, file_name, input_folder)

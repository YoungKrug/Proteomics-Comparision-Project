from pridepy import Project
from util.api_handling import Util
import os
import logging
import urllib
import urllib.request
from Resources.ResourceDownloader import ResourceDownloader
from RawFIleConverter.RawToMZMLConverter import RawToMZMLConverter
class PrideDatabase:
    api_base_url = "https://www.ebi.ac.uk/pride/ws/archive/v2/"
    downloaded_file_paths = []
    def __init__(self, search_element, output_folder, amount_to_download=1):
        self.search_element = search_element
        self.accession_data = []
        self.output_folder = output_folder
        self.amount_to_download = amount_to_download
    def DownloadResources(self):
        if not (os.path.isdir(self.output_folder)):
            os.mkdir(self.output_folder)
        print(os.path)
        self.SearchDatabase()
        for accession_number in self.accession_data:
            print(f"Downloading data for {accession_number}")
            request_url = self.api_base_url + "files/byProject?accession=" + accession_number + ",fileCategory.value==RAW"
            headers = {"Accept": "application/JSON"}
           # response = self.get_file_from_api(project_accession, file_name)
           # self.download_files_from_ftp(response, output_folder)
            response = Util.get_api_call(request_url, headers)
            print(response.json())
            self.download_files_from_ftp(response.json(), self.output_folder)

    def SearchDatabase(self):
        project = Project()
        # Staphylococcus aureus is our prokaryote
        results = project.search_by_keywords_and_filters(
            str(self.search_element),  # search for a specific species
            "filter",  # you can define a filter here, but you don't need to
            1000,  # maximum number of results
            0,  # pages - no need to change this
            10,  # date gap - no need to change this
            "DESC",  # order in which results are sorted
            "submission_date",  # sorting criterium
        )
        for val in results["_embedded"]["compactprojects"]:
            self.accession_data.append(val["accession"])
            print(val["accession"])
    def ConvertToDataReadableFiles(self):
        mzmlConvert = RawToMZMLConverter(self.downloaded_file_paths)
        return mzmlConvert.ConvertToMZML(self.output_folder, self.search_element)

    def download_files_from_ftp(self, file_list_json, output_folder):
        """
        Download files using ftp transfer url
        :param file_list_json: file list in json format
        :param output_folder: folder to download the files
        """
        print("Downloading")
        file = file_list_json[0]
        if file['publicFileLocations'][0]['name'] == 'FTP Protocol':
            ftp_filepath = file['publicFileLocations'][0]['value']
        else:
            ftp_filepath = file['publicFileLocations'][1]['value']
        print(file)
        logging.debug('ftp_filepath:' + ftp_filepath)
        public_filepath_part = ftp_filepath.rsplit('/', 1)
        logging.debug(file['accession'] + " -> " + public_filepath_part[1])
        new_file_path = file['accession'] + "-" + public_filepath_part[1]
        filepath = f"{output_folder}/{new_file_path}"
        urllib.request.urlretrieve(ftp_filepath, filepath)
        self.downloaded_file_paths.append(filepath)
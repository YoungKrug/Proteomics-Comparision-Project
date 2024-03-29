from pridepy import Project
from util.api_handling import Util
import os
import logging
import urllib
import urllib.request
from Resources.ResourceDownloader import ResourceDownloader
from RawFIleConverter.RawToMZMLConverter import RawToMZMLConverter
class PrideDatabase:
    # This class is used to download pride archive databases. Use by passing a
    # search element, and output folder. There are option parameters as well
    api_base_url = "https://www.ebi.ac.uk/pride/ws/archive/v2/"
    downloaded_file_paths = []
    def __init__(self, search_element, output_folder, filterList = [], amount_to_download=1):
        self.search_element = search_element
        self.accession_data = []
        self.output_folder = output_folder
        self.amount_to_download = amount_to_download
        self.filterList = filterList
    def DownloadResources(self):
        # Gets the data to download the necessary resources
        new_directory = self.search_element[:5]
        new_path = os.path.join(self.output_folder, new_directory)
        if (not os.path.exists(new_path)):
            os.mkdir(new_path)
        self.output_folder = new_path
        self.SearchDatabase()
        counter = 0
        if(len(self.filterList) > 0):
            self.accession_data = self.filterList
            print(f"Filtering out accession data, new data:\n{self.accession_data}")
        for accession_number in self.accession_data:
            print(f"Downloading data for {accession_number}")
            request_url = self.api_base_url + "files/byProject?accession=" + accession_number + ",fileCategory.value==RAW"
            headers = {"Accept": "application/JSON"}
           # response = self.get_file_from_api(project_accession, file_name)
           # self.download_files_from_ftp(response, output_folder)
            response = Util.get_api_call(request_url, headers)
            # print(response.json())
            bacteriaName = self.search_element.replace(" ", "_")
            bacteriaName = f"{bacteriaName}_{counter}.raw"
            self.download_files_from_ftp(response.json(), self.output_folder, number=counter,
                                         bacteria_file=bacteriaName)
            counter += 1


    def SearchDatabase(self):
        # Searches for data
        project = Project()
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
        # Used to convert to mzml data, a wrapper function
        mzmlConvert = RawToMZMLConverter()
        return mzmlConvert.ConvertToMZML(self.output_folder, self.search_element.replace(" ", "_"))

    def download_files_from_ftp(self, file_list_json, output_folder, number, bacteria_file):
        """
        Download files using ftp transfer url
        :param file_list_json: file list in json format
        :param output_folder: folder to download the files
        """

        filepath = f"{output_folder}/{bacteria_file}"
        if(os.path.isfile(filepath)):
            print(f"{filepath} already exist, continuing...")
            self.downloaded_file_paths.append(filepath)
            return
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

        urllib.request.urlretrieve(ftp_filepath, filepath)
        self.downloaded_file_paths.append(filepath)

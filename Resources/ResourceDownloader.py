class ResourceDownloader: # Will be the downloader method for the pride datasets
    # This class is a wrapper for database downloads, you can create other databases like the pride database
    # in the database folder to download data with.
    def __init__(self, database):
        self.database = database
    def DownloadResources(self):
        self.database.DownloadResources()
    def ImportResources(self):
        self.database.ImportResources()
    def ConvertToDataReadableFiles(self): # In our cases, this converts to mzml, in sure your data downloads .raws
        return self.database.ConvertToDataReadableFiles()

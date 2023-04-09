class ResourceDownloader: # Will be the downloader method for the pride datasets
    def __init__(self, database):
        self.database = database
    def DownloadResources(self):
        self.database.DownloadResources()
    def ImportResources(self):
        self.database.ImportResources()
    def ConvertToDataReadableFiles(self):
        return self.database.ConvertToDataReadableFiles()

import ppx

# Enter you project ID
proj = ppx.find_project("PXD000001")
remote_files = proj.remote_files()
print(remote_files)

# Download a target remote file to your local drive
downloaded = proj.download("F063721.dat-mztab.txt")
print(downloaded)

proj = ppx.find_project("PXD000001", repo="PRIDE")
local_files = proj.local_files()
print(local_files)

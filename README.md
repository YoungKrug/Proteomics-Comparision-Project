# Proteocompare (A protein comparison tool)
### Protein One vs Protein Two
#### This is the hub of our project, please read everything below to properly create the environment.
##### To install the conda with all the required files, run this command -> 
##### conda env create -f environment.yml 
##### This will create the environment and import dependencies, after this you should be able to run the project
### To install Engine Packages
* Ursgal has a function named download_resources (ex... uc.download_resources(["YOUR RESOURCES TO DOWNLOAD"]))
* Use this to download engines such as thermal raw parser and percolator
#### To use our program, it will require you to know what bacteria you are looking for, and a reference protein (fasta file)
#### All of your results will be outputted in the user specified output folder.
#### During the second run, you can add other mzml files or raw files to the specified folders for more information!

# Proteomics Comparision Project
### Encephalitis vs Meningitis
#### This is the hub of our project, please read everything below to properly create the environment.
##### To install the conda with all the required files, run this command -> 
##### conda env create -f environment.yml 
##### This will create the environment and import dependencies, after this you should be able to run the project
### To install MSConvert: 
* Go to this webpage [MSReader](https://github.com/frallain/pymsfilereader/tree/master/MSFileReader) and install the 3.1SP4 exe (Make sure it correlates to your os, 32bits or 64 bits)
* Backup the *XRawfile2_x64.dll* at your install location and install MSFileReader 3.1SP2
* Remove the *XRawfile2_x64.dll* install with 3.1SP2 and replace it with the one you backed up
* Finally install pymsfilereader, pip install pymsfilereader.
#### The package should work now. Additionally, the pymsfilereader should be including inside of the environment.yml but you still must install the MSReader bindings. 

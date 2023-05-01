from PipelineBuilder.PipelineBuilder import PipelineBuilder
import os
# Example script for the pipeline
list = ["PXD003000", "PXD008055", "PXD000896", "PXD003261"] # You can filter for certain datasets you want if you know there Ids
listSalmonella = []
outputDir = "PrideResources/RawFiles"
fastaDir = "PrideResources/Fasta/Vibrio_Second/vibrio_B22.fasta"
pipeline = PipelineBuilder() # The pipeline builder class, used to construct and create the pipeline
# Requires a output and fastA directory, and a bacteria
# The with pride numbers it the class you enter the list of pride numbers you want to filter
pipeline.OutputDirectoryAt(directory=outputDir).\
    WithFastaFile(directory=fastaDir).\
    AsBacteria(bacteria="Salmonella enterica serotype typhi").\
    WithPrideNumbers().\
    Build()
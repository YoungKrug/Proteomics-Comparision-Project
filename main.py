from PipelineBuilder.PipelineBuilder import PipelineBuilder
import os
list = ["PXD003000", "PXD008055", "PXD000896", "PXD003261"]
listSalmonella = []
outputDir = "PrideResources/RawFiles"
fastaDir = "PrideResources/Fasta/Vibrio_Second/vibrio_B22.fasta"
pipeline = PipelineBuilder()
pipeline.OutputDirectoryAt(directory=outputDir).\
    WithFastaFile(directory=fastaDir).\
    AsBacteria(bacteria="Vibrio cholerae").\
    WithPrideNumbers(list).\
    Build()
from PipelineBuilder.PipelineBuilder import PipelineBuilder
import os

outputDir = "PrideResources/RawFiles"
fastaDir = "PrideResources/Fasta/salmonella"
pipeline = PipelineBuilder()
pipeline.OutputDirectoryAt(directory=outputDir).\
    WithFastaFile(directory=fastaDir).\
    AsBacteria(bacteria="Salmonella enterica serotype typhi").\
    Build()
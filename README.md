# Data2Bots Assessment

This is Paschal Uwakwe's submission of Data2Bots' technical assessment. 

## Overview
This is a simple project with a few files. The project has no requirements, and 
doesn't need a virtual environment.  
To run, enter `python3 main.py` while in the directory.  
The result shows up in `tests/text_files/test_output.json`.

## ElementType
This class is an enum that holds values for all supported element types.  
I took the liberty of adding Boolean and Object types since they weren't mentioned 
in the question.

## InvalidElementTypeError
This is a custom error raised if an unsupported element type is contained in 
the JSON file

## InvalidJsonError
This is a custom error raised when attempting to encode or decode invalid JSON

## JsonFileWriterReader
This is a wrapper class that wraps around Python's file API and json module.  
It has two methods that read or write JSON data from files, it also validates 
the data.

## JsonTransformer
This is the core class of the project. It handles the transformation of JSON data 
from the initial shape to the expected resultant shape. It has a `transform` 
method that handles the transformation, a `determine_type` helper method that 
detects the element type of each element passed, and a `run` method that acts 
as a client for reading, transforming and writing.

## Testing
To run tests, enter `python3 -m unittest discover -v`.
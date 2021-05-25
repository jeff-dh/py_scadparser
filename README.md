# py_scadparser
A basic openscad parser written in python using ply.

This parser is intended to be used within solidpython to import openscad code. For this purpose we only need to extract the global definitions of a openscad file. That's exactly what this package does. It parses a openscad file and extracts top level definitions. This includes global variables, function and module definitions.

Even though this parser actually parses (almost?) the entire openscad language (at least the portions used in my test libraries) 90% is dismissed and only the needed definitions are processed and extracted.

For information on what this parser is capable of and how to use it, take a look at the bottom of scad_parser.py.

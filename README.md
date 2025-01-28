# PXML Reader

PXML Reader is a Python module that allows you to read .pxml files. Based on the PXML standard by Progress Group, this reader was developed following the Progress manifesto to establish an automatic and efficient PXML reader.

## Table of Contents

- [Introduction](#introduction)
- [PXML Standard](#pxml-standard)
- [Authors](#authors)
- [Usage/Examples](#usageexamples)
- [Getting Started](#getting-started)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Introduction

PXML Reader is designed to simplify the process of reading and modifying .pxml files. It provides a straightforward interface for manipulating PXML data structures.

## PXML Standard

The PXML standard, created by ebawe, is a comprehensive XML-based format used for efficient data interchange. It is widely used in various industries for its robustness and flexibility. For more information, refer to the [PXML Specification 1.3](https://www.pxml.eu/PXML-Specification-1.3-EN.pdf).

## Authors

- [@faressofiane -- Sofiane Fares](https://github.com/FaresSofiane)
- [@Brisoz77 -- François BRIDONNEAU](https://github.com/Bridoz77)

## Usage/Examples

```python
from PXML_Reader import *

# Read a file
file_path = "//path/to/your/file"
pxml_obj = pxml(file_path)

# Modify a file
pxml_obj.DocInfo.Comment = "test"  # Refer to PXML documentation for the correct value position

element = elementinfo.ElementInfo("test", True, "test", "test", "test", "test", 1, 1.0, 1.0, "test", "test", [])
element.ElementInfoVal.append(eleminfoval.ElemInfoVal(Type="test", V="test"))
pxml_obj.Order[0].Product[0].ElementInfo.append(element)

# Save the file
with open(file_path, 'w', encoding='UTF-8') as file:
    file.write(pxml_obj.__xml__())
```

## Getting Started

To get started with PXML Reader, follow these steps:

Clone the repository:
``` sh
git clone https://github.com/FaresSofiane/PXML_Reader.git
```
Install the required dependencies:
```sh
pip install -r requirements.txt
```
Run your first PXML Reader script:
```sh
python your_script.py
```

## Acknowledgments

Special thanks to the Progress Group for their support and the creation of the PXML standard.

## License

This project is licensed under the MIT License - see the LICENSE file for details.





# https://github.com/HannaKoo/IMC_Leeds_2027/blob/42534ffc8cbfb6a7336e3bde8d0eb0a837fbd622/Sample_cases

import xml.etree.ElementTree as ET

tree = ET.parse("Sample_cases")
root = tree.getroot()

print(root.tag)

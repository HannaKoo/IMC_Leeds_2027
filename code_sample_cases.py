

https://github.com/HannaKoo/IMC_Leeds_2027/blob/42534ffc8cbfb6a7336e3bde8d0eb0a837fbd622/Sample_cases

from pathlib import Path
import xml.etree.ElementTree as ET


def xml_to_text(xml_file):
    """
    Read an XML file and return all textual content
    with XML tags removed.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    text_parts = []

    for text in root.itertext():
        text = text.strip()

        if text:
            text_parts.append(text)

    return " ".join(text_parts)


if __name__ == "__main__":
    xml_file = Path("data/example.xm")

    text = xml_to_text(xml_file)

    print(text)

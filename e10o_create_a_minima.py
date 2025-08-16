Python
import re
import xml.etree.ElementTree as ET

class MinimalistParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.parsed_data = {}

    def parse_xml(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        for elem in root:
            self.parsed_data[elem.tag] = elem.text

    def parse_csv(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            for line in lines[1:]:
                data = line.strip().split(',')
                self.parsed_data[data[0]] = {header: value for header, value in zip(headers, data[1:])}

    def parse_json(self):
        import json
        with open(self.file_path, 'r') as file:
            self.parsed_data = json.load(file)

    def get_parsed_data(self):
        return self.parsed_data


def main():
    parser = MinimalistParser('path_to_your_file.xml')  # Replace with your file path
    # parser.parse_xml()
    # parser.parse_csv()
    parser.parse_json()  # Uncomment the parser you want to use
    print(parser.get_parsed_data())


if __name__ == "__main__":
    main()
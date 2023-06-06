import csv
import xml.etree.ElementTree as ET

def xml_to_csv(xml_file_path, csv_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the column headers
        headers = []
        for child in root[0]:
            headers.append(child.tag)
        writer.writerow(headers)

        # Loop through each element and write a new row to the CSV file
        for element in root:
            row = []
            for child in element:
                row.append(child.text)
            writer.writerow(row)

if __name__ == '__main__':
    xml_to_csv('example.xml', 'example.csv')

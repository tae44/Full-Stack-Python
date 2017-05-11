from xml.etree import ElementTree as ET

tree = ET.parse('first.xml')
root = tree.getroot()

def a():
    for node in root.iter('year'):
        new_year = int(node.text) + 1
        node.text = str(new_year)
        node.set('name', 'jeff')
        del node.attrib['name']
    tree.write('new.xml', encoding='utf-8')

def b():
    for country in root.findall('country'):
        rank = int(country.find('rank').text)
        if rank > 50:
            root.remove(country)

def c():
    for country in root.find('country'):
        print(country)

if __name__ == '__main__':
    for node in root.iter('year'):
        print(node.tag, node.text)


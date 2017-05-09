from xml.etree import ElementTree as ET
from xml.dom import minidom

def pretty(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='\t')

root = ET.Element('family')

son1 = root.makeelement('son', {'name': 'son1'})
son2 = root.makeelement('son', {'name': 'son2'})

grandson1 = son1.makeelement('grandson', {'name': 'son11'})
grandson2 = son1.makeelement('grandson', {'name': 'son22'})

son1.append(grandson1)
son1.append(grandson2)

root.append(son1)
root.append(son2)

raw_str = pretty(root)

f = open('xxx.xml', 'w', encoding='utf-8')
f.write(raw_str)
f.close()

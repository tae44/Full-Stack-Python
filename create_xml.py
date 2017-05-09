from xml.etree import ElementTree as ET

root = ET.Element('famliy')

def a():
    son1 = ET.Element('son', {'name': 'son1'})
    son2 = ET.Element('son', {'name': 'son2'})

    grandson1 = ET.Element('grandson', {'name': 'son11'})
    grandson2 = ET.Element('grandson', {'name': 'son22'})

    son1.append(grandson1)
    son1.append(grandson2)

    root.append(son1)
    root.append(son2)

def b():
    son1 = root.makeelement('son', {'name': 'son1'})
    son2 = root.makeelement('son', {'name': 'son2'})

    grandson1 = son1.makeelement('grandson', {'name': 'son11'})
    grandson2 = son1.makeelement('grandson', {'name': 'son22'})

    son1.append(grandson1)
    son1.append(grandson2)

    root.append(son1)
    root.append(son2)

def c():
    son1 = ET.SubElement(root, 'son', attrib={'name': 'son1'})
    son2 = ET.SubElement(root, 'son', attrib={'name': 'son2'})

    grandson1 = ET.SubElement(son1, 'age', attrib={'name': 'son11'})
    grandson1.text = 'grandson'

if __name__ == '__main__':
    c()
    tree = ET.ElementTree(root)
    tree.write('ooo.xml', encoding='utf-8')

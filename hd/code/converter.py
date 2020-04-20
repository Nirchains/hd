# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def main():
	tree = ET.parse("charts.xml")
	#print(doc.nodeName)
	root = tree.getroot()

	for record in root:
		#print record.tag, record.attrib
		for field in record.iter("field"):
			print ("%s - %s" % (field.attrib, field.text))
		print("---------")


if __name__ == "__main__":
	main()
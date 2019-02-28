import xml.etree.ElementTree as et

stu = et.Element("Studentb1.xml")

name = et.SubElement(stu, "Name")
name.attrib = {"lang", "en"}
name.text = "xiaodong"

age = et.SubElement(stu, "Age")
age.text = 18

et.dump(stu)
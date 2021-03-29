import xml

with open("allSprites_default.xml") as f:
    data = xml.dom.minidom.parse(f)

print(data)

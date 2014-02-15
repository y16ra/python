#
# parsing maven pom.xml
# artifactId & version
#
from xml.etree import ElementTree

POM_FILE="y16ra/test_pom.xml"  # replace your path
namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}

tree = ElementTree.parse(POM_FILE)
root = tree.getroot()

deps = root.findall(".//xmlns:dependency", namespaces=namespaces)
for d in deps:
    artifactId = d.find("xmlns:artifactId", namespaces=namespaces)
    version    = d.find("xmlns:version", namespaces=namespaces)
    print artifactId.text + '\t' + version.text


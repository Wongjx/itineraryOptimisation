import xml.etree.ElementTree as etree

ns = {'kml': 'http://www.opengis.net/kml/2.2'}

def parseKML(file):
    tree = etree.parse(file)
    root = tree.getroot()
    # print("Root",root)
    # print("Root Tag: ",root.tag)
    # print("Root Attrib: ",root.attrib)
    # print("Root Items: ",root.items())
    # print("Root Keys: ",root.keys())
    # print("Root Document",root.get("Document"))

    placeMarks = []

    for placemark in root.iter("Placemark"):
        # print("Placemark tag: ",placemark.tag)
        # print("Placemark attrib: ",placemark.attrib)
        # print("Placemark Coordinates: ",placemark.findtext('coordinates'))
        # for text in placemark.itertext():
        #     print(text)
        # print(placemark.items())
        for child in list(placemark):
            if(child.tag=="Point"):
                coord = list(child)[0].text
                lat,lon,x = coord.strip().split(",")
                # print(coord.strip().split(",")) 
            if(child.tag=="name"):
                name=child.text
        placeMarks.append(Placemark(name,float(lat),float(lon)))
    return placeMarks

def parseKMLforKmeans(file):
    placemarks = parseKML(file)
    nameList=[]
    comList=[]
    for placemark in placemarks:
        nameList.append(placemark.name)
        # lonList.append((float(placemark.lat)-126)*10)
        # latList.append((float(placemark.lon)-33)*10)
        # lonList.append(placemark.lat)
        # latList.append(placemark.lon)
        comList.append([placemark.lat,placemark.lon])
    return nameList,comList


class Placemark:
    def __init__(self,name,lat,lon):
        self.name=name;
        self.lat=lat;
        self.lon=lon;

    def __str__(self):
        return "Placemark:"+self.name+","+self.lat+","+self.lon

if __name__ == "__main__":
    # execute only if run as a script
    # parseKML("doc.kml")
    parseKMLforKmeans("doc.kml")
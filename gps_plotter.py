# receives a 2d list of coordinates and plots them using google maps.
# The simplekml python module seems like a good choice. The maps
# need to be imported on My Maps though.

import gmplot
import simplekml

# !!!NEW!!! way to write to google maps. Creates KML files instead
# of html. Opened on Google maps. I dunno if this is preferable
# but whatever.
# filename doesnt need extension.
# data 2d list: [lat,lng,speed,time]
def kmlPlotter(filename,data):
    # create kml object
    kml = simplekml.Kml()

    # iterate through each list in data
    for i in data:
        # name is curently speed,time
        point_name = str(i[2]) + ',' + (str(i[3]))
        # coords is in the format longitude,latitude instead
        # of latitude,longitude because fuck you
        kml.newpoint(name=point_name, coords=[(i[1],i[0])])

    # save kml
    kml.save(filename + '.kml')

### <OLD> ###
### Old stuff that uses gmplot to create an html file. It works
### but there doesn't seem to be a way to label markers which
### is pretty important

# receive 2d list and return list of lats (which should be in
# position 0 of lists in data)
def extractLats(data):
    return [i[0] for i in data]

# receive 2d list and return list of lngs (which should be in
# position 1 of lists in data)
def extractLngs(data):
    return [i[1] for i in data]

# receive filename (no extension), 2d list of data, and setup list
def gpsPlotter(filename, data, setup):
    # extract the lats and lngs of data into a list
    lats = extractLats(data)
    lngs = extractLngs(data)
    # create GoogleMapPlotter object with (center lat,center long, zoom)
    gmap = gmplot.GoogleMapPlotter(setup[0],setup[1],setup[2])

    # create a scatter plot using the lats and lngs.
    gmap.scatter(lats,lngs,'b',marker=True)

    # write gmap to file
    gmap.draw(filename + '.html')

### </OLD> ###

if __name__ == '__main__':
    # just example data

    data = [[33.46211,-112.42335,0,0],
            [33.46225,-112.41806,1,1],
            [33.46137,-112.40798,2,2]]

    filename = "temp"

    kmlPlotter(filename,data)

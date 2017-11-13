# receives a 2d list of coordinates and plots them using google maps.
# The gmplot python module seems like a good choice

# collection of example plots

# plot(lat_list,lng_list, color, width). Just creates a line
# between points
# gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)

# scatter(lat_list,lng_list,color,size,marker). creates markers
# on the points
#gmap.scatter(lats, lngs, '#3B0B39', size=40, marker=False)
#gmap.scatter(lats, lngs, 'k', marker=True)

#gmap.heatmap(heat_lats, heat_lngs)

import gmplot

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

if __name__ == '__main__':
    # creates a GoogleMapPlotter object named gmap with center lat 37.428,
    # center lng -122.145, and zoom 9
    # gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 9)

    # just example data
    setup = [37.428,-122.145,14]

    data = [[37.42,-122.145,0,0],
            [37.418,-122.144,0,0],
            [37.414,-122.140,0,0]]

    filename = "temp"

    gpsPlotter(filename,data,setup)

    # collection of example plots

    # plot(lat_list,lng_list, color, width). Just creates a line
    # between points
    # gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)

    # scatter(lat_list,lng_list,color,size,marker). creates markers
    # on the points
    #gmap.scatter(lats, lngs, '#3B0B39', size=40, marker=False)
    #gmap.scatter(lats, lngs, 'k', marker=True)

    #gmap.heatmap(heat_lats, heat_lngs)

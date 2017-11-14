# File responsible for taking a 2d list of gps data and writing it
# to an excel spreedsheet

import xlwt
import csv

# !!!NEW!!! way to write to excel file using csv files.
# filename without extension. Data 2d list [lat,lng,speed,time]
def csvWriter(filename, data):
    # open file
    with open(filename + '.csv', "wb") as csv_file:
            writer = csv.writer(csv_file,delimiter=',')
            header = ['Latitude','Longitude','Speed','Time']
            writer.writerow(header)
            for line in data:
                writer.writerow(line)

### <OLD> ###
### csv is a simpler file to read and write to. This still works
### though with xlx files though

# recieve filename and 2d list of gps data
# data should be in format: [Latitude, Longitude, Speed, Time]
# filename should not have an extension
def excelWriter(filename, data):
    # create workbook object and sheet object
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1')
    # keeps track of the row that will be written to
    row = 1

    # write headers to the columns. write(row,columns,data)
    sheet1.write(0,0, "Latitude")
    sheet1.write(0,1, "Longitude")
    sheet1.write(0,2, "Speed")
    sheet1.write(0,3, "Time")

    # move through 2d list data and write them to sheet.
    # i iterates through the lists
    # j,k hold the position and value in list i
    for i in data:
        for j,k in enumerate(i):
            sheet1.write(a,j,k)
        row += 1

    # save workbook using filename. .xlx appended
    workbook.save(filename + '.xlx')

### </OLD> ###

if __name__ == '__main__':

    data = [[1,2,3,4], [1,2,3,4]]

    csvWriter('temp',data)

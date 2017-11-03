#

import xlwt

# recieve filename and lat, long, speed, time data and write to xlx file
def excelWriter(filename, data):
    # create workbook object and sheet object
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1')

    a = 1

    # write headers to the columns. write(row,columns,data)
    sheet1.write(0,0, "Latitude")
    sheet1.write(0,1, "Longitude")
    sheet1.write(0,2, "Speed")
    sheet1.write(0,3, "Time")

    # move through data and write them to sheet
    for i in data:
        for j,l in enumerate(i):
            sheet1.write(a,j,l)
        a += 1


    # save workbook using filename
    workbook.save(filename)

if __name__ == '__main__':

    data = [[1,2,3,4], [1,2,3,4]]

    excelWriter('temp.xlx',data)

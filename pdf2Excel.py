import camelot
import xlwt
import xlrd

data = xlrd.open_workbook("1.xls")
book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
row = 0
for i in range(13):
    table = data.sheet_by_name("page-{}-table-1".format(i+1))

    for j in range(9, table.nrows):
        msg = table.row_values(j)
        for k in range(table.ncols):
            sheet.write(row, k, msg[k])
        row += 1

book.save('output.xls')
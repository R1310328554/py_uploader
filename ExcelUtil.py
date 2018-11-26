import logging
import xdrlib, sys
import xlrd


def open_excel(file='account.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        logging.error(str(e))


def excel_table_byname(file='account.xlsx', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数

    # logging.info("colnameindex " + str(colnameindex))
    # logging.info("nrows " + str(nrows))
    colnames = table.row_values(0)  # 某一行数据
    # logging.info("colnames " + str(colnames))

    list = []
    for rownum in range(1, nrows):
        # print("rownum " + str(rownum))
        row = table.row_values(rownum)
        if row:
            app = {}

            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def main():
    tables = excel_table_byname(file='account.xlsx',colnameindex=2)
    for row in tables:
        print(row)


if __name__ == "__main__":
    main()

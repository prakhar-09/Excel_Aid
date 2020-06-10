import xlrd
sheet_data = []   
wb = xlrd.open_workbook(Path_to_xlsx)
p = wb.sheet_names()
for y in p:
   sh = wb.sheet_by_name(y)
   for rownum in xrange(sh.nrows):
      sheet_data.append((sh.row_values(rownum)))

found_list = []
rows_to_be_saved = []
for i in sheet_data:
  if i[2] == "string_1" or i[2] == "string_2" or i[2] == "string_3" or i[2] == "string_4" or i[2] == "string_5":
    found_list.append(i)
  else:
      rows_to_be_saved.append(i)

text_file = open("Output_file.txt", "w")
text_file.write(found_list)
text_file.close()

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
  if i[2] == "string1" or i[2] == "string2" or i[2] == "string3" or i[2] == "string4" or i[2] == "string5":
    found_list.append(i)
  else:
      rows_to_be_saved.append(i)

text_file = open("Output.txt", "w")
text_file.write(found_list)
text_file.close()
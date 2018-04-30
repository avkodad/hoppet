def svdt(x):

wb = openpyxl.Workbook()
sheet = wb.active

for i, entry in enumerate(x, start=1): sheet.cell(row=2, column=i, value = entry)

wb.save('usrdata.xlsx')




ref = input('Er referens?')
kontakt = input('Kontakt')
tot = (ref,kontakt)
#varor = str(input('Hur manga?'))
#, varor)
#datum = 
#summa = 


for i, row in enumerate(tot):
        ws.write(i, 0, row )

wb.save('exempelexcel.xls')

"""

- ta in betsumma, antal, ref och datum
- namnge varje sparad kvitto/faktura med datum
- omvandla till PDF kvitto
- maila kvitto
- smsa bestallningar till kvinnor

- 


"""






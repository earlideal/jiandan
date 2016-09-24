import win32print

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
names = []
for printer in printers:
    names.append(printer[2])

print names

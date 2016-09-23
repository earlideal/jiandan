import win32print

print win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS
                              + win32print.PRINTER_ENUM_LOCAL)
print win32print.GetDefaultPrinter()

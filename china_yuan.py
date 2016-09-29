# -*- coding: utf8 -*-


def rmb_digits_to_char(currency):
    zen = u'整'
    dot = currency.find('.')
    if dot == -1:
        total = integral(currency) + zen
    else:
        int_part = currency[:dot]
        dec_part = currency[dot + 1:len(currency)]
        if dec_part == '00' or dec_part == '0':
            total = integral(int_part) + zen
        else:
            total = integral(int_part) + decimal(dec_part)
    return total


def integral(currency):
    units = ['', u'万', u'亿']
    ratio = ['', u'拾', u'佰', u'仟']
    yuan = u'元'
    num = len(currency)
    zero_num = 0
    total = ''
    for i in xrange(0, num):
        j = num - i - 1
        x = j / 4
        y = j % 4
        d = currency[i]
        if d == '0':
            zero_num += 1
        else:
            if zero_num > 0:
                total += digit2char('0')
            zero_num = 0
            total += digit2char(d) + ratio[y]
        if y == 0 and zero_num < 4:
            total += units[x]
    total += yuan
    return total


def decimal(currency):
    units = [u'角', u'分']
    num = len(currency)
    total = ''
    for i in xrange(0, num):
        total += digit2char(currency[i]) + units[i]
    return total


def digit2char(digits):
    digits_num = '0123456789'
    digits_char = u'零壹贰叁肆伍陆柒捌玖'
    index = digits_num.find(digits)
    char = '口'
    if index != -1:
        char = digits_char[index]
    return char

import log

def check_telephone_number(symbol: str) -> str:
    '''
    Проверка ввода номера телефона
    '''
    if len(symbol)<12 and len(symbol)>4:
        if not symbol[0].isdigit() and symbol[0] != '+':
            log.logger(f"Ошибка в строке {symbol}", "Ошибка")
            return ''
        else:
            for i in range(1,len(symbol)):
                if not symbol[i].isdigit(): 
                    log.logger(f"Ошибка в строке {symbol}", "Ошибка")
                    return ''
        # print(symbol, i, symbol[i], symbol[i].isdigit(), symbol[i].isdigit() or symbol[i] != '+')
    else: 
        log.logger(f"Ошибка в строке {symbol}", "Ошибка")
        return ''
    return symbol

def check_fio(symbol: str) -> str:
    new_string = ''
    if len(symbol)>2 and len(symbol) <=40:
        for i in range(len(symbol)):
            if symbol[i].isdigit() or symbol[i] == '+' or symbol[i] == '*' or symbol[i] == '/' or symbol[i] == ' ' or symbol[i] == ',' or symbol[i] == ';' or symbol[i] == ':' or symbol[i] == '.':
                log.logger(f"Ошибка в строке {symbol}", "Ошибка")
                return ''
            else:
                if i==0 or symbol[i-1] == '-':
                    new_string = new_string + symbol[i].upper()
                else:
                    new_string = new_string + symbol[i] 
        return new_string
    else:
        log.logger(f"Ошибка в строке {symbol}", "Ошибка")
        return ''
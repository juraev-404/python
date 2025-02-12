def km(el):
    if el[-2:] == 'см':
        return f'{int(el[:-2])/100000}км'
    elif el[-2:] == 'дм':
        return f'{int(el[:-2])/10000}км'
    elif el[-1] == 'м':
        return f'{int(el[:-2])/1000}км'
    elif el[-2:] == 'км':
        return el

def m(el):
    if el[-2:] == 'см':
        return f'{int(el[:-2])/100}м'
    elif el[-2:] == 'дм':
        return f'{int(el[:-2])/10}м'
    elif el[-1] == 'км':
        return f'{int(el[:-2])*1000}м'
    elif el[-2:] == 'м':
        return el

def dm(el):
    if el[-2:] == 'см':
        return f'{int(el[:-2])/10}дм'
    elif el[-2:] == 'км':
        return f'{int(el[:-2])*10000}дм'
    elif el[-1] == 'м':
        return f'{int(el[:-2])*10}дм'
    elif el[-2:] == 'дм':
        return el
    
def sm(el):
    if el[-2:] == 'км':
        return f'{int(el[:-2])*100000}см'
    elif el[-2:] == 'дм':
        return f'{int(el[:-2])*10}см'
    elif el[-1] == 'м':
        return f'{int(el[:-2])*100}см'
    elif el[-2:] == 'см':
        return el
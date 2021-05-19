stroke1 = 'строкcdscdcdа'
stroke2 = 'learn'

def compare_stroke(stroke1, stroke2):
    if type(stroke1) is  not str or type(stroke2) is not str:
        return '0'
    elif stroke1 == stroke2:
        return '1'
    elif stroke2 == 'learn':
        return '3'
    elif len(stroke1) > len(stroke2):
        return '2'
    

print(compare_stroke(stroke1, stroke2))

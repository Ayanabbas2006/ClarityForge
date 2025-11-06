from datetime import datetime
hour=int(str(datetime.now()).split()[1].split(':')[0])

def color(a: int,b: int,c: int)-> list:
    return [a/256,b/256,c/256,1]

def rev_color(a: int,b: int,c: int)->  list:
    return [((256-a)/256),((256-b)/256),((256-c)/256),1]
def theme():
    if 20<=hour<=23 or 0<=hour<5:
        return [color(15,19,117),rev_color(15,19,117),'Good Night']
    elif 5<=hour<12:
        return [color(156, 184, 44),rev_color(156, 184, 44),'Good Morning']
    elif 12<=hour<17:
        return [color(68, 192, 219),rev_color(68, 192, 219),'Good Afternoon']
    return [color(173, 124, 45),rev_color(86,62,22),'Good evening']

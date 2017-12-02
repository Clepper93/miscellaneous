class Funletter:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
def fun_with_names():
    myname = str(input("What is your name?\n")).lower()
    letterlist = [Funletter('a','awesome'),Funletter('b','badass'),Funletter('c','cool'),Funletter('d','divine'),Funletter('e','excellent'),Funletter('f','fantastic'),Funletter('g','great'),Funletter('h','honorable'),Funletter('i','incredible'),Funletter('j','jovial'), Funletter('k','kingly'),Funletter('l','lively'),Funletter('m','magnificent'),Funletter('n','neato'),Funletter('o','outstanding'),Funletter('p','perfect'),Funletter('q','queenly'),Funletter('r','rad'),Funletter('s','superb'),Funletter('t','terrific'),Funletter('u','unique'),Funletter('v','vivaceous'),Funletter('w','wonderful'),Funletter('x','xtremely good'),Funletter('y', 'yes'),Funletter('z','zany')]
    for char in myname:
        if not char.isalpha():
            print("{} is for...???".format(char))
        else:
            for letter in letterlist:
                if letter.name == char:
                    print("{} is for {}!".format(char,letter.desc))
fun_with_names()

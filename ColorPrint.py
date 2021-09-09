class ColorPrint:
    def __init__(self):
        self.CEND = '\33[0m'
        self.CRED = '\33[31m'
        self.CBLUE = '\33[34m'
        self.CGREEN = '\33[32m'
        self.CBLINK = '\33[5m'
        self.CBOLD = '\33[1m'

    def print_blue(self,string):
        print(self.CBLUE + string + self.CEND)  

    def print_red(self,string):
        print(self.CRED + string + self.CEND)

    def print_green(self,string):
        print(self.CGREEN + string + self.CEND)          

    def print_blink(self,string):
        print(self.CBLINK + string  + self.CEND)    

    def print_bold(self,string):
        print(self.CBOLD + string + self.CEND)    
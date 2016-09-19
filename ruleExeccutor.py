__author__ = 'pramodkumar'
class rules:
    def __init__(self):
        self.ruleCount=0
    def r1(self):
        "R1 modlue to add two numbers"
        print self.__doc__


from os import walk

f = []
for dirpath, dirnames, filenames in walk(r"E:\bits-dissertation\code\rules"):
    pass
ruleInstance=rules()
for file in filenames:
    try:
        # with open (dirpath+"/"+file, 'r') as fileopen:
        #     f.append(fileopen.read())
        execfile(dirpath+"\\"+file)
        setattr(ruleInstance,file,locals()[file])
    except Exception as e:
        print "Failed reading rule file",file
print f

def insert(code):
    try:
        exec (code)
        return 1
    except Exception as e:
        print e
        return 0

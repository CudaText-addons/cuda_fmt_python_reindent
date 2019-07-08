from .reindent import Reindenter

class MyFile:
    newlines = '\n'
    def __init__(self, lines):
        self.lines = lines
    def readlines(self):
        return self.lines

def do_reindent(text):

    fake = MyFile(text.split('\n'))
    r = Reindenter(fake)
    r.run()
    return ''.join(r.after)

from .reindent import Reindenter
from io import StringIO

def do_reindent(text):

    f = StringIO(text)
    r = Reindenter(f)
    r.run()
    f.close()
    return ''.join(r.after)

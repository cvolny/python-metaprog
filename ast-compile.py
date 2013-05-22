#!/usr/bin/python2.6

import ast

code = '''
for i in range(10):
    print(i)
del i
'''

expar = ast.parse(code, mode='exec')
execu = compile(expar, '<stdin>', 'exec')
exec(execu)

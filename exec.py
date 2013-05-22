#!/usr/bin/python3
'''
Use exec() to declare a dynamic function, then call it.
'''


#pylint: disable=W0122,C0103

def lookup(name, globaldict=None, localdict=None):
    '''Resolve a name within global or local dictionaries'''
    scope = (globaldict if globaldict else {}).copy()
    scope.update(localdict if localdict else {})
    return scope.get(name)

def test_func(x):
    '''Test exec() of a module function.'''
    fname = "foo"
    code = '''def {0:s}(x=10):
        """ Print 1..x to stdout. """
        for i in range(1, x+1):
            print(i)
    '''.format(fname)
    exec(code)
    func = lookup(fname, {}, locals())
    assert callable(func)
    func(x)

def test_method(message = "Hello World!", default = "My Default Message!"):
    '''Test exec() of an instance method.'''
    clsname = 'A'
    methname = 'foo'
    clscode = '''class {0}:
        def __init__(self, default="Hello!"):
            self.default = default
        '''.format(clsname)
    methodcode = '''def {0}(self, msg=None):
        print(msg if msg else self.default)'''.format(methname)
    exec(clscode)
    cls = lookup(clsname, None, locals())
    assert isinstance(cls, object)
    exec(methodcode)
    meth = lookup(methname, None, locals())
    setattr(cls, methname, meth)
    func = lookup(methname, None, cls.__dict__)
    assert callable(func)
    inst = cls(default)
    func(inst)
    func(inst, message)
    func(cls())



def main():
    '''Program entry point'''
    print("Testing Function Creation:")
    test_func(5)
    print()
    print("Testing Class and Method Creation (binding):")
    test_method("Hello World!")





if __name__ == "__main__":
    main()

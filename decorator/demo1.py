def log(func)：
    def wrapper(*args, **kw):
        print 'call %s()'
    

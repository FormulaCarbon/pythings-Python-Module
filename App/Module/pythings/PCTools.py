def test():
    print('Test Complete. Pythings PCTools working.')
    return 'PCTools Working'

def pypiinstall(modname, os, modsrc = 'pypi'):
    import os
    modname=str(modname)
    if modsrc == 'pypi':
        src = ''
    elif modsrc == 'testpypi':
        src = '--index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ '
    elif modsrc != 'pypi' and modsrc != 'testpypi':
        raise ValueError('"'+modsrc+'" is not a valid argument for modsrc. Valid arguements are "pypi" and "testpypi".')
    if os == 'windows':
        os.system('py -m pip install ' +src+ modname)
    elif os == 'unix-mac':
        os.system('python3 -m pip install '+src+modname)
    elif os != 'windows' and os != 'unix-mac':
        raise ValueError('"'+os+'" is not a valid argument for os. Valid arguements are "windows" and "unix-mac".')

def notify(title, desc, appname='pythings',icon=None, time='2', status=None, toast=False):
    from plyer import notification
    notification.notify(
        title = title,
        message = desc,
        app_name = appname,
        app_icon = icon,
        timeout = int(time),
        ticker = status,
        toast = toast
    )

def slice_mail(address):
    user = address[:address.index('@')]
    domain = address[address.index('@') + 1:]
    sm = {"username": user, "domain": domain}
    return sm.copy()
def debug(filename, encodetype='utf_8'):
    
    file = open(filename, 'r', encoding = encodetype)
    code = file.read()
    try:
        exec(code)
    except Exception as e:
        print(e)

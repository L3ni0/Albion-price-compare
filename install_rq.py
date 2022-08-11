import importlib

def install_and_import(package):
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


def check_modules():
    modules = ['requests', 'pandas']
    for modul in modules:
        if importlib.util.find_spec(modul):
            print(f'{modul} jest pobrany')
        else:
            print(f'pobieranie {modul}')
            install_and_import(modul)
    print('gotowe')
    
check_modules()
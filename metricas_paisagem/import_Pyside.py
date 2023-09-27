import platform
import subprocess 
import sys

try:
    import PySide2
except ModuleNotFoundError:
    if platform.system() == 'Windows':
        subprocess.call([sys.exec_prefix + '/python', "-m", 'pip', 'install', 'PySide2'])
    else:
        subprocess.call(['python3', '-m', 'pip', 'install', 'PySide2']) 
    import PySide2
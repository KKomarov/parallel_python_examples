import os
import sys

arguments = (sys.executable, '\called_process.py',)

print('calling...')
print(os.getcwd())
# os.execvp('calc', ('calc',))
os.execvp(sys.executable, arguments)

print('Goodbye!!')

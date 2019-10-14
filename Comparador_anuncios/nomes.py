
import os
from Extrator import *

array = []
for filename in os.listdir('pdfs'):
    array.append(filename.__str__())
    extrator(filename)

print(array)


from sys import stdout, version
from os import write

stdout.write(version + '\n')
a = 3; b = 4
stdout.write(str(a+b)+'\n')
stdout.write(str(a-b)+'\n')
stdout.write(str(a*b)+'\n')
stdout.write(str(a%b)+'\n')
stdout.write(str(a/b)+'\n')
stdout.write(str(a**b)+'\n')
stdout.write(str(a//b)+'\n')


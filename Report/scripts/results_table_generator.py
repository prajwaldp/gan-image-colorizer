basepath = 'results'

# items = [23, 24, 30, 36, 40, 45, 48, 54, 56, 60, 65, 72, 73, 89, 130,
#          133, 138, 171, 179, 207, 219, 83, 97, 192, 81, 123, 246]

items = [23, 24, 30, 36, 40, 45, 48, 54, 56, 60, 65, 72, 73, 89, 130, 133, 138, 171, 179, 207, 219, 83, 97, 192]

template = '''
\includegraphics[width=2cm]{} &
\includegraphics[width=2cm]{} &
\includegraphics[width=2cm]{} \\
'''

res = ''

for i in items:
    res += '\includegraphics[width=2cm]{{{}3/{}-bw.png}} & '.format(basepath, i)
    res += '\includegraphics[width=2cm]{{{}3/{}-gt.png}} & '.format(basepath, i)
    res += '\includegraphics[width=2cm]{{{}5/{}-relucnn.png}} & '.format(basepath, i)
    res += '\includegraphics[width=2cm]{{{}5/{}-tanhcnn.png}} & '.format(basepath, i)
    res += '\includegraphics[width=2cm]{{{}3/{}-gan.png}} \\\\ \n'.format(basepath, i)

print(res)

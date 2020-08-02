from sys import argv

script, file_from, file_to = argv

file_from = open(file_from)
content1 = file_from.read()
content2 = input('> ')

to_file = open(file_to, 'w')
to_file.write(content1 + '\n' + content2)

file_from.close()
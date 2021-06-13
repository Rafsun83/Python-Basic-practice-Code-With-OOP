# class open_file():
#     def __init__(self, filename, mode):
#         self.filemane = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filemane, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with open_file ('sample.txt', 'w') as f:
#     f.write('Testing')
#
# print(f.closed)
#
#

from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file('sample.txt', 'w') as f:
    f.write('hi im human bt i have no humanity')
print(f.closed)

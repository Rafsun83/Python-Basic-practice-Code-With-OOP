# rev = reversed('spam')
#
#
# for char in rev:
#     print(char)

# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]

# data = 'golf'
# x = list(data[i] for i in range(len(data)-1, -1, -1))
# print(x)


from urllib.request import urlopen
with urlopen('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)


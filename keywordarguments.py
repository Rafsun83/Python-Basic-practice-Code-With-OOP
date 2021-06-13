# def student(age, **other):
#     print(age)
#     print(other)
#
# student(25, name = 'rafsun',number= 'number')

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
#
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')



def chees(kind, *arguments, **others):
    print("my name is ", kind)
    print("my country name is", kind)

    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in others:
        print(kw, ': ', others[kw])

chees('Rafsun', 'my university name is bubt',
      'my collage name is cumilla gov. collage',
      name = 'rafsun jani',
      roll =  83,
      intake = 38,
      section = 2

      )

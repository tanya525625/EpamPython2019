"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __init__(self, shift):
        self.shift = shift
        self.value = ''

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        new_value = ''
        for curr_char in value:
            curr_value = chr(ord(curr_char) + self.shift)
            if ord(curr_value) > 122:
                curr_value = chr(ord(curr_char) + self.shift - 123 + ord('a'))
            new_value += curr_value
        self.value = new_value


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)
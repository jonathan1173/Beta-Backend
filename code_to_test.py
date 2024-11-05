# -*- coding: utf-8 -*-
def concatenate(str1, str2):
    return str1 + str2

if __name__ == "__main__":
    assert concatenate("Hola, ", "mundo!") == "Hola, mundo!", "Error: concatenate('Hola, ', 'mundo!') debería ser 'Hola, mundo!'"
    assert concatenate("Python", "3.10") == "Python3.10", "Error: concatenate('Python', '3.10') debería ser 'Python3.10'"
    assert concatenate("123", "456") == "123456", "Error: concatenate('123', '456') debería ser '123456'"
    assert concatenate("", "Test") == "Test", "Error: concatenate('', 'Test') debería ser 'Test'"
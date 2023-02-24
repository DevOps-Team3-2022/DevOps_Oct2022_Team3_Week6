import pytest
from helloworld import *
def success_string():
  result1 = helloworld("item")
  assert result1 == "Hello item! Welcome to Hello World File!"
def length_test():
  result2 = helloworld("Stringtoolong")
  assert result2 == "Input string too long!"
def empty_test():
  result3 = helloworld("")
  assert result3 == "Input string is empty!"
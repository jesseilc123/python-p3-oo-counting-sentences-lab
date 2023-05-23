#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_string(self):
    return self._value

  def set_string(self, value):
    if type(value) != (str):
      print("The value must be a string.")
    else:
      self._value = value
    
  def is_sentence(self):
    if self.value[-1] != ".":
      return False
    else:
      return True
    
  def is_question(self):
    if self.value[-1] != "?":
      return False
    else:
      return True
    
  def is_exclamation(self):
    if self.value[-1] != "!":
      return False
    else:
      return True
    
  def count_sentences(self=""):
    noExclamtion = self.value.replace("!", " ")
    noQuestion = noExclamtion.replace("?", ".")
    finalList = noQuestion.split(".")
    for i in finalList:
      if i == "":
        finalList.remove(i)
    return len(finalList)

  
  value = property(get_string, set_string)
class StringUtility:
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    vowels = "aeioAEIOU"
    for char in self.string:
      if char in vowels:
        count += 1
      if count >= 5:
        return "many"
      else:
        return str(count)
    
  def bothEnds(self):
    string_count = len(self.string)
    string_count += len(self.string)
    if string_count >= 3:
      both_ends =  self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return both_ends
    else:
      return ""
      
  def fixStart(self):
    if len(self.string) <=1:
      return self.string
    first_letter = self.string[0]
    count = 0
    string1 = self.string
    for char in string1:
      if char == first_letter:
        count +=1
      if count <= 0:
        return self.string
      else:
        result = first_letter + string1.replace(first_letter, "*") [1: len(string1) + 1]
        return result

  def asciiSum(self):
    ascii_sum = 0
    for i in self.string:
      for chars in i:
        ascii_term = ord(chars)
      ascii_sum += ascii_term
    return ascii_sum

  def cipher(self):
    for i in self.string:
      for chars in i:
        ascii_term = ord(chars)
        ascii_term += 3
    for i in ascii_term:  
      chr (i)
    return ascii_term
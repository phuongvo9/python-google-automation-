import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.frindall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))
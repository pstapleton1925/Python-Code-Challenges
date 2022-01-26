import re 

class Main:

  def encrypt():

    word = input("\nType a word to encrypt\n\n").lower()

    #print("\nReversing your input...\n")
    word_rev = word[::-1]
    #print(word_rev, "\n")

    #print("Replacing your vowels...\n")
    def vowel_replace(wrod):
      wrod1 = re.sub("[aA]", "0", wrod)
      wrod2 = re.sub("[eE]", "1", wrod1)
      wrod3 = re.sub("[iI]", "2", wrod2)
      wrod4 = re.sub("[oO]", "2", wrod3)
      wrod5 = re.sub("[uU]", "3", wrod4)
      return wrod5
    wrod_nums = vowel_replace(word_rev)
    #print(wrod_nums, "\n")
    
    #print("Translating your instruments into vocals...\n")
    wrod_aca = wrod_nums + "aca"
    print(wrod_aca)

  encrypt()

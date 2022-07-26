list_of_words = ['he', 'she', 'He', 'She','man', 'woman', 'son', 'daughter', 'father', 'mother', 'brother', 'sister', 'boy', 'girl', 'lad', 'lass', 'sir', 'madam', 'Mr.', 'Miss', 'him', 'her', 'his', 'her', 'fellow', 'sister', 'sistership', 'sisterhood', 'men', 'women', 'lady', 'lord']

book = open("text_data.txt")
book_contents = book.read()
feminized_book = open("Feminized LOTR.txt", "a")
index = 0
while index < len(list_of_words):
  if index == 0:
    new_book = book_contents.replace(list_of_words[index], list_of_words[index + 1])
    index += 2
  else:
    new_book = new_book.replace(list_of_words[index], list_of_words[index + 1])
    index += 2
feminized_book.write(new_book)



  
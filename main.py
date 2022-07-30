from list_of_words import word_list
book = open("text_data.txt") #original transcript
book_contents = book.read()
feminized_book = open("Feminized LOTR.txt", "a")
index = 0
while index < len(word_list):
  if index == 0: #base case
    new_book = book_contents.replace(word_list[index], word_list[index + 1])
    index += 2 #words occur in pairs: a masculine and a feminine
  else:
    new_book = new_book.replace(word_list[index], word_list[index + 1]) #recursion to replace multiple words from the source material, one pair at a time
    index += 2
feminized_book.write(new_book)



  
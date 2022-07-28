list_of_words = [' he ', ' she ', 'He ', 'She ','man ', 'woman ', ' son ', ' daughter ', 'father', 'mother', 'brother', 'sister', 'boy', 'girl', ' lad ', ' lass ', 'sir', 'madam', 'Mr.', 'Miss', ' him ', ' her ', ' his ', ' her ', 'himself', 'herself', 'His', 'Her', 'fellow', 'sister', 'sistership', 'sisterhood', 'men ', 'women ', 'Men', 'Women', 'lady', 'lord', ' king', ' queen', 'prince ', 'princess ', 'Daddy', 'Mommy', 'Dad', 'Mom', 'beard ', 'hair ', 'uncle', 'aunt', 'Uncle', 'Aunt', 'nephew', 'niece', ' him,', ' her,', ' him?', ' her?', ' him:', ' her:', ' him;', ' her;', ' him.', ' her.', 'Him', 'Her', '(him ', '(her ', ' him)', ' her)', ' he,', ' she,', ' he?', ' she?', ' he:', ' she:', ' he;', 'she;', ' he.', ' she.', '(he ', '(she ', ' he)', ' she)', 'man,', 'woman,', 'man?', 'woman?', 'man;', 'woman;', 'man:', 'woman:', 'man.', 'woman.', 'man)', 'woman)', ' King', ' Queen', 'Lady', 'Lord', 'emperor', 'empress', 'Mrs.', 'Miss', ' son,', ' daughter,', ' sons', ' daughters', 'princes ', 'princesses ', ' lads ', ' lasses ', 'beards', 'hair']

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



  
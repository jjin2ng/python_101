#영문 기사를 2개 들고와서 공통으로 쓰인 단어를 가져오기

article1 = """Experts call for lifestyle change to reverse trend
By Kwak Yeon-soo
HONG KONG — In an alarming trend, millennials, born between 1981 and 1996, have become the subject of a paradox: they are facing a faster decline in health compared to older generations despite a heightened awareness of fitness among younger people.

This perplexing phenomenon, initially identified in the United States, is now resonating across major Asian countries, including Korea, Hong Kong and Singapore, countering conventional expectations that the health-savvy younger generation would enjoy increased longevity.

According to a 2020 study by medical insurer Blue Cross Blue Shield in the United States, millennials face an accelerated deterioration in both physical and mental health, with conditions such as hypertension, high cholesterol, depression, and anxiety disorders appearing at an earlier age compared to older generations.

For example, Korean millennials are positioned to outpace their parents in aging, Hong Kong is observing an alarming rise in age-related ailments, and the younger generation in Singapore finds itself susceptible to an accelerated decline in health."""



article2 = """Strategies for preserving health

Experts emphasize the importance of lifestyle changes for young adults to preserve and improve their health.

“The key to reversing accelerated aging depends on your lifestyle. You have to remodel your life and manage ‘intrinsic capacity’,” Jung said, referring to the overall combination of an individual’s physical and mental capacities.

He said this could be done through managing four “M’s”: mobility , medical issues` taking preventive measures such as eating healthy foods, being active and getting regular medical check-ups, mental activity practicing meditation and staying present-focused and focusing on what matters setting priorities in life.

Au Yeung stressed the importance of building muscles in order to “lower your chance of suffering from fractures when you grow old.”"""

words = article1.split()
setWords = set(words)

words2 = article2.split()
setWords2 = set(words2)

int = setWords.intersection(setWords2)
list_words = list(int)
list_words.sort()
print(list_words)
print(len(list_words)) # 글자 갯수


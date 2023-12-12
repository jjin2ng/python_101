article = """Experts call for lifestyle change to reverse trend
By Kwak Yeon-soo
HONG KONG — In an alarming trend, millennials, born between 1981 and 1996, have become the subject of a paradox: they are facing a faster decline in health compared to older generations despite a heightened awareness of fitness among younger people.

This perplexing phenomenon, initially identified in the United States, is now resonating across major Asian countries, including Korea, Hong Kong and Singapore, countering conventional expectations that the health-savvy younger generation would enjoy increased longevity.

According to a 2020 study by medical insurer Blue Cross Blue Shield in the United States, millennials face an accelerated deterioration in both physical and mental health, with conditions such as hypertension, high cholesterol, depression, and anxiety disorders appearing at an earlier age compared to older generations.

For example, Korean millennials are positioned to outpace their parents in aging, Hong Kong is observing an alarming rise in age-related ailments, and the younger generation in Singapore finds itself susceptible to an accelerated decline in health."""

words = article.split() #띄어쓰기 기준으로 나누는
words.sort() # 숫자부터 abcd 순서로 나열
setWrods = set(words)  #단어 리스트를 세트화 시킴
listedWords = list(setWrods) #리스트화 시킴
listedWords.sort()  # 오름차순 정리
print(listedWords)

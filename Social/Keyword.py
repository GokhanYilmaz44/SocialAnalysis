from collections import Counter
with open('keyword.csv','r') as myfile:
      texts=myfile.read().replace('\n','')

general_list = []
keyword = [tag.strip("#") for tag in texts.split() if tag.startswith("#")]
print(keyword)
general_list.extend(keyword)

#num_words = [len(sentence.split()) for sentence in list]
#print(num_words)
print(Counter(general_list))

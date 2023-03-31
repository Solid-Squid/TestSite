
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#1
print(sentence.replace("!" , " "))

#2
sentence_new = sentence.upper()
print(sentence_new.replace("!" , " "))

#3
print(sentence[44::-1])

#extra flavour
sentence_old = sentence_new.replace("!" , " ")
print(sentence_old[44::-1])
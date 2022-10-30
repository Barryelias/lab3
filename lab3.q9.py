def main():
    sentence = input("Enter a sentence: ")
    word_sentence = word.sentence()

    for word in range(0, len(word_sentence)):
        print(f"{word_sentence[word]} (length: {len(word_sentence[word])})")


main()        

    

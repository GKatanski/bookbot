def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_words_report = get_words(text)
    print(f"{num_words_report}")
    #print(sorted(num_words_report.items(), key = lambda items:items[1], reverse = True))
    num_of_letters = get_num_of_letters(text)
    print(num_of_letters)

    #print(sorted(num_words_report.items(), key = lambda items:items[1], reverse = True))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    counter_dictionary ={}
    words = text.split()
    for w in words:
        if w.lower() in counter_dictionary:
            counter_dictionary[w.lower()] +=1
        else:
            counter_dictionary[w.lower()] = 1
    return counter_dictionary

def get_num_of_letters(text):
    counter_dictionary = {}
    words = text.split()
    for w in words:
        for l in w:
            if l.lower() in counter_dictionary:
                counter_dictionary[l.lower()] +=1
            else:
                counter_dictionary[l.lower()] = 1
    return counter_dictionary

           

    

main()
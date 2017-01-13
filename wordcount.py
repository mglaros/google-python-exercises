import sys



def word_mapping(filename):
    f = open(filename)
    words = f.read()
    words_list = words.split()
    word_dictionary = {}
    for word in words_list:
        if word in word_dictionary.keys():
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    dictionary_print(word_dictionary)
            
            
def dictionary_print(d):
    for word in sorted(d, key=d.get, reverse=True):
        print word + ": " + "%s" %(d[word])
        
    
    
    
    
    
def main():
    word_mapping(sys.argv[1])
    

if __name__ == "__main__":
    main()
    
    
    

    
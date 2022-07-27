def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        # print(f"Sorry!, the {filename} does not exit")
        pass
    
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has {num_words} words")


filename = 'alice.txt'
count_words(filename)

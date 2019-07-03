def read_text():
    quotes = open("D:\github\UDACITY--Programming_Foundations_with_Python\Lesson05\Video04\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    
read_text()
import sqlifree


sql = sqlifree.prediction("With that done, all we have to do next is run the following command in the same directory ")

if sql:
    print("It's SQL Injection!")
else:
    print("It's not SQL Injection!")
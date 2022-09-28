#Team number: T046
#Version 1.0 - 06/12/2021
#Contributors:
#101220723 Abdullah Baseem
#101234882 Calvin Bramble
#101182813 Rola Elghonimy 
#101236768 Liam Beecham

from P5_T046_load_dataset import load_dataset

#function 1 - Abdullah Baseem
def print_dictionary_category(category :str, book_dict :dict) -> int:
    """
    Written By: 101220723 Abdullah Baseem
    
    Returns the number of books that are associated with the given category
    key. Also prints a string that says the details of each book within the
    the category.
    
    >>> print_dictionary_category('Business', book_dict))
    "The cateogry Business has 20 books. This is the list of books in the category Business:"
    {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'page_count': 224, 'language': 'English'}
    {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'page_count': 176, 'language': 'English'}
    Book 3 details
    ...
    Book 20 details
    """
    
    books_in_category = [] #makes an empty list which will contain the book details
    
    for i in book_dict: #sorts through the dictionary to look for the specified category
        if i == category:
            num_books = len(book_dict.get(i)) #gets the length of the list of books associated with the specified category and assigns num_books to that value
            for x in book_dict.get(i): #goes through the list of books associated with the specified category and adds them to the list that contains the book details
                books_in_category.append(x) 
    
    print("The cateogry ", category, " has ", num_books, " books. This is the list of books in the category ", category, ":", sep="")
    for i in books_in_category:
        print(i)

    return num_books

#function 2 - Abdullah Baseem
def add_book(book_dict :dict, book_details :tuple) -> dict:
    """ 
    Written By: 101220723 Abdullah Baseem
    
    This function adds a book with the specified details into the specified 
    dictionary "book_dict". After adding the book, it returns the updated 
    dictionary containing the new book and prints a message indicating that the 
    book has been added. If the book has not been added, due to a missing 
    argument within the details tuple, or due to the book already being in the
    dictionary, it prints an error message.
    
    book_details format: 
    ("title", "author", "rating", "publisher", "category", "page_count", "language")
    
    >>> add_book(book_dict, ("Harry Potter", "J.K Rowling", "5.0", "Bloomsbury Publishing", "Fiction", "1000", "English"))
    "The book has been added correctly"
    >>> add_book(book_dict, ("Harry Potter", "5.0", "Bloomsbury Publishing", "Fiction", "1000"))
    "There was an error adding the book."
    >>> add_book(book_dict, ("Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth", "T. Harv Eker", "4.6", "Harper Collins", "Business", "224", "English"))
    There was an error adding the book. The book already exists.
    """
    if len(book_details) == 7:
        book_details_dict = {} #makes an empty dictionary which will store all the book details
        book_details_dict["title"] = book_details[0]
        book_details_dict["author"] = book_details[1]
        if book_details[2] != '': book_details_dict["rating"] =  float(book_details[2]) #converts the rating to a float if it is not an empty string
        else: book_details_dict["rating"] = ''
        book_details_dict["publisher"] = book_details[3]
        book_details_dict["page_count"] = int(book_details[5]) #converts page count to an int
        book_details_dict["language"] = book_details[6]
        
        for i in book_dict: #loops through the specified dictionary to look for the category in which to add the book
            if i == book_details[4]: #adds the book to the list of books that are associated with the category provided
                compare_book = book_dict.get(i) 
                for x in compare_book: #checks to see if the book already exists within the specified category
                    if x == book_details_dict:
                        print("There was an error adding the book. The book already exists.")
                        return book_dict
                book_dict[i].append(book_details_dict)
                print("The book has been added correctly.")
    else:
        print("There was an error adding the book. Not enough details provided.")
   
    return book_dict

#function 3 - Abdullah Baseem
def remove_book(title :str, category :str, book_dict :dict) -> dict:
    """
    Written By: 101220723 Abdullah Baseem
    
    This funciton deletes the book with the title and category speicifed from
    the dictionary "book_dict" and prints a success message if the book was 
    removed or prints an error message if the book was not found. If the book
    is successfully deleted, it returns an updated dictionary and if it was not
    found/deleted, it returns the same dictionary.
    
    >>> remove_book("Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction", book_dict)
    "The book has been removed correctly."
    >>> remove_book("Rework", "Business", book_dict)
    "The book has been removed correctly."
    >>> remove_book("Rework", "Fiction", book_dict)
    "There was an error removing the book. Book not found."
    >>> remove_book("Kite runner", "Fiction", book_dict)
    "There was an error removing the book. Book not found."
    >>> remove_book("Kite runner", "Non-fiction", book_dict) #non-fiction is not a category within this dictionary
    "There was an error removing the book. Category not found."
    """
    
    for i in book_dict: #sorts through the dictionary to look for the specified category
        if i == category:
            temp_book_list = book_dict.get(i) #makes a temporary book list associated with the specified category so that it can be changed
            x = 0
            while x != len(temp_book_list): #iterates through the temporary book list and looks for the book that is to be deleted
                if x == len(temp_book_list) - 1 and temp_book_list[x]['title'] != title: #if x is at the final book, and the specified book is still not found, print the error message.
                    print("There was an error removing the book. Book not found.")
                    x += 1
                elif temp_book_list[x]['title'] == title: #if the specified book has been found:
                    del temp_book_list[x] #deletes the book from the temporary book list
                    print("The book has been removed correctly.") #prints success message
                    x = len(temp_book_list) #exits the while loop
                else:
                    x += 1 #if the book has not been found but x is not at the final book, increment x and keep going
            book_dict[i] = temp_book_list #update the value of the specified category by setting it equal to the temp book list that excludes the specified book
            return book_dict
    print("There was an error removing the book. Category not found.")
    return book_dict

#function 4 - Liam Beecham
def get_books_by_rate(rating: int, books: dict) -> list:
    """
    find the books with a rating between a given whole number and .9 higher and prints it so the reader can see
    >>>get_books_by_rate(3,books)
    title (title of book)
    author (author of book)
    rating (between 3 and 3.9)
    publisher (Publisher of book)
    page_count (length of book)
    language (language book is written in)
    """
    quality_book = []

    for genre in books:
        book = books.get(genre)
        for current_book in book:

            if current_book['rating'] != '' and rating <= current_book['rating'] < rating + 1:
                quality_book.append(current_book)
    for book in quality_book:
        for key, value in book.items():
            print(key, value)   
        print('\r')
    return quality_book


#function 5 - Liam Beecham
def find_books_by_title(title: str, dictionary: dict) -> bool:
    """
    Written by: 101236768 Liam Beecham
     
    iterates through the dictionary and finds a matching title
    >>>find_books_by_title("book title", dictionary)
    if the book exists
    The book has been found.
    if the book does not exist
    The book has not been found
    """
    for genre in dictionary:
        books = dictionary.get(genre)
        for current_book in books:
            if title == current_book['title']:
                print("The book has been found")
                return True
    print("The book has NOT been found")
    return False

#function 6 - Liam Beecham
def get_books_by_author(author: str, dictionary: dict) -> list:
    """
    Written by: 101236768 Liam Beecham
     
    Searches dictionary for all books by one author and prints out the book information
    >>>get_books_by_author("author", dictionary)
    The author has "author" has published the following work
    1 - book1
    2 - book2
    3 - book3
    """
    books_written = []
    for genre in dictionary:
        books = dictionary.get(genre)
        for current_book in books:
            if author == current_book['author']:
                books_written.append(current_book)

    unique_books = []
    for book in books_written:
        if book not in unique_books:
            unique_books.append(book)

    print("The author", author, "has published the following books")
    i = 1
    book_title = []
    for book in unique_books:
        book_title.append(book['title'])
        print(i, "-", book['title'])
        i += 1
    return book_title

#function 7 - Calvin Bramble
def get_books_by_publisher(pub:str, dictionary:object) -> list:
    """
    Written By: Calvin Bramble 101234882
    
    Returns all the books published by a certain publisher
    >>>get_books_by_publisher("Vintage Crime/Black Lizard", google_books_dataset)
    The publisher "Vintage Crime/Black Lizard" has published the following books:
	1- The Girl in the Spider's Web: A Lisbeth Salander novel, continuing Stieg Larsson's Millennium Series
    ["The Girl in the Spider's Web: A Lisbeth Salander novel, continuing Stieg Larsson's Millennium Series"]
    >>>get_books_by_publisher("Random House", google_books_dataset)
    The publisher "Random House" has published the following books:
	1- Happy: Why More or Less Everything is Absolutely Fine
	2- The Power of Habit: Why We Do What We Do in Life and Business
    ['The Power of Habit: Why We Do What We Do in Life and Business', 'Happy: Why More or Less Everything is Absolutely Fine']
    >>>get_books_by_publisher("DC Comics", google_books_dataset)
    The publisher "DC Comics" has published the following books:
	1- Watchmen (2019 Edition)
    ['Watchmen (2019 Edition)']
    """
    booklist = []
    
    #Creates the list of books by the given publisher
    for key in dictionary.keys(): #Loops over every key in the dictionary
        for book in dictionary.get(key): #Loops over every book
            if book.get("title") not in booklist: #Prevents adding duplicates
                if book.get("publisher") == pub: #Checks if the book is by the correct publisher
                    booklist.append(book.get("title")) #Adds the book to the list 
    
    
    #Prints the books by the given publisher.
    print_count = 1
    print('The publisher'+ ' "' + str(pub) + '" ' + 'has published the following books:')
    for title in booklist:
        print("\t" + str(print_count) + "- " + str(title))
        print_count += 1
    
    return booklist

#function 8 - Calvin Bramble
def check_category_and_title(category:str, title:str, dictionary:object) -> bool:
    """
    Written by: Calvin Bramble 101234882
    
    Returns True if the book is in the given cattegory and false if not
    >>>check_category_and_title("Business", "The Essentials of Finance and Accounting for Nonfinancial Managers", google_books_dataset)
    The category Business has the book title The Essentials of Finance and Accounting for Nonfinancial Managers.
    True
    >>>check_category_and_title("Economics", "The Mysterious Affair at Styles", google_books_dataset)
    The category Economics does not have the book title The Mysterious Affair at Styles.
    False
    >>>check_category_and_title("Mythical Creatures","Sword of Destiny: Witcher 2: Tales of the Witcher", google_books_dataset)
    The category Mythical Creatures has the book title Sword of Destiny: Witcher 2: Tales of the Witcher.
    True
    """
    for key in dictionary.keys(): #Loops over every key
        for book in dictionary.get(key): #Loops over every book 
            if book.get("title") == title: #Checks if the book has the correct title
                if key == category: #Checks if the book is of the correct cattegory
                    #Prints the book info if both criteria are met
                    print("The category " + str(category) + " has the book title " + str(title) + ".")
                    return True
                
    #prints that the book did not meet all the criteria
    print("The category " + str(category) + " does not have the book title " + str(title) + ".")
    return False

#function 9 - Calvin Bramble
def all_categories_for_book_title (title:str, dictionary:object) -> list:
    """
    Written By: Calvin Bramble 101234882
    
    Returns all the categories for a given book title 
    >>>all_categories_for_book_title("Sword of Destiny: Witcher 2: Tales of the Witcher", google_books_dataset)
    The book title"Sword of Destiny: Witcher 2: Tales of the Witcher"has the following categories:

	1- Fiction
	2- Adventure
	3- Mythical Creatures
    ['Fiction', 'Adventure', 'Mythical Creatures']
    >>>all_categories_for_book_title("No One Is Too Small to Make a Difference", google_books_dataset)
    The book title"No One Is Too Small to Make a Difference"has the following categories:

	1- Biography
    ['Biography']
    >>>all_categories_for_book_title("The Way Of Shadows: Book 1 of the Night Angel", google_books_dataset)
    The book title"The Way Of Shadows: Book 1 of the Night Angel"has the following categories:

	1- Fantasy
	2- Adventure
	3- Epic
    ['Fantasy', 'Adventure', 'Epic']
    """
    #Defines needed objects for the function
    cat_list = []
    counter = 1
    
    #Prints the header
    print("The book title" + '"' + str(title) + '"' + "has the following categories:")
    print()
    
    #Finds and prints all the categories for the given book
    for key in dictionary.keys(): #Loops over every key
        for book in dictionary.get(key): #Loops over every book
            if book.get("title") == title: #Checks if the book has the correct title
                print("\t" + str(counter) + "- " + str(key))
                cat_list += [key] #Adds the genere to the list of categories
                counter += 1 #Updates the counter for the genere
    return cat_list

#function 10 - Rola Elghonimy
def get_books_by_category(category : str, dictionary: dict) -> list:
    
    """   
    Written by: 101182813 Rola Elghonimy 
    
    returns a list of the book titles for the given category 'category' in the dictionary 'dictionary'
    
    >>>P5_T046_load_dataset.get_books_by_category("Adventure", T046_P1_load_data.load_dataset("Google_Books_Dataset.csv"))
    The follwing books are in: Adventure
    1-Sword of Destiny: Witcher 2: Tales of the Witcher
    2-A Feast for Crows (A Song of Ice and Fire, Book 4)
    3-After Anna
    4-The Way Of Shadows: Book 1 of the Night Angel
    5-A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    6-Edgedancer: From the Stormlight Archive
    7-The Malady and Other Stories: An Andrzej Sapkowski Sampler
    
    >>>P5_T046_load_dataset.get_books_by_category("Scifi", P5_T046_load_dataset.load_dataset("Google_Books_Dataset.csv"))
    No books in category: Scifi
    
    
    """
    
    titles = []
    if (category not in dictionary):
        print("No books in category:", category)
    else:
        print("The follwing books are in:", category)
        count = 1
        for book_obj in dictionary[category]:
            titles.append(book_obj["title"])
            print(str(count)+"-"+book_obj["title"])
            count += 1
    return titles

#function 11 - Rola Elghonimy
def get_books_by_category_and_rate(category : str, rate : int, dictionary : dict) -> list:
    """
    Written by: 101182813 Rola Elghonimy 
    
    returns a list of book titles for the given category 'category' and rate interval 'rate'
    
    >>> P5_T046_load_dataset.get_books_by_category_and_rate('Fiction', 3, P5_T046_load_dataset.load_dataset("Google_Books_Dataset.csv"))
    The follwing books are in: Fiction with a rate of 3
    1-Antiques Roadkill: A Trash 'n' Treasures Mystery
    2-Bring Me Back
    3-Mrs. Pollifax Unveiled
    
    >>> P5_T046_load_dataset.get_books_by_category_and_rate('Scifi', 3, P5_T046_load_dataset.load_dataset("Google_Books_Dataset.csv"))
    No books in category: Scifi
    No books in category: Scifi with a rate of 3
    
    >>> P5_T046_load_dataset.get_books_by_category_and_rate('Fiction', 87, P5_T046_load_dataset.load_dataset("Google_Books_Dataset.csv"))
    No books in category: Fiction with a rate of 87
    
    """
    
    titles = []

    header = True
    if (category not in dictionary) :
        
        print("No books in category:", category)
        
    else:
        
        count = 1
        for book_obj in dictionary[category]:
            if book_obj['rating'] != '' and rate <= float(book_obj['rating']) < rate + 1:
                titles.append(book_obj["title"])
                count += 1
                if header:
                    print("The follwing books are in:", category, "with a rate of", rate)
                    header = False
                print(str(count)+"-"+book_obj["title"])
                
                
    if (len(titles) == 0):
        print("No books in category:", category, "with a rate of", rate)
    
    return titles

#function 12 - Rola Elghonimy
def get_author_categories(author: str, dictionary: dict) -> list:
    """
    Written by: 101182813 Rola Elghonimy 
    
    returns a list of categories for the given author 'author' in the dictionary 'dictionary'
    
    >>>P5_T046_load_dataset.get_author_categories("Blake Pierce", P5_T046_load_dataset.load_dataset("Google_Books_Dataset.csv"))
    The follwing auhor: Blake Pierce has published books under the following category
    1 Fiction
    2 Detective
    3 Thrillers
    4 Mystery
    
    >>>P5_T046_load_dataset.get_author_categories("Bob", P5_T046_load_dataset.load_dataset("Google_Books_Dataset.csv"))
    No books under author: Bob
    

    """
    categories = []
    count = 0
    header = True
     
   
    for category in dictionary.keys():
        for book in dictionary[category]:
            if book["author"] == author and not (category in categories):
                count += 1
                categories += [category]
                if header == True:
                    print("The follwing auhor:", author, "has published books under the following category")
                    header = False
                print(count, categories[count - 1])    
                
    if len(categories) == 0:
        print("No books under author:", author) 
    return categories

# Team number: T046
# Version 1.0 - 06/12/2021
# Contributors:
# 101220723 Abdullah Baseem
# 101234882 Calvin Bramble
# 101182813 Rola Elghonimy
# 101236768 Liam Beecham

from P5_T046_load_dataset import load_dataset
from T046_P2_search_modify_dataset import *
from T046_P3_sorting import *


# function definitions
def displayMenu() -> str:
    """
    Written By: 101220723 Liam Beecham
    
    Displays all the commands and asks for and returns the user input.
    
    >>> displayMenu()
    1- Command Line L)oad file
    2- Command Line A)dd book
    3- Command Line R)emove book
    4- Command Line F)ind book by title
    5- Command Line NC) Number of books in a category
    6- Command Line CA) Categories for an author
    7- Command Line CB) Categories for a book title
    8- Command Line G)et book
	R)ate   A)uthor   P)ublisher   C)ategory   CT) Category and Title   CR) Category and Rate
    9- Command Line S)ort book
	T)itle   R)ate   P)ublisher   C)ategory   PA)ageCount
    10- Command line Q)uit
    :
    """
    print("\n\t1- Command Line L)oad file", "\t2- Command Line A)dd book", "\t3- Command Line R)emove book",
          "\t4- Command Line F)ind book by title", "\t5- Command Line NC) Number of books in a category",
          "\t6- Command Line CA) Categories for an author", "\t7- Command Line CB) Categories for a book title",
          "\t8- Command Line G)et book",
          "\t\tR)ate   A)uthor   P)ublisher   C)ategory   CT) Category and Title   CR) Category and Rate",
          "\t9- Command Line S)ort book", "\t\tT)itle   R)ate   P)ublisher   C)ategory   PA)ageCount",
          "\t10- Command line Q)uit", sep='\n')

    command = input(": ")

    return command.upper() #converts lowercase commands to uppercase to account for both


def funcAddBook(book_dict: dict):
    """
    Written By: 101220723 Abdullah Baseem
    
    Displays the prompts for adding a book to the dictionary and runs the
    add_book function with the inputs provided.
    
    >>> funcAddBook(book_dict)
    Please enter the title of the book: Harry Potter
    Please enter the author of the book: JK Rowling
    Please enter the rating of the book: 5.0
    Please enter the publisher of the book: Bloomsbury
    Please enter the genere of the book: Fiction
    Please enter the page count of the book: 1000
    Please enter the language of the book: English
    The book has been added correctly.
    """

    title = input("Please enter the title of the book: ")
    author = input("Please enter the author of the book: ")
    rating = input("Please enter the rating of the book: ")
    publisher = input("Please enter the publisher of the book: ")
    genere = input("Please enter the genere of the book: ")
    page_count = input("Please enter the page count of the book: ")
    language = input("Please enter the language of the book: ")

    book_info = title + ',' + author + ',' + rating + ',' + publisher + ',' + genere + ',' + page_count + ',' + language
    #combines all the info into the format required for the add_book function
    add_book(book_dict, tuple(book_info.split(',')))


def funcRemoveBook(book_dict: dict):
    """
    Written By: 101220723 Abdullah Baseem
    
    Displays the prompts for removing a book and runs the remove_book function 
    with the input provided.
    
    >>> funcRemoveBook(book_dict)
    Please enter the title of the book you wish to remove: Antiques Roadkill: A Trash 'n' Treasures Mystery
    Please enter the category of the book: Fiction
    The book has been removed correctly.
    """

    book_title = input("Please enter the title of the book you wish to remove: ")
    book_category = input("Please enter the category of the book: ")
    remove_book(book_title, book_category, book_dict)


def funcFindBookTitle(book_dict: dict):
    """
    Written By: 101220723 Abdullah Baseem
    
    Displays the prompt for finding the book in the given dictionary and runs 
    the function find_books_by_title with the input provided.
    
    >>> funcFindBookTitle(book_dict)
    Please enter the title of the book you wish to find: Rework
    The book has been found.
    """

    book_title = input("Please enter the title of the book you wish to find: ")
    find_books_by_title(book_title, book_dict)


def funcNumberOfBooksCategory(book_dict: dict):
    """
    Written by: 101236768 Liam Beecham
    """
    category = input("Please enter the category you wish to search for: ")
    get_books_by_category(category, book_dict)


def funcCategoryByAuthor(book_dict: dict):
    """
    Written by: 101236768 Liam Beecham
    """
    author = input("Which author do you wish to search for: ")
    get_author_categories(author, book_dict)


def funcCategoryForBookTitle(book_dict: dict):
    """
    Written by: 101236768 Liam Beecham
    """
    title = input("which book would you like to look up: ")
    all_categories_for_book_title(title, book_dict)


def funcGetBook(book_dict: dict):
    """
    Written by: 101182813 Rola Elghonimy 
    
    Prompts user to to enter subcommand to get the book the user requests by
    rate, author, publisher, category, category and title or category and rate
    and then calls the specified function based on their input 
    
    >>>8- Command Line G)et book
    R)ate   A)uthor   P)ublisher   C)ategory   CT) Category and Title   CR) Category and Rate 10- Command Line Q)uit
    : g
    
    Please enter the subcommand you wish to use: cr
    Please enter the category you wish to use: Fiction
    Please enter the rate you wish to use: 3
    The follwing books are in: Fiction with a rate of 3.0
    2-Antiques Roadkill: A Trash 'n' Treasures Mystery
    3-Bring Me Back
    4-Mrs. Pollifax Unveiled
    
    
    >>> 8- Command Line G)et book
    R)ate   A)uthor   P)ublisher   C)ategory   CT) Category and Title   CR) Category and Rate 10- Command Line Q)uit
    : g
    Please enter the subcommand you wish to use: cr
    Please enter the category you wish to use: Aventure
    Please enter the rate you wish to use: 3
    No books in category: Aventure
    No books in category: Aventure with a rate of 3.0
    []
        
    
    
    >>> 8- Command Line G)et book
    R)ate   A)uthor   P)ublisher   C)ategory   CT) Category and Title   CR) Category and Rate10- Command Line Q)uit
    : g
        Please enter the subcommand you wish to use: r
        Please enter the rate you wish to use: 3
    title Antiques Roadkill: A Trash 'n' Treasures Mystery
    author Barbara Allan
    rating 3.3
    publisher Kensington Publishing Corp.
    page_count 288
    language English

    title Bring Me Back
    author B A Paris
    rating 3.8
    publisher HarperCollins UK
    page_count 368
    language English
    
    title Mrs. Pollifax Unveiled
    author Dorothy Gilman
    rating 3.9
    publisher Ballantine Books
    page_count 208
    language English
    
    ... continued ...
    """
    subcom = ["R", "A", "P", "C", "CT", "CR"]

    subcommand = (input("Please enter the subcommand you wish to use: ")).upper()

    if subcommand not in subcom:
        print("No such command")

    if subcommand == "R":
        rate = float(input("Please enter the rate you wish to use: "))
        get_books_by_rate(rate, book_dict)
    if subcommand == "A":
        author = input("Please enter the author you wish to use: ")
        get_books_by_author(author, book_dict)
    if subcommand == "P":
        publisher = input("Please enter the publisher you wish to use: ")
        get_books_by_publisher(publisher, book_dict)
    if subcommand == "C":
        category = input("Please enter the category you wish to use: ")
        get_books_by_category(category, book_dict)
    if subcommand == "CT":
        category = input("Please enter the category you wish to use: ")
        title = input("Please enter the title you wish to use: ")
        check_category_and_title(category, title, book_dict)
    if subcommand == "CR":
        category = input("Please enter the category you wish to use: ")
        rate = float(input("Please enter the rate you wish to use: "))
        get_books_by_category_and_rate(category, rate, book_dict)


def funcSort(book_dict: dict):
    """
    Written By: Calvin Bramble 101234882
    
    Prompts user to to enter subcommand and runs the desied functions based
    on their input
    
    >>> funcSort(book_dict)
    ["T", "R", "P", "C", "PA"] (insert subcommand letter)
    """

    subcommands = ["T", "R", "P", "C", "PA"]

    subcommand = input("Please enter the subcommand you wish to use: ").upper()

    if subcommand not in subcommands:
        print("No such command")

    if subcommand == "T":
        sort_books_title(book_dict)
    if subcommand == "R":
        order = input("Please specify Ascending or Descending Rate (A or D)\n: ").upper()
        if order == "D":
            sort_books_descending_rate(book_dict)
        if order == "A":
            sort_books_ascending_rate(book_dict)
    if subcommand == "P":
        sort_books_publisher(book_dict)
    if subcommand == "C":
        sort_books_category(book_dict)
    if subcommand == "PA":
        sort_books_pageCount(book_dict)

#main script
book_dict = None #no file loaded
command_dict = {'A': funcAddBook, 'R': funcRemoveBook, 'F': funcFindBookTitle, 'NC': funcNumberOfBooksCategory,
                'CA': funcCategoryByAuthor, 'CB': funcCategoryForBookTitle, 'G': funcGetBook,
                'S': funcSort} #makes the command dictionary to call the functions depending on the command
command = displayMenu() #displays the menu initially
while command != 'Q': #run loop until command is Q and user wants to quit
    if command == "L": #load file
        filename = input("Please Enter the name of the csv file to load (include the extension): ")
        if ".csv" in filename: #if file is not a csv file, ask again
            book_dict = load_dataset(filename)
        else: print("Please enter a proper filename")
    elif book_dict: #if book_dict == True (if the book is loaded)
        if command in command_dict: command_dict[command](book_dict) #if the command is in the dictionary, run the corresponding function
        else: print("no such command.")
    else: print("No file loaded.")
    command = displayMenu() #display the menu again after the loop

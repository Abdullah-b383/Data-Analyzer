ECO1042 Fall 2021 README for Data Analyzer Project Version 1.0 10/12/2021

The project can be reached at:<br>
Website: https://carleton.ca/<br>
Email: abdullahbaseem@cmail.carleton.ca

# Description:
The project edits, searches, and sorts through a dictionary provided by the user. The specific command to be used it determined by prompting the user for their choice through a user interface.

The project is made up of four files:
  - T046_P4_booksUI.py (main file to run)
  - T046_P3_sorting.py
  - T046_P2_search_modify_dataset.py
  - P5_T046_load_dataset.py

# Installation:
Python 3.7.4 or later must be installed.<br>
Only built in Python modules are used. No external modules are required.

# Usage:
**> python T046_P4_booksUI.py**

You will be prompted with a user interface with 10 commands. If Q (quit) is entered as a command, the program will stop. On the first run, if a command other than L (load) or Q (quit) is entered, the program will re-prompt until a file is first loaded. If a non-.csv file is loaded, the program will re-prompt until a .csv file is loaded. Once the file is loaded, the program will convert it into a dictionary and any of the other commands can now be used. The commands are also error-checked so that if a lower case command is entered, the program will run as normal. Additonally, the command names are self explanatory and can be seen through the user interface.
 
After running the **bolded** line in the shell, this inteface will be displayed:

1- Command Line L)oad file<br>
2- Command Line A)dd book<br>
3- Command Line R)emove book<br>
4- Command Line F)ind book by title<br>
5- Command Line NC) Number of books in a category<br>
6- Command Line CA) Categories for an author<br>
7- Command Line CB) Categories for a book title<br>
8- Command Line G)et book<br>
	&emsp; &emsp; R)ate &emsp; A)uthor &emsp; P)ublisher &emsp; C)ategory &emsp; CT) Category and Title &emsp; CR) Category and Rate<br>
9- Command Line S)ort book<br>
	&emsp; &emsp; T)itle &emsp; R)ate &emsp; P)ublisher &emsp; C)ategory &emsp; PA)ageCount<br>
10- Command line Q)uit<br>
: 

The command is to be typed in after the colon.

# Credits:

### For the file T046_P4_booksUI.py:
- Liam Beecham - the author of the functions: 
  - _displayMenu_
  - _funcNumberOfBooksCategory_
  - _funcCategoryByAuthor_
  -  _funcCategoryForBookTitle_
- Abdllah Baseem - the author of the functions: 
  - _funcAddBook_
  - _funcRemoveBook_
  - _funcFindBookTitle_
- Rola Elgonimy - the author of the function:
  - _funcGetBook_
- Calvin Bramble - the author of the function: 
  - _funcSort_

*_The main script of the file was a collective effort, contributed to by each of the aforementioned authors._

### For the file T046_P3_sorting.py:
- Liam Beecham - the author of the functions: 
  - _sort_books_ascending_rate_
  - _sort_books_descending_rate_
- Abdllah Baseem - the author of the functions: 
  - _dict_to_list_load_data_
  - _sort_books_title_
  - _sort_books_category_
- Rola Elgonimy - the author of the function: 
  - _sort_books_publisher_
- Calvin Bramble - the author of the function: 
  - _sort_books_pageCount_

### For the file T046_P2_search_modify_dataset.py:
- Liam Beecham - the author of the functions:
  - _get_books_by_rate_
  - _find_books_by_title_
  - _get_books_by_author_
- Abdllah Baseem - the author of the functions:
  - _print_dictionary_category_
  - _add_book_
  - _remove_book_
- Rola Elgonimy - the author of the functions: 
  - _get_books_by_category_
  - _get_books_by_category_and_rate_
  - _get_author_categories_
- Calvin Bramble - the author of the functions:
   - _get_books_by_publisher_
   - _check_category_and_title_
   - _all_categories_for_book_title_

### For the file P5_T046_load_dataset.py:
- Rola Elgonimy - the author of the function: 
  - _load_dataset_

*_This function was reviewed and edited by Liam Beecham, Abdullah Baseem, and Calvin Bramble_

Copyright 2021 Abdullah Baseem, Liam Beecham, Rola Elghonimy, and Calvin Bramble (Team T046). All rights reserved.

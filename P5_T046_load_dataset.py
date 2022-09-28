# T046
# Version 1.0 - 06/12/2021
#Contributors:
# Written by Rola Elghonimy 101182813
# reviewed by Liam Beecham 101236768
# reviewed by Abdullah Basseem 101220723 
# reviewed by Calvin Bramble 101234882
    
import csv
    
def load_dataset(filename: str) -> dict:
    """
        returns a dictionary with each of the genres as keys with their
        corresponding values as lists of dictionaries when given a csv file
        precondition: filename has to be a csv file 
        >>>T46_P1_case1.book_category_dictionary_list(filename)
        {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery",
        'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington
        Publishing Corp.', 'page_count': 288, 'language': 'English'}, ...
    """
    
    big_dict = {}  # creates a big dictionary with each of the genres as keys with their
    # corresponding values as lists of dictionaries.
    
    infile = open(filename, 'r')
    file_d = csv.DictReader(infile)
    
    for dict in file_d:
        if dict['generes'] not in big_dict:
            big_dict[dict['generes']] = []
    
        if dict.get('rating') != "":
            dict['rating'] = float(dict.get('rating', 0))
            # converts rating into a float if string is not empty
    
        if dict.get('page_count') != '':
            dict["page_count"] = int(dict.get('page_count', 0))
            # converts page count into a float if sting is not empty
    
        
        # Checking that the genre of the book is in big_dict (as precaution)
        if dict.get('generes') in big_dict:
                # Saving the genre of the book
            genre = dict.get('generes')
                # Deleting the key,value pair of generes in the dict
            del dict['generes']
                # Deleting the first column of the cvs file
            del dict[""]
        if dict not in big_dict[genre]:
                # Appending the dictionary to the corresponding list in the dictionary
            big_dict[genre].append(dict)
        
    return big_dict  



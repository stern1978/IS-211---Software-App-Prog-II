#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 - Assignment 2"""

class Book(object):
    """Collection of books"""
    
    author = ''
    title = ''

    def __init__(self, author, title):
        """Constructs a book.

        Args:
            author (str): name of Author
            title (str): title of Book
        """
        self.author = author
        self.title = title

    def display(self):
        """Formats and displays results of a book."""
        display_out = '{}, written by author {}'.format(self.title, self.author)
        print display_out

book1 = Book('John Steinbeck', 'Of Mice and Men')
book2 = Book('Harper Lee','To Kill a Mockingbird')

book1.display()
book2.display()

#!user/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def data():
    ''' ''' 
    userInput = None

    try:
        while userInput != -1:
            userInput = raw_input('\nPlease input a person\'s ID number: ')
            userInput2 = userInput
            con = lite.connect('pets.db')
            cur = con.cursor()
            cur2 = con.cursor()
            cur.execute('SELECT first_name, last_name, age FROM'
                        ' person WHERE id = ?', (userInput))

            cur2.execute('SELECT pet.name, pet.breed, pet.age, pet.dead '
                         'FROM pet '
                         'INNER JOIN person_pet '
                         'ON pet.id = person_pet.pet_id '
                         'INNER JOIN person '
                         'ON person_pet.person_id = person.id '
                         'WHERE person.id = ?', (userInput))

            rows = cur.fetchall()
            rows2 = cur2.fetchall()
            #print rows
            #print rows2
            print '\n{} {} is {} years old.'.format(rows[0][0], rows[0][1], rows[0][2])
            for pet in rows2:

                if rows2[0][3] == 1:
                    print '{} {} owned a {} named {}, who was {} years old.'.format(rows[0][0], rows[0][1], pet[0], pet[1], pet[2])
                else:
                    print '{} {} owns a {} named {}, who is {} years old.'.format(rows[0][0], rows[0][1], pet[0], pet[1], pet[2])
                con.commit()

    except IndexError:
        print '\nIndex out of range please try again!\n'
        data()
    except:
        print '\nFatal error program had to close.'
        sys.exit

if __name__ == '__main__':
    data()

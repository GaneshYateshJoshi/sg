import os
from src.main import main

def generator():
    '''To generate the schema for us'''
    sr = input('Enter your source of json file> ')
    dis = input('Enter your destination for .db file> ')
    main(sr, dis)

if __name__ == '__main__':
    generator()

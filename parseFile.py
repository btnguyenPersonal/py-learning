#!/usr/bin/env python

file = open('settings.txt', 'r')
print(file.read())
file.close()
file = open('settings.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
file = open('settings.txt', 'r')
print(file.readlines())
file.close()
    

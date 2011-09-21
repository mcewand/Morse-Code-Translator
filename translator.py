#!/usr/bin/python

# -*- coding: utf-8 -*-

#convert a string of input text to morse code
import serial

#morse code array
morseDict = {
  	'a':'13',
		'b':'3111',
		'c':'3131',
		'd':'311',
		'e':'1',
		'f':'1131',
		'g':'331',
		'h':'1111',
		'i':'11',
		'j':'1333',
		'k':'313',
		'l':'1311',
		'm':'33',
		'n':'31',
		'o':'333',
		'p':'1331',
		'q':'3313',
		'r':'131',
		's':'111',
		't':'3',
		'u':'113',
		'v':'1113',
		'w':'133',
		'x':'3113',
		'y':'3133',
		'z':'3311',
		' ':'00000',
		}
text = raw_input('Please enter your string:\n')
text_div = list(text)
for item in text_div:
	if (item == ' '):
		item = '0'
#print text_div
morse_list = list()
for char in text:
	for key in morseDict:
		if (char.lower() == key):
			value = morseDict[key]
			morse_list.append(value)
#print morse_list
morse_out = '0'
for item in morse_list:
	morse_out = morse_out + item + '0'
print 'Your text string in Morse Code is: \n' 
print morse_out

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:30:52 2021

@author: Reed Riggs

Title: Chinese Tokenizer
Note: This is modified from Kris Kyle's tutorial
Link: https://kristopherkyle.github.io/corpus-analysis-python/Python_Tutorial_4.html
"""

def tokenize(input_string):
	tokenized = [] #empty list that will be returned

	#these are normal Chinese punctuation characters
	punct_list = ["。", "？", "！", "，", "、", "‘", "“"]

	#no items to replace with spaces
	#replace_list = ["\n","\t"]

	#This is a list of items to ignore
	ignore_list = ["。", "？", "！", "，", "、", "‘", "“", "\n", "\t"]

	#iterate through the punctuation list and replace each item with a space + the item
	#for x in punct_list:
		#input_string = input_string.replace(x," " + x)

	#iterate through the replace list and replace it with a space
	for x in replace_list:
		input_string = input_string.replace(x," ")

	#our source texts will be in Chinese, so no need to lower them
	#input_string = input_string.lower()

	#then we split the string into a list
	input_list = input_string.split(" ")

	#finally, we ignore unwanted items
	for x in input_list:
		if x not in ignore_list: #if item is not in the ignore list
			tokenized.append(x) #add it to the list "tokenized"

	#Then, we return the list
	return(tokenized)
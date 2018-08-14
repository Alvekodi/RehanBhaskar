import os
import sys
import re
import xlrd
import xlwt

base_path = os.path.dirname(os.path.realpath(__file__))
print("The Current Running Directory: ", base_path)

file_parse_directory = "\\\\btc7n001\\PH\\SDE\\2018\\SprintReports\\Nagaraj\\Rums_Update\\standup.xlsx"
print("XL file to Parse: ", file_parse_directory)


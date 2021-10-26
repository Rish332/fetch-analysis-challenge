import gzip
import shutil
import os
import pandas as pd
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
from ast import literal_eval
import json
from datetime import datetime
from sqlalchemy import create_engine
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# def replace(file_path, pattern, subst):
#     #Create temp file
#     fh, abs_path = mkstemp()
#     with fdopen(fh,'w') as new_file:
#         with open(file_path) as old_file:
#             for line in old_file:
#                 new_file.write(line.replace(pattern, subst))
#     #Remove original file
#     remove(file_path)
#     #Move new file
#     move(abs_path, file_path)
for files in os.listdir():
    if 'json' in files:
        with gzip.open(files, 'rb') as file_input:
            with open(files.replace('.gz', ''), 'wb') as file_output:
                shutil.copyfileobj(file_input, file_output)





# replace('', '{"_id"', ',{"_id"')
# receipts_data = pd.read_json('receipts.json', lines=True)
# brands_data = pd.read_json('brands.json', lines=True)
# users_data = pd.read_json('users.json', lines=True)
#
# print(receipts_data.head())

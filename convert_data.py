import os
import re
import glob
import pandas as pd

os.chdir("./data/raw_data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for f in all_filenames:
    df = pd.read_csv(f, header=None)
    df['source'] = f
    os.makedirs('../proc_tmp', exist_ok=True)
    df.to_csv(f'../proc_tmp/{f}.csv', index=True)

os.chdir("../../data/proc_tmp")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, header=None) for f in all_filenames])
combined_csv = combined_csv[[2, 3, 4]]
combined_csv.columns = ['text', 'outcome', 'source']
combined_csv = combined_csv[combined_csv['text'] != '1'].reset_index(drop=True)
combined_csv = combined_csv.sort_values(by=['outcome', 'source', 'text']).reset_index(drop=True)
classes = combined_csv['outcome'].unique()

# get the distinct classes
# for each class, create a file with that line of text and name it as the original file name, f

# export to file
os.makedirs('../train', exist_ok=True)
# combined_csv.to_csv(f'../train/train_data.csv', index=False)
for c in classes:
    c = re.sub(r'\s+', '', c)
    os.makedirs('../train/{}'.format(c), exist_ok=True)
    for index, data in combined_csv.iterrows():
        source = re.sub(r'\s+', '', data['source'])
        source = re.sub(r'.csv', '', source)
        filename = '../train/{}/{}-{}.txt'.format(c, source, index)
        with open(filename, 'w+') as f:
            f.write(data['text'])

# print(combined_csv.columns)
# print(classes)
# print(os.getcwd())
# print(combined_csv)
# print(combined_csv.groupby(combined_csv.columns.tolist(), as_index=False).size())



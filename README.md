1. Clone the repository from the provided GitHub link.
2. Wordnet should be installed before running the files. 
3. Place the input text file in the data folder.
4. The input file format should be 1 sentence per line. Refer existing data files for reference.
5. The output file will be generated in the same data folder with the prefix eda_ to the input file name.
6. Execute the augment.py file. 
7. The only input argument need to be provided is the input file name.
8. Sample execution command for reference: 
python augment.py --input=self_data.txt
9. Code modified to execute only synonym replacement.
10. Removed 0/1 sentiments.
11. All augmented sentences per sentence are combined and shuffled.

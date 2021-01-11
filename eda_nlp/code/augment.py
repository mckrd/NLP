# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou

from eda import *

#arguments to be parsed from command line
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="input file of unaugmented data")
args = ap.parse_args()

output = None
from os.path import dirname, basename, join
output = join(dirname(args.input), 'eda_' + basename(args.input))

#how much to replace each word by synonyms
alpha_sr = 0.1#default

#generate more data with standard augmentation
def gen_eda(train_orig, output_file, alpha_sr):

    writer = open(output_file, 'w')
    lines = open(train_orig, 'r').readlines()
    for i, line in enumerate(lines):
        aug_sentences = eda(line, alpha_sr=alpha_sr)
        for aug_sentence in aug_sentences:
            writer.write(aug_sentence + '\n')

    writer.close()
    print("generated augmented sentences with eda for " + train_orig + " to " + output_file)

#main function
if __name__ == "__main__":

    #generate augmented sentences and output into a new file
    gen_eda(args.input, output, alpha_sr=alpha_sr)
import os
import argparse
import pandas as pd

def parse_arguments(parser):
    parser.add_argument('--batch_size', default=128, type=int,help='The batch size')
    parser.add_argument('--min_samp', default=1300, type=int,help='Minimum number of samples')
    parser.add_argument('--data', default='/DATA/', type=str,help='Data folder')
    parser.add_argument('--file', default='product_List.txt', type=str,help='Txt file')
    args = parser.parse_args()
    return (args)

def data_extract(args):
    batch_size = args.batch_size
    min_samples = args.min_samp
    data_folder = args.data
    file_txt = args.file
    fw = open(os.getcwd()+data_folder+file_txt, 'w')
    for root, dirs, files in os.walk(os.getcwd()+data_folder):
        for file_name in files:
            if '.csv' in file_name:
                data = pd.read_csv(os.path.join(root, file_name),sep=';')
                if (data.shape[0]>min_samples)and (not ((data['Interval']>batch_size).any())):
                    print(file_name, file=fw)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parse_arguments(parser)
    data_extract(args)

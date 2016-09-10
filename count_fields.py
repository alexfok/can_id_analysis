#
# Alex Fok: Sep 2016
# Filter CAN ids from CAN capture in csv file given id appearance range
#
# Execution example:
# python2.7 count_fields.py --f AlexTest_504_508_50Aactuator2\ 9-04-2016\ 10-15-06\ am.csv  --id '525, 500, 7E0, 2222'
#     ('AlexTest_504_508_50Aactuator2 9-04-2016 10-15-06 am.csv', '1', '10', '525, 500, 7E0, 2222')
#     ('Command Line options: ', 'AlexTest_504_508_50Aactuator2 9-04-2016 10-15-06 am.csv', '1', '10', ['525', '500', '7E0', '2222'])
#
# Output example:
#***********CSV File analysis result:*********
#
#Found id: 525 Number of times: 155
#Found id: 500 Number of times: 157
#Found id: 7E0 Number of times: 149
#
#**************************************************


import sys
import csv
import argparse

def csv_count_as_dict(file, ref_header, delimiter=None, col_numb=None):

    import csv
    if not delimiter:
        delimiter = ','

    if not col_numb:
        col_numb = 10


    # skip first 60 lines in file
    fl = open(csv_file, 'r')
    [fl.readline() for i in xrange(59)]


    reader = csv.DictReader(fl, delimiter=delimiter)
#    reader = csv.DictReader(open(file), delimiter=delimiter)
    result = {}
    res_count = {}
    for row in reader:
#        print(row)
        # skip not relevant rows - with less than 10 columns
        if len(row) < col_numb:
           continue
        key = row.pop(ref_header)
#        print ("found key:", key)
        if key in res_count:
#            print ("key already exist:", key)
            res_count[key] += 1
            # implement your duplicate row handling here
#            pass
        else:
#            print ("Adding new key:", key)
            result[key] = row
            res_count[key]=1
    return res_count, result



if __name__ == "__main__":

# Command line options parsing
    parser = argparse.ArgumentParser(description='Filter ids from csv file given id appearance range',
    usage='%(prog)s -f <CSV_FILE> [--min 1] [--max 10] or %(prog)s -f <CSV_FILE> --id <COMMAND_ID_FOR_LOOKUP>')
    parser.add_argument('-f', '--file',dest='csv_file', required=True, help='csv file name')
    parser.add_argument('--min', dest='cid_min_app', help='min number of times id appears (default 1)',default='1')
    parser.add_argument('--max', dest='cid_max_app', help='max number of times id appears (default 10)',default='10')
    parser.add_argument('--id', dest='cid_lookup', type=str, help='id for lookup')
    args = parser.parse_args()
    print (args.csv_file, args.cid_min_app, args.cid_max_app, args.cid_lookup)

    csv_file = args.csv_file
    cid_min_app = args.cid_min_app
    cid_max_app = args.cid_max_app
    if args.cid_lookup:
       cid_lookup_list=[]
       cid_lookup_list_tmp = args.cid_lookup.split(',')
       for cids in cid_lookup_list_tmp:
          cid_lookup_list.append(cids.strip())
    else:
       cid_lookup_list = None

    print ("Command Line options: ", csv_file, cid_min_app, cid_max_app,cid_lookup_list)

    res_count = {}
    result = {}
    res_count, result = csv_count_as_dict(csv_file,'ID',',', 1)
    print("\n***********CSV File analysis result:*********\n")
    if not cid_lookup_list:
        for cid in res_count:
#        print ("res_count[cid]: ", res_count[cid], cid_min_app, cid_max_app)
            if int(cid_min_app) <= int(res_count[cid]) <= int(cid_max_app):
               print ("found id: ", cid, res_count[cid])
    else:
        for cid in res_count:
            if cid in cid_lookup_list:
               print("Found id: " + cid + " Number of times: " + "{}".format(res_count[cid]))
    print("\n**************************************************\n")

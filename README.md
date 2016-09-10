# can_id_analysis

# Alex Fok: Sep 2016
# Filter CAN ids from CAN capture in csv file given id appearance range

# Execution example:
python2.7 count_fields.py --f AlexTest_504_508_50Aactuator2\ 9-04-2016\ 10-15-06\ am.csv  --id '525, 500, 7E0, 2222'
     ('AlexTest_504_508_50Aactuator2 9-04-2016 10-15-06 am.csv', '1', '10', '525, 500, 7E0, 2222')
     ('Command Line options: ', 'AlexTest_504_508_50Aactuator2 9-04-2016 10-15-06 am.csv', '1', '10', ['525', '500', '7E0', '2222'])

# Output example:
***********CSV File analysis result:*********

Found id: 525 Number of times: 155
Found id: 500 Number of times: 157
Found id: 7E0 Number of times: 149

**************************************************

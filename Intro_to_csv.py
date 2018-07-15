import unicodecsv

def read_csv(file):
    with open(file,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

# read csv file
enrollments = read_csv('enrollments.csv')
print(enrollments[0])



# adjust the type of columns (dataType)

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

from datetime import datetime as dt
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date,'%Y-%m-%d')

for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

import random
import string
import pandas as pd

dummy_data_length = 100000

# Generating Cost Centers
ccs_ls = []

while len(ccs_ls) < 16:
    costcenter = ''.join(random.choices(string.ascii_uppercase, k=3))
    if costcenter in ccs_ls:
        pass
    else:
        ccs_ls.append(costcenter)

ccs = []

while len(ccs) < dummy_data_length:
    x = random.choice(ccs_ls)
    ccs.append(x)


# Generating Employee IDs
ids = []

while len(ids) < dummy_data_length:
    code = random.choice(string.ascii_uppercase)
    num = ''.join(random.choices(string.digits, k=6))
    newid = code + num
    if newid in ids:
        pass
    else:
        ids.append(code + num)

# Generating Payroll Codes

pr = []

while len(pr) < dummy_data_length:
    x = random.choices(['ADM', 'ATW', 'BTW'],
                       weights = [.1, .45, .45])
    pr.append(x[0])

# Generating Hiring Period

hire = []

while len(hire) < dummy_data_length:
    x = random.choice(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                       'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])
    hire.append(x)

# Generating FT/PT Categories
ftpt = []

while len(ftpt) < dummy_data_length:
    x = random.choices(['FT', 'PT'],
                               weights = [.3, .7])
    ftpt.append(x[0])


# Joining lists into data frame
df = pd.DataFrame(list(zip(ccs, ids, pr, hire, ftpt)),
                  columns = ['Cost Center', 'Employee ID', 'Payroll Code', 'Hiring Period', 'FT-PT Status'])

df.to_csv('dummy_data.csv')
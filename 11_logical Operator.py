#if applicant has high income and good credit
#       Eligible for loan

has_hign_income = True
has_good_credit = True

if has_good_credit and has_hign_income:
    print('Eligible for loan')

#if applicant has high income or good credit
#       Eligible for loan

has_hign_income = False
has_good_credit = True

if has_good_credit or has_hign_income:
    print('Eligible for loan!')


#  AND : both are true
#   OR : at least one is true

# if applicant has a good credit and dosen't have a criminal record
#       Eligible for loan

has_hign_income = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan!!')


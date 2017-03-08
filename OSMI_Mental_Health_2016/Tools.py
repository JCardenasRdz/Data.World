def clean_gender(df):
    list_male_genders = ['male','Male ','MALE','Man','man','M','m','male ']
    list_female_genders = ['female','female','female ','Female ','FEMALE','Woman','woman','F','f','fm']

    # make list of cases 
    # replace strings
    for str_ in list_male_genders:
        df.replace(str_,'Male',inplace=True)  
    for str_ in list_female_genders:
        df.replace(str_,'Female',inplace=True)
    return df


def my_chi2(X,Description):
    import scipy.stats
    from numpy import round
    chi2, p, _, expected_distribution = scipy.stats.chi2_contingency(X)
    def f():
        print('=='*20)
    print(Description)
    f()
    print('The p-value is : '+str(p))
    f()
    print('The test statistic is : '+str(chi2))
    f()
    print('The expected distribution is :')
    print(round(expected_distribution))
    f()
    
def get_data():
    import pandas as pd
    df = pd.read_csv('https://query.data.world/s/bs6aqtm2l54gty0ng1vsgw37k')
    # Get columns we need
    return df
    
def clean_US_states(full_names):
    us_state_abbrev_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'District of Columbia':'DC',
}
    import numpy as np
    states_abbreviation = np.zeros_like(full_names)
    for idx,name in enumerate(full_names):
        states_abbreviation[idx] = us_state_abbrev_dict[name]
    return states_abbreviation
    
    

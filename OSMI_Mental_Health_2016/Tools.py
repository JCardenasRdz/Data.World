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
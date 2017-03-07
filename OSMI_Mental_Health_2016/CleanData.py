def clean_data(df):
    list_male_genders = ['male','Male ','MALE','Man','man','M','m','male ']
    list_female_genders = ['female','female','female ','Female ','FEMALE','Woman','woman','F','f','fm']

    # make list of cases 
    # replace strings
    for str_ in list_male_genders:
        df.replace(str_,'Male',inplace=True)  
    for str_ in list_female_genders:
        df.replace(str_,'Female',inplace=True)
    return df
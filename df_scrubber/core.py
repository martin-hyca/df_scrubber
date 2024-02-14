# df_scrubber/core.py


# function to display all columns, their type, number of values, missing values, distinct values... 
def evaluate_df(df):
    column_name_types = [(name, dtype.name) for name, dtype in df.dtypes.items()]
    rows_count = df.shape[0] * 100  # get number of all rows in the df
    for column in column_name_types:  # for each column
        values_count = rows_count - df[column[0]].isna().sum()  # count missing values 
        missing_values_count = df[column[0]].isna().sum()  # count missing values 
        distinct_values_count = df[column[0]].nunique()
        missing_percentage = (missing_values_count / rows_count)  # calculate the percentage
        print(f"""{column[0]}\n 
    {column[1]} 
    {values_count} values
    {distinct_values_count} distinct values
    {missing_values_count} missing values 
    {missing_percentage:.5f}% of the rows missing""")

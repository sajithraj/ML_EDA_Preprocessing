


#Visualization of categorical Variables

# Visualization of categorical Variables using matplotlib barplot
def visualize_barplot(df , variable,x_axis =None , y_axis=None,title=None):
    df[variable].value_counts().plot(kind='bar', title= title,grid=True)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()


# Visualization of categorical Variables using sns countplot
def plot_sns_cat_feature(df , variable,x_axis =None , y_axis=None,title=None):
#     print(df[variable].value_counts())
    ax = sns.countplot(x=variable, data=df)
    plt.show()

# Visualization of categorical Variables using sns count plot with 2 variable
def plot_sns_cat_feature_with_target(df , variable, target_feature ,x_axis =None , y_axis=None,title=None):
    ax = sns.countplot(x=target_feature, hue=variable, data=df)
    plt.show()

##Visualization of Numerical Variables

# Visualization of of Numerical Variables using sns distplot 
def plot_sns_numeric_feature(df,variable ,x_axis =None , y_axis=None,title=None):
    sns.distplot(df[variable], kde=False, bins=15,grid=True)
    plt.show()

# Visualization of Numerical Variables using matplotlib histogram 
def plot_numeric(df,variable ,x_axis =None , y_axis=None,title=None):
    plt.hist(df[variable], bins = 20)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)
    plt.show()

# TO visualize the features in histogram
dataset.hist(figsize=(15, 20))

# Fectching features list based on the feature data type
1
# list of categorical features
2
def get_categorical_features(df):
3
    categorical_features = [feature for feature in df.columns if df[feature].dtypes == 'O']
4
    print('Number of categorical features : ', len(categorical_features))
5
    return categorical_features
1
# list of numerical features
2
def get_numerical_features(df):
3
    numerical_features = [feature for feature in df.columns if df[feature].dtypes != 'O']
4
    print('Number of numerical features : ', len(numerical_features))
5
    return numerical_features
1
# list of date features
2
def get_date_features(df):
3
    numerical_features = [feature for feature in df.columns if df[feature].dtypes != 'O']
4
    year_feature = [feature for feature in numerical_features if 'Yr' in feature or 'yr' in feature or 'Year' in feature or 'year' in feature]
5
    print('Number of date features: ', len(year_feature))
6
    return year_feature
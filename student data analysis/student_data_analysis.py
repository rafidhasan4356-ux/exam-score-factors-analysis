import numpy as np

import pandas as pd

import sqlite3 as sq


conn = sq.connect("student_data.db")

df = pd.read_csv(r"A:\student data analysis\student_dataset.csv")

print(df.isnull().sum())

print("\n \n")

# checking outliners in numeric columns 
numeric_cols = ['Hours_Studied','Attendance','Sleep_Hours','Previous_Scores','Tutoring_Sessions','Final_Exam_Score']

for col in numeric_cols:
    print(f"{col} - min: {df[col].min()},max: {df[col].max()}")

print("\n \n")

# checking unique values in categorical columns
cat_cols = ['Parental_Involvement','Access_to_Resources','Extracurricular_Activities','Motivation_Level','Internet_Access']

for col in cat_cols:
    print(f"{col}: {df[col].unique()}")


print('\n \n')


# checking on study hours 
print("Study Hours Description.....")
print(df["Hours_Studied"].describe())
print("\n")

print("Study Hours greater than 30")
print(df[df["Hours_Studied"] > 30])
print("\n")

print("Students Whom study hour is greater than 39 hours")
print(df[df["Hours_Studied"] > 39.0])
print('\n')

print("Printing Performance Level......")
df["Performance_level"] = np.where(df["Final_Exam_Score"] >= 80 ,'High',
                                   np.where(df["Final_Exam_Score"] >=60, 'Medium', 'Low'))

print(df["Performance_level"].value_counts())
print(df[["Final_Exam_Score","Performance_level"]].head())
print('\n \n')


# compute correlation matrix
corr_matrix = df[numeric_cols].corr()

# show correlation with Final_Exam_Score(sorted)
corr_with_Target = corr_matrix['Final_Exam_Score'].sort_values(ascending=False)
print("Correlation with Final Exam Score:")
print(corr_with_Target)

print('\n \n ')


df.to_sql("students",conn,if_exists="replace",index=False)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'; ",conn)

print(tables)

print("\n \n")

column_info = pd.read_sql_query("PRAGMA table_info(students);",conn)

print(column_info)

print("\n \n")

sample = pd.read_sql_query("SELECT * FROM students LIMIT 5;",conn)

print(sample)

print("\n \n")

query_sleep_final_score= 'SELECT Sleep_hours, Final_Exam_Score FROM students'

sleep_final_score = pd.read_sql_query(query_sleep_final_score,conn)

print(sleep_final_score.head())

print("\n \n")

query_get30 = ' SELECT Extracurricular_Activities, Sleep_Hours,Previous_Scores  FROM students WHERE Hours_Studied >30 '

df_get30 = pd.read_sql_query(query_get30,conn)
print("Students with Hours_Studied > 30 :")
print(df_get30)
print('\n Shape:',df_get30.shape)
print("\n \n")

query_get39 = "SELECT Extracurricular_Activities, Sleep_Hours , Previous_Scores FROM students WHERE Hours_Studied >39"

df_get39 = pd.read_sql_query(query_get39,conn)
print("Students With Hours_Studied >39 :")
print(df_get39)
print("\nShape:", df_get39.shape)


Performance = pd.read_sql_query("SELECT Performance_level, AVG(Hours_Studied),AVG(Sleep_Hours) FROM students GROUP BY Performance_level",conn)
print(Performance)

parental_involvementWise_avg_score = pd.read_sql_query("SELECT Parental_Involvement, AVG(Final_Exam_Score) as avg_score FROM students GROUP BY Parental_Involvement ORDER BY avg_score DESC",conn)

print(parental_involvementWise_avg_score)

tutoring_sessions_related = pd.read_sql_query("SELECT Tutoring_Sessions,Final_Exam_Score FROM students",conn)

# close connection
conn.close()


# correlation
print('Tutoring Session related correlation.....')
print(tutoring_sessions_related.corr())

# compare groups 
print("Comparing Groups.......")
df["tutoring_group"] = pd.cut(df["Tutoring_Sessions"],bins=[-1,2,8],labels= ['0-2 sessions','3+ sessions'])
print(df.groupby("tutoring_group")["Final_Exam_Score"].describe())

print("\n \n")

conn  = sq.connect("student_data.db")

effectsof_Accesstoresources = pd.read_sql_query("SELECT Access_to_Resources, AVG(Final_Exam_Score) as avg_score , COUNT(*) as count FROM students GROUP BY Access_to_Resources ORDER BY avg_score DESC",conn)

print(effectsof_Accesstoresources)

print("\n \n ")

accessofresources_motivationlevel = pd.read_sql_query("SELECT Access_to_Resources,Motivation_Level,AVG(Final_Exam_Score) as avg_score FROM students GROUP BY Access_to_Resources,Motivation_Level ORDER BY Access_to_Resources , avg_score DESC",conn)

print(accessofresources_motivationlevel)

df_extra = pd.read_sql_query("SELECT Extracurricular_Activities, Final_Exam_Score FROM students", conn)

# Group Averages
print(df_extra.groupby("Extracurricular_Activities")["Final_Exam_Score"].agg(['mean','std','count']))

df_internet = pd.read_sql_query("SELECT Internet_Access , Final_Exam_Score FROM students",conn)

print(df_internet.groupby("Internet_Access")["Final_Exam_Score"].agg(["mean",'std',"count"]))

df_prev = pd.read_sql_query("SELECT Previous_Scores,Final_Exam_Score FROM students",conn)

corr_prev = df_prev["Previous_Scores"].corr(df_prev["Final_Exam_Score"])

print(f"Correlation between Previous score and Final Exam Score: {corr_prev:.3f}")

conn.close()
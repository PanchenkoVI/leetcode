'''
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
'''

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    tmo_dict = {}
    result = []
    for lst in person['email'].tolist():
        tmo_dict[lst] = tmo_dict.get(lst, 0) + 1
    for key, value in tmo_dict.items():
        if value > 1:
            result += [key]
    return pd.DataFrame({'Email':result})

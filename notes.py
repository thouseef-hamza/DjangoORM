# =======================================================================================
# ================================= Keys In RDBMS =======================================
# ======================================================================================
# Keys =================>
"""
<> Is an attribute or a set of attribute that uniquely identify a row/tuple in a relation/table
<> It is used to establish raltionship between tables and columns of a relational databases
"""
# Types of Keys =================>
"""
=> SuperKey
=> Candidate Key 
=> Primary Key   
=> Secondary/Alternate Key
=> Composite Key
=> Foreign Key
"""
# Super Key =====>
"""
* a set of attribute that uniquely identify 
* a combination of  unique key and other attributes
"""

# Candidate Key =====>
"""
<> Key Definition
<> Subset of SuperKey
<> Minimal SuperKey
! <> Not allows null
            

SuperKey ===================> CandidateKey
           (Extracted to)
"""
# Primary Key ====>
"""
<> Key Definition
<> Only 1 primary for a table 
<> Selected from list of candidate keys
! <> Not allow null

SuperKey ===================> CandidateKey ====================> PrimaryKey
           (Extracted to)                     (Extracted to)
"""
# Alternate Key / Secondary Key ========>
"""
<> Key Definition
<> Are candidate keys that has been selected to be the primary key 
"""
# Composite Key ========>
"""
<> Combination of one or more attributes that uniquely identify tuples in a relation.
<> Any Key can be composite 
"""
# Foreign Key =======>
"""
<> Used to link two tables via primary key 
"""
# ========================================================================================
# ================= Normalization =======================================================
# =================================================================================
"""
<> Used to reduce data redundancy
<> Redundancy ( Duplicate Data )
!PROBLEMS
-> More Memory
-> More Access Time
-> Data Inconsistency     # sthiratha
-> Anomalies              # Errors
   => Insertion Anomalies
   => Deletion Anomalies
   => Updation Anomalies
"""
# 1st Normal Form =========================>
"""
<> It should have only single valued attribute

! Table with Violation of 1NF:

                       Table: Student_Courses

| Student_ID | Student_Name | Course_1   | Course_2   | Course_3   |
|------------|--------------|------------|------------|------------|
| 1          | John         | Math       | Science    | History    |
| 2          | Jane         | English    | Math       | NULL       |
| 3          | Mike         | History    | Physics    | Chemistry  |

! Converted To 1NF ===================>
 
      Table:- Students                 Table:- Courses                     Table:- Enrollments
|------------|--------------|
| Student_ID | Student_Name |     | Course_ID | Course_Name |           | Student_ID | Course_ID |
|------------|--------------|     |-----------|-------------|           |------------|-----------|
| 1          | John         |     | 1         | Math        |           | 1          | 1         |
| 2          | Jane         |     | 2         | Science     |           | 1          | 2         |
| 3          | Mike         |     | 3         | History     |           | 1          | 3         |
                                  | 4         | English     |           | 2          | 4         |
                                  | 5         | Physics     |           | 2          | 1         |
                                  | 6         | Chemistry   |           | 3          | 3         |
                                                                        | 3          | 5         |
                                                                        | 3          | 6         |
"""
# 2nd Normal Form =========================>

"""
<> It Should Be In 1st Normal Form
<> All NonKeys are Fully Functionally depends on Primary Key OR
<> No Partial Dependancy

! Table with Violation of 2NF:

                     Table: Order_Details

| Order_ID | Product_ID | Product_Name | Category      | Quantity |
|----------|------------|--------------|---------------|----------|
| 1        | 101        | Laptop       | Electronics   | 2        |
| 1        | 102        | Mouse        | Accessories   | 5        |
| 2        | 101        | Laptop       | Electronics   | 1        |
| 2        | 103        | Keyboard     | Accessories   | 3        |

! Converted to 2NF:

Table: Orders              Table: Products                      Table: Order_Details

| Order_ID |   | Product_ID | Product_Name | Category     |  | Order_ID | Product_ID | Quantity |
|----------|   |------------|--------------|--------------|  |----------|------------|----------|
| 1        |   | 101        | Laptop       | Electronics  |  | 1        | 101        | 2        |
| 2        |   | 102        | Mouse        | Accessories  |  | 1        | 102        | 5        |
               | 103        | Keyboard     | Accessories  |  | 2        | 101        | 1        |
                                                             | 2        | 103        | 3        |
"""

# 3rd Normal Form =======================================>

"""
<> It Should be in 2nd Normal Form.
<> There must not be any transitive dependency
"""

arr =[1,3,5]

def test(arr):
      X  = {x for x in arr}
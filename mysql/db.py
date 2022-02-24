import csv

import mysql.connector

from private.keys import db_id, db_pass



def read_from_file ():
  mydb = mysql.connector.connect(
    database="mondrian",
    host="localhost",
    user=db_id,
    password=db_pass
  )
  mycursor = mydb.cursor()

  with open('../data/adult.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
      else:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        sql2 = "INSERT INTO adult(age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hour_per_week,native_country,income) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        val = (
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
        row[13], row[14])

        mycursor.execute(sql2, val)



        line_count += 1
    print(f'Processed {line_count} lines.')
    mydb.commit()


read_from_file ()
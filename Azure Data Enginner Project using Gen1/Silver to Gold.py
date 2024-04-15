# Databricks notebook source
# MAGIC %md
# MAGIC ## Change "ColumnName" to "Column_Name" for all tables

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for name in table_name:
    path='/mnt/silver/SalesLT/'+ name
    print(path)
    df=spark.read.format("csv").option('header','true').load(path)

    #get the list of column_names
    column_names=df.columns

    for old_col_name in column_names:
        # convert column name from column to column_name format
        new_col_name="".join(["_"+ char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

        # Change the column name using withcolumnRenamed and regexp_replace
        df=df.withColumnRenamed(old_col_name,new_col_name)

    output_path='/mnt/gold/SalesLT/' + name + '/'
    df.write.format('csv').option('header','true').mode("overwrite").save(output_path)


# COMMAND ----------

display(df)

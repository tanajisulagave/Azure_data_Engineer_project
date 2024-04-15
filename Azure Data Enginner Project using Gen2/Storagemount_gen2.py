# Databricks notebook source
# MAGIC %md
# MAGIC ##Mount blob storages (Staging, Load and Datawarehouse) in Azure data bricks

# COMMAND ----------

dbutils.fs.mount(
  source = 'wasbs://staging@satandatalakegen2.blob.core.windows.net',
  mount_point = '/mnt/staging',
  extra_configs = {'fs.azure.account.key.satandatalakegen2.blob.core.windows.net':'aUiNca/KjvQ1xEGMd2RpFEDBM8kGmDnqvbyjskMIwAdLxgCNOYNb1DbEKlKG4r5JL3I3ydLznYqJ+AStG/lMhQ=='})

# COMMAND ----------

dbutils.fs.ls("/mnt/staging/SalesLT")

# COMMAND ----------

dbutils.fs.mount(
  source = 'wasbs://load@satandatalakegen2.blob.core.windows.net',
  mount_point = '/mnt/load',
  extra_configs = {'fs.azure.account.key.satandatalakegen2.blob.core.windows.net':'aUiNca/KjvQ1xEGMd2RpFEDBM8kGmDnqvbyjskMIwAdLxgCNOYNb1DbEKlKG4r5JL3I3ydLznYqJ+AStG/lMhQ=='})

# COMMAND ----------

dbutils.fs.ls("/mnt/load")

# COMMAND ----------

dbutils.fs.mount(
  source = 'wasbs://datawarehouse@satandatalakegen2.blob.core.windows.net',
  mount_point = '/mnt/datawarehouse',
  extra_configs = {'fs.azure.account.key.satandatalakegen2.blob.core.windows.net':'aUiNca/KjvQ1xEGMd2RpFEDBM8kGmDnqvbyjskMIwAdLxgCNOYNb1DbEKlKG4r5JL3I3ydLznYqJ+AStG/lMhQ=='})

# COMMAND ----------

dbutils.fs.ls("/mnt/datawarehouse")

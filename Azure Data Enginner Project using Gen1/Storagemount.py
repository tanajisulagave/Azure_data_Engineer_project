# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount blob storages (bronze, Sliver and Gold) in Azure data bricks 

# COMMAND ----------

dbutils.fs.mount(
  source = 'wasbs://bronze@tandatalakegen2.blob.core.windows.net',
  mount_point = '/mnt/bronze',
  extra_configs = {'fs.azure.account.key.tandatalakegen2.blob.core.windows.net':'3VXAiTJNOxIg9LZk5jD/HTwbTA7aYtLXJJJAwqPA5bMD3s/HJIpRCg5HtjXlrgFTt3kgsIwzxPKC+AStd+UIag=='})

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze/SalesLT")

# COMMAND ----------

#dbutils.fs.unmount('/mnt/silver')

dbutils.fs.mount(
  source = 'wasbs://silver@tandatalakegen2.blob.core.windows.net',
  mount_point = '/mnt/silver',
  extra_configs = {'fs.azure.account.key.tandatalakegen2.blob.core.windows.net':'3VXAiTJNOxIg9LZk5jD/HTwbTA7aYtLXJJJAwqPA5bMD3s/HJIpRCg5HtjXlrgFTt3kgsIwzxPKC+AStd+UIag=='})

# COMMAND ----------

dbutils.fs.mount(
  source = 'wasbs://gold@tandatalakegen2.blob.core.windows.net',
  mount_point = '/mnt/gold',
  extra_configs = {'fs.azure.account.key.tandatalakegen2.blob.core.windows.net':'3VXAiTJNOxIg9LZk5jD/HTwbTA7aYtLXJJJAwqPA5bMD3s/HJIpRCg5HtjXlrgFTt3kgsIwzxPKC+AStd+UIag=='})

# COMMAND ----------

dbutils.fs.unmount('/mnt/silver')

# COMMAND ----------

# MAGIC %md
# MAGIC

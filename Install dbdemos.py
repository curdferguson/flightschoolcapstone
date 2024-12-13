# Databricks notebook source
# MAGIC %pip install dbdemos

# COMMAND ----------

import dbdemos

# COMMAND ----------

dbdemos.install('lakehouse-iot-platform', catalog = "dbdemosfs1224group5", schema = "dbdemos_iot_platform", overwrite=True)

# COMMAND ----------



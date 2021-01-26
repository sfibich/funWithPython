#!/bin/bash
# WORKS IF YOU ONLY HAVE ONE FUNCTIONAPP...otherwise add to the query
APP_NAME=$(az functionapp list --query "[].name" -o tsv)
func azure functionapp publish $APP_NAME

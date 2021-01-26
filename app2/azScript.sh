RESOURCE_GROUP=AzureFunctionQuickstart-rg
RANDOM_NUMBER=($RANDOM % 100000)
STORAGE_NAME="azfuncqsst$RANDOM_NUMBER"
LOCATION=eastus2
APP_NAME="azfuncqsfn$RANDOM_NUMBER"
echo "STORAGE_NAME:$STORAGE_NAME"

az group create --name $RESOURCE_GROUP --location $LOCATION

az storage account create --name $STORAGE_NAME  --location $LOCATION --resource-group $RESOURCE_GROUP --sku Standard_LRS

az functionapp create --name $APP_NAME \
	--resource-group $RESOURCE_GROUP \
	--consumption-plan-location $LOCATION \
	--runtime python --runtime-version 3.6 \
	--functions-version 3 --name $APP_NAME \
	--storage-account $STORAGE_NAME \
	--os-type linux


az functionApp list -g AzureFunctionQuickstart-rg  -- output table


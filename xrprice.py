# Grabs and displays XRP Price from an XRP Validator: rXUMMaPpZqPutoRszR29jtC8amWq3APkx
# xrpl.account.get_latest_transaction(account: str, client: SyncClient) → Response
import xrpl
from datetime import datetime
import mysql.connector
# Configure local setting information in the settings.py file
import settings 
dbaddress=settings.dbaddress
dbuser=settings.dbuser
dbpassword=settings.dbpassword
dbdb=settings.dbdb
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
# Connect to DB
mydb = mysql.connector.connect(
  host=dbaddress,
  user=dbuser,
  password=dbpassword,
  database=dbdb
)
# Get current Price
from xrpl.clients import JsonRpcClient
JSON_RPC_URL = "https://s2.ripple.com:51234/"
client = JsonRpcClient(JSON_RPC_URL)
xaccount = "rXUMMaPpZqPutoRszR29jtC8amWq3APkx"
xresponse = xrpl.account.get_latest_transaction(xaccount, client)
price=xresponse.result['transactions'][0]['tx']['LimitAmount']['value']
print(price)
# Data to write to DB : datetime, price
mycursor = mydb.cursor()
sql = "INSERT INTO xrp (pricedatetime, price) VALUES (%s, %s)"
val = (dt_string,price)
mycursor.execute(sql, val)
mydb.commit()

from mailjet_rest import Client
from db_details import mailjet_public_api_key as api_key, mailjet_secret_api_key as api_secret_key

mailjet = Client(auth=(api_key, api_secret_key), version='v3.1')

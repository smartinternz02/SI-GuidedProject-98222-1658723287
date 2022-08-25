import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "G-hCBLM-IG6t46oFLPdg5SEh6oXkmn5NUoK_E8nTD3dD"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["diagnosis","fev","age","performance","tnm","hae","pain","dys","cough","weakness","dm","mi","pad","smoking","asthma"]],
                                   "values": [[1.22459508,  0.00717926,  0.37059679, -0.25400025, -0.40430377,
       -0.24147264,  0.64650503, -0.44942937,  0.38985389, -0.29466311,
       -0.07443229, -0.15011733,  0.46703405, -0.05255883,  1.43058247]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8eda797d-2bfb-454d-a287-de8e8f68de56/predictions?version=2022-08-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]
if(pred == 0):
    print("Patient is at high risk")
else:
    print("Patient is not at risk")
    

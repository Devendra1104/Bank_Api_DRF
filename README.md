# Bank_Api_DRF
Developed Api's to fetch bank details using ifsc and also all the bank branch in a particular city using bank name and city.
The basic endpoint format for this API is http://devendra1049.pythonanywhere.com/bank/?.Searching for bank using bank ifsc is also available.
We can aslo get the list of branch in particular city using the city and bankname parameters.

Examples:
1. sample endpoint : GET http://devendra1049.pythonanywhere.com/bank/?ifsc=ABHY0065004
sample response:
 [{
        "id": 51,
        "ifsc": "ABHY0065004",
        "bank_id": 60,
        "branch": "BHANDUP",
        "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
        "city": "MUMBAI",
        "district": "GREATER MUMBAI",
        "state": "MAHARASHTRA",
        "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    }]
    
  2. sample endoint: GET http://devendra1049.pythonanywhere.com/bank/?city=MUMBAI&bank_name=ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED
  sample response: 
  [{
        "id": 48,
        "ifsc": "ABHY0065001",
        "bank_id": 60,
        "branch": "RTGS-HO",
        "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
        "city": "MUMBAI",
        "district": "GREATER MUMBAI",
        "state": "MAHARASHTRA",
        "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    },
    {
        "id": 49,
        "ifsc": "ABHY0065002",
        "bank_id": 60,
        "branch": "ABHYUDAYA NAGAR",
        "address": "ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033",
        "city": "MUMBAI",
        "district": "GREATER MUMBAI",
        "state": "MAHARASHTRA",
        "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    }]

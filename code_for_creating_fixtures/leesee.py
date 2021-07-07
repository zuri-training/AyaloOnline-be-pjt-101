# {			Business_name = models.CharField(max_length=150)
# 			business_address=models.CharField(max_length=150)
# 			CAC=models.CharField(max_length=150)
# 			choicess=[('BVN', 'BVN'), ('NIN', 'NIN')]
# 			VerificationMethod=models.CharField(max_length=256, choices=choicess)
# 			VerificationField=models.IntegerField()

# }


import random
from barnum import gen_data
import math
import json
choicess=['BVN', 'NIN']


data=[]

p=[i for i in range(1, 39)]
for i in p:

	item={"model": "ayaloapp.ModelLeesee", "pk": i, "fields": {}}
	item["fields"]['Leesee']=random.choice(p)
	item["fields"]['Business_name']=gen_data.create_company_name()
	address=""
	for i in gen_data.create_city_state_zip():
		address=address+i+","
	item["fields"]['business_address']=address.strip(',')
	item["fields"]['CAC']=gen_data.create_cc_number()[1][0]
	item["fields"]['VerificationMethod']=random.choice(choicess)
	item["fields"]['VerificationField']=gen_data.create_cc_number()[1][0]
	data.append(item)



with open('C:\\Users\\Amaka\\Scripts\\django-codes\\other_code\\AyaloOnline-be-pjt-101\\fixtures\\leesee.json', 'a') as file:
	file.write(json.dumps(data))

file.close()
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
p=[i for i in range(40)]



m=0
p=[i for i in range(40)]
for i in range(40):
	m=m+1
	if m == 2:
		continue
	item={"model": "ayaloapp.ModelLeesee", "pk": m, "fields": {}}
	item["fields"]['Leesee']=p[m]
	item["fields"]['Business_name']=gen_data.create_company_name()
	address=""
	for i in gen_data.create_city_state_zip():
		address=address+i+","
	item["fields"]['business_address']=address
	item["fields"]['CAC']=gen_data.create_cc_number()[1][0]
	item["fields"]['VerificationMethod']=random.choice(choicess)
	item["fields"]['VerificationField']=gen_data.create_cc_number()[1][0]



	with open('.\\django-codes\\other_code\\AyaloOnline-be-pjt-101\\fixtures\\leesee.json', 'a') as file:
		file.write(json.dumps(item))

	file.close()
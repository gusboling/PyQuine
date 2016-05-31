original_code="import random\nid_number=random.randint(0,9999)\n"
import random
id_number=random.randint(0,9999)
copy_name="pyquine+str(id_number)+".py"
copy=open(copy_name,'w')
copy.write(original_code)
copy.close()
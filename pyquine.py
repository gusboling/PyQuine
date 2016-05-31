original_code="import random\nid_number=random.randint(0,9999)\ncopy_name=\"pyquine\"+str(id_number)+\".py\"\ncopy=open(copy_name,\'w\')\ncopy.write(original_code)\ncopy.close()"
import random
id_number = random.randint(0,9999)
copy_name = "pyquine" + str(id_number) + ".py"
copy = open(copy_name, 'w')

#May 31, 2016: I've just realized the code below is flawed due to a cyclical relation between the original_code string and
#   the code I want written in the offspring code. Because of this, the second-generation offspring will be sterile and/or nonfunctional.
#   I'm going to stop development for now, but I am confident I can overcome this hurdle. It would be a lot easier to just read in the source
#   code as input, but I think that would violate the conditions of a quine.
copy.write("original_code="+"\""+"import random\\nid_number=random.randint(0,9999)\\n")
copy.write("copy_name="+"\\"+"\""+"pyquine+"+"\""+"str(id_number)+"+"\\"+"\""+".py"+"\\"+"\"")
copy.write("\"")
copy.write("\n")

copy.write(original_code)
copy.close()

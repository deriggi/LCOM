from random import random

class Industry(object):

	def __init__(self, industry_name):
		self.name = industry_name
		self.cam = []
		self.cam_length = 10;

	# assign 10 scores from a random normal sample	
	def assign_random_normal_scores(self):
		for x in range (self.cam_length):
			randy_normal = random()/2 - random()/2 + 0.5;
			self.cam.append(randy_normal);

	def output_cam(self):
		for x in self.cam:
			print(x)		


######################################
# example usage
######################################

# create an industry
c1 = Industry("catering");

# populate its cam 
c1.assign_random_normal_scores();

# print the list
c1.output_cam()

# a list of names
industry_names=  ["aviation", "concrete construction", "hydro engineering", "drilling", "oil extraction"]

# create a bunch of industries from a list of names
for namo in industry_names :
	i = Industry(namo)
	i.assign_random_normal_scores()


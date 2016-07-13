from random import random

class Industry(object):

	def __init__(self, industry_name):
		self.name = industry_name
		self.cam = []
		self.cam_length = 10;

	# assign 10 scores to random normal function	
	def assign_random_normal_scores(self):
		for x in range (self.cam_length):
			randy_normal = random()/2 - random()/2 + 0.5;
			self.cam.append(randy_normal);


# create a category
c1 = Industry("catering");

# populate its cam with a random normal distribution
c1.assign_random_normal_scores();


print(c1);

from random import random

class Category(object):

	def __init__(self):
		self.cam = []
		self.cam_length = 10;

	def assign_random_normal_scores(self):
		for x in range (self.cam_length):
			randy_normal = random()/2 - random()/2 + 0.5;
			self.cam.append(randy_normal);


# create a category
c1 = Category();

# populate its cam with a random normal distribution
c1.assign_random_normal_scores();


print(c1);

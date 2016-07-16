import random
import math


class Company(object):
	MAX_COMPANY_SIZE = 10000;
	ASSESSMENT_SCORE_SIZE = 25;

	def __init__(self):
		self.size = math.floor(random.random()*Company.MAX_COMPANY_SIZE)	
		self.assessment_scores = []

	# assigne random normal scores to the self assessment
	def assign_assessment_scores(self):

		# for each score
		for x in range(Company.ASSESSMENT_SCORE_SIZE):

			# get a random normal averaged at 3.5 with stdev of 1
			randy_normal = random.normalvariate(3.5,1)

			# scale by the size of the company
			randy_normal = randy_normal*math.log(self.size)
			self.assessment_scores.append(randy_normal);


class Industry(object):

	def __init__(self, industry_name):
		self.name = industry_name
		self.cam = []
		self.cam_length = 10;
		self.cam_radius = 3.0;  # for the 0 to 7 score


	# assign cam scores from a random normal sample	
	def assign_random_normal_scores(self):
		for x in range (self.cam_length):
			# (0 -> 7)
			randy_normal = random.random()*self.cam_radius - random.random()*self.cam_radius + self.cam_radius;
			self.cam.append(randy_normal);

	def output_cam(self):
		for x in self.cam:
			print(x)		


######################################
# example usage
######################################



# test random company size with 10 companies
print("company sizes")
for z in range(40):
	c = Company()
	c.assign_assessment_scores()
	print(c.assessment_scores)



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


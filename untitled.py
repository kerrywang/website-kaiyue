##Recommendation System####

#the General Workflow: Job Post -> filtering (hard requirements) -> (K nearest Neighbor for Personality match)

#2 types of recommendation: usr -> jobs.  employer -> usr


###Employer -> usr
def filter (requirement-matrix):
	# Look through data base and query the index of users that satisfy the requirement ( probably need to come up with a priority matching algo)

	# return the list of index of users that satisfy the requirement


def recommendation (usr-index-list, founder-index, k):
	# get the k nearest neighbors of usr related to founders personality
	#Possible algo: KNN, K-D tree
	#return a list of k usr index which is the recommended user.



###usr -> job
def job-filter (usr-skill-set):
	# Look through data base and query the index of job that matches the usr skill set 
	# return the list of index of jobs that satisfy the requirement


def recommendation (usr-index, jobs-index, k):
	# within the jobs that matches user, find the top k founders have the similar peronality

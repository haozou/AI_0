'''
Created on 2013-1-11

the program is based on python 2.6

this program is used to calculate the 

times that each user has logged in the

some on line game. Also, it calculates 

the average times for all the users.
  
@author: Hao Zou
'''
class LoginCount:
    # the dictionary for the users, the key is the user id
    # the value is the times the user had logged in
    user_dic = {}
    # initial function to initialize the user_dic
    def __init__(self,file_name):
        userloginfile = open(file_name,'r')  
        for line in userloginfile:
            line = line.strip().split()
            uid = line[2]
            # for the user that has alread appear, we add one
            # to the times, otherwise, we add a new user.
            if self.user_dic.has_key(uid):
                self.user_dic[uid] += 1
            else:
                self.user_dic[uid] = 1
    # output the user_id and the times the user had logged in
    def times_for_each(self):
        print 'user_id', 'login_times'
        for id in self.user_dic:
            print id,'\t',self.user_dic[id] 
            
    # ontput the average of the times for all the user
    def average(self):
        count = 0.0
        for id in self.user_dic:
            count += self.user_dic[id]
        average = count/len(self.user_dic)
        print 'average times:', average
    
if __name__ == '__main__':
    file_name = 'userlogin.txt'
    l = LoginCount(file_name)
    l.times_for_each()
    l.average()
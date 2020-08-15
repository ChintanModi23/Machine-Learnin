Write a Python program that implements gradient descent for minimizing
the least squares loss. As a stopping condition check for the objective
between the current and previous iteration. If the objective improves
by less than theta then you stop. The input and output should be the same 
as for nearest means and Naive-Bayes. 

Test your program with the input data

0 0
0 1
1 0
1 1
10 10
10 11
11 10
11 11

and labels 

0 0
0 1
0 2
0 3
1 4
1 5
1 6
1 7

Use eta=.001 and stopping condition of .001. 

Your final w would be close to

w = 0.0889184232356005 0.0907934047968894 

and distance of plane to origin would be about

abs(w0/||w||) = 7.09045903042441

If you change the stopping condition to 0, in other words 
full convergence, then your final w would be

w = 0.0995024069539168 0.0995025677420564 

and distance to origin 

abs(w0/||w||) = 7.77817457926694

Added an adaptive eta setting for Hinge Loss. 
Between the compute dellf and updatew code portions
insert the following pseudocode

eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
bestobj = 1000000000000
for k in range(0, len(eta_list), 1):

  eta = eta_list[k]
  
  ##update w
  ##insert code here for w = w + eta*dellf

  ##get new error
  error = 0
  for i in range(0, rows, 1):
    if(trainlabels.get(i) != None):
      ##update error
      ##insert code to update the loss (which we call error here)

  obj = error

  ##update bestobj and best_eta
  ##insert code here

  ##remove the eta for the next
  ##insert code here for w = w - eta*dellf

eta = best_eta


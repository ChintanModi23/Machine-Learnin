Write a Python program for optimizing the SVM hinge loss. 
descent algorithm. The input and output should be the same as for
assignment 2.

Test your program with the input data

1 1
1 2
1 3
3 1
3 2
3 3
50 2

and labels <to be provided>

0 0
0 1
0 2
1 3
1 4
1 5
1 6

Convert label 0 to -1 so that labels yi are either +1 or -1. This is
necessary for the gradient descent to work.

Use eta=.001 and stopping condition of while(abs(prevobj - obj) > .000000001). 
Note the absolute value to account for instability in the gradient for hinge 
loss. The converged solution with the hinge loss would be

w = (1.4605574252399243, -0.4595542036671061)
w0 = -2.0024682128830427
Dist to origin= 1.3078203832146862

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


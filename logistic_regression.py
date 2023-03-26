
import numpy as np

# x represents size of tumor  in cm
x = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
print(x)

#0 represents 'NO' and 1 represents 'YES'
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
print(y)

from sklearn import linear_model

logr = linear_model.LogisticRegression()
logr.fit(x,y)

n = input("Enter the size of tumor in (cm) :  "  )
predicted = logr.predict(np.array([n]).reshape(-1,1))
print(predicted)
print(type(predicted))
if(predicted == True):
  print(n,"is cancerous. Do visit oncologist !")
else:
  print(n,"is not cancerous. Thank you 😄")


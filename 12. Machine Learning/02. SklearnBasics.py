'''
				Scikit learn
'''

'''
Scikit learn is a library used to perform machine learning in Python. 
It provides a range of supervised and unsupervised learning algorithms in Python. 
Apart from that, it also contains the following packages:
- NumPy
- Matplotlib
- SciPy (Scientific Python)
To implement Scikit learn, we first need to import the above packages.

Scikit learn comes with sample datasets, such as iris and digits. 
You can import SVM which stands for Support Vector Machine. SVM is a form of machine learning which is used to
 analyze data.
'''

EXAMPLE_1 = '''
Let us take an example where we will take digits dataset and it will categorize the numbers for us, 
for example- 0 1 2 3 4 5 6 7 8 9.
'''
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits= datasets.load_digits()
print(digits.data)

# output
[[ 0.  0.  5. ...  0.  0.  0.]
 [ 0.  0.  0. ... 10.  0.  0.]
 [ 0.  0.  0. ... 16.  9.  0.]
 ...
 [ 0.  0.  1. ...  6.  0.  0.]
 [ 0.  0.  2. ... 12.  0.  0.]
 [ 0.  0. 10. ... 12.  1.  0.]]


# other operations such as target, images
print(digits.target)
print(digits.images[0])

# output  
#  target of the data
[0 1 2 ... 8 9 8]

# image of the data
[[ 0.  0.  5. 13.  9.  1.  0.  0.]
 [ 0.  0. 13. 15. 10. 15.  5.  0.]
 [ 0.  3. 15.  2.  0. 11.  8.  0.]
 [ 0.  4. 12.  0.  0.  8.  8.  0.]
 [ 0.  5.  8.  0.  0.  9.  8.  0.]
 [ 0.  4. 11.  0.  1. 12.  7.  0.]
 [ 0.  2. 14.  5. 10. 12.  0.  0.]
 [ 0.  0.  6. 13. 10.  0.  0.  0.]]


# Learning and Predicting
# To predict the class, we need an estimator which helps to predict the classes to which unseen samples belong. 
# In Scikit learn, we have an estimator for classification which is a python object that implements 
# the methods fit(x,y) and predict(T). 

EXAMPLE_2 = '''
we have used a dataset (sample of 10 possible classes, digits from zero to nine) and 
we need to predict the digits when an image is given.
'''
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()                     # dataset

clf = svm.SVC(gamma=0.001, C=100)
print(len(digits.data))

x, y = digits.data[:-1], digits.target[:-1]         # train the data
clf.fit(x, y)

print('Prediction:', clf.predict(digits.data[-1].reshape(1, -1)))  # predict data

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()  

# Output
1797
1797
Prediction: [8]


EXPLAINATION = '''
1. We had first found the length and loaded 1797 examples. 
2. Next, we have used this data as a learning data, where we need to test the last element and 
	first negative element. 
3.we need to check whether the machine has predicted the right data or not. 
	For that, we had used Matplotlib where we had displayed the image of digits. 
	So to conclude, you have digits data, you got the target, you fit and predict it
'''


EXAMPLE_3 = 'You can also visualize the target labels with an image'
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits= datasets.load_digits()
# Join the images and target labels in a list
images_and_labels = list(zip(digits.images, digits.target))

# for every element in the list
for index, (image, label) in enumerate(images_and_labels[:8]):
    # initialize a subplot of 2X4 at the i+1-th position
    plt.subplot(2, 4, index + 1)
    # Display images in all subplots
    plt.imshow(image, cmap=plt.cm.gray_r,interpolation='nearest')
    # Add a title to each subplot
    plt.title('Training: ' + str(label))

# Show the plot
plt.show()


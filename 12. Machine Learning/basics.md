# Machine Learning 
Machine learning is a type of artificial intelligence that allows software applications to learn from the data and become more accurate in predicting outcomes without human intervention.

Their are three types of machine learning:
- Supervised Learning
- Unsupervised Learning
- Reinforcement learning


## 1. Supervised Learning
This is a process of an algorithm learning from the training dataset. Supervised learning is where you generate a mapping function between the input variable (X) and an output variable (Y) and you use an algorithm to generate a function between them. 
It is also known as predictive modeling which refers to a process of making predictions using the data. Some of the algorithms include:
1. Linear Regression 
2. Logistic Regression
3. Decision tree
4. Random forest
5. Naive Bayes classifier
6. Support vector machine (SVM)
7. K-Nearest Neighbor(KNN)

### 1.1 Linear Regression 
Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting. 
Linear regression performs the task to predict a dependent variable value (y) based on a given independent variable (x). So, this regression technique finds out a linear relationship between x (input) and y(output). Hence, the name is Linear Regression.

### 1.2. Logistic Regression 
Logistic Regression produces results in a binary format which is used to predict the outcome of a categorical dependent variable. It is most widely used when the dependent variable is binary i.e, the number of available categories is two such as, the usual outputs of logistic regression are:
- Yes and No
- True and False
- High and Low
- Pass and Fail

### 1.3. Decision tree
A decision tree builds tree branches in a hierarchical approach and each branch can be considered as an if-else statement. The branches develop by partitioning the dataset into subsets based on the most important features.

### 1.4. Random forest
As the name suggests, a random forest is a collection of decision trees.
It is a common type of ensemble method which aggregates results from multiple predictors.

### 1.5. Naive Bayes classifier
It is not a single algorithm but a family of algorithms where all of them share a common principle, i.e. every pair of features being classified is independent of each other.

### 1.6  Support vector machine (SVM)
Support vector machine finds the best way to classify the data based on the position in relation to a border between positive class and negative class.
This border is known as the hyperplane which maximizes the distance between data points from different classes

### 1.7. K-Nearest Neighbour (KNN)
KNN works by finding the distances between a query and all the examples in the data, selecting the specified number of examples (K) closest to the query, then voting for the most frequent label.



## Unsupervised Learning
In Unsupervised Learning, the data contains only the inputs, and the algorithms look for the structures and patterns in the data.
This is a process where a model is trained using information which is not labeled. This process can be used to cluster the input data in classes on the basis of their statistical properties. Unsupervised learning is also called as clustering analysis which means the grouping of objects based on the information found in the data describing the objects or their relationship. The goal is that objects in one group should be similar to each other but different from objects in another group. Some of the algorithms include:
1. K-means clustering
2. Hierarchical clustering 



## Reinforcement learning
This area is concerned with software taking actions based on some kind of cumulative reward. These algorithms do not assume knowledge of an exact mathematical model and are used when exact models are unavailable. 
Reinforcement learning is learning by interacting with space or an environment. An RL agent learns from the consequences of its actions, rather than from being taught explicitly. It selects its actions on basis of its past experiences (exploitation) and also by new choices (exploration).



## Python tools for MACHINE LEARNING
- Scikit learn
- TensorFlow
-


### Scikit learn
- It provides a range of supervised and unsupervised learning algorithms in Python
-




## Ensemble Models
Ensemble models is a machine learning approach to combine multiple other models in the prediction process. Those models are referred to as base estimators. It is a solution to overcome the following technical challenges of building a single estimator:
- **High variance:** The model is very sensitive to the provided inputs to the learned features.
- **Low accuracy:** One model or one algorithm to fit the entire training data might not be good enough to meet expectations.
- **Features noise and bias:** The model relies heavily on one or a few features while making a prediction.

### Ensemble Algorithm
If we build and combine multiple models, the overall accuracy could get boosted. The combination can be implemented by aggregating the output from each model with two objectives: 
- reducing the model error and 
- maintaining its generalization. 
The way to implement such aggregation can be achieved using some techniques, such as meta-algorithms.

### Ensemble Learning
we could build multiple C45 models where each model is learning a specific pattern specialized in predicting one aspect. Those models are called weak learners that can be used to obtain a meta-model. 
In this architecture of ensemble learners, the inputs are passed to each weak learner while collecting their predictions. The combined prediction can be used to build a final ensemble model.

### Ensemble Techniques

#### Bagging
The idea of bagging is based on making the training data available to an iterative process of learning. Each model learns the error produced by the previous model using a slightly different subset of the training dataset. Bagging reduces variance and minimizes overfitting. Examples of such a technique:
- Bootstrapping:
- Random Forest
- Extra-Trees Ensemble

#### Boosting
- **Adaptive Boosting (AdaBoost)** - is an ensemble of algorithms, where we build models on the top of several weak learners [1].
- **Gradient Boosting** - Gradient boosting algorithms are great techniques that have high predictive performance. Xgboost [2], LightGBM [3], and CatBoost are popular boosting algorithms that can be used for regression and classification problems. 

#### Stacking
Stacking is similar to boosting models; they produce more robust predictors. Stacking is a process of learning how to create such a stronger model from all weak learners’ predictions.

#### Blending
Very similar to the stacking approach, except the final model is learning the validation and testing dataset along with predictions. Hence, the features used is extended to include the validation set.

#### Classification Problems
Since classification is simply a categorization process. If we have multiple labels, we need to decide: shall we build a single multi-label classifier? or shall we build multiple binary classifiers? If we decided to build a number of binary classifiers, we need to interpret each model prediction.

#### Regression Problems
In regression problems, we are not dealing with yes or no questions. We need to find the best predicted numerical values. We can average the collected predictions.

#### Aggregating Predictions
When we ensemble multiple algorithms to adapt the prediction process to combine multiple models, we need an aggregating method. Three main techniques can be used:
- **Max Voting:** The final prediction in this technique is made based on majority voting for classification problems.
- **Averaging:** Typically used for regression problems where predictions are averaged. The probability can be used as well, for instance, in averaging the final classification.
- **Weighted Average:** Sometimes, we need to give weights to some models/algorithms when producing the final predictions.





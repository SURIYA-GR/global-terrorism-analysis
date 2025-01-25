"# global-terrorism-analysis" 

Link for the dataset 
https://www.kaggle.com/datasets/itssuru/global-terrorism?resource=download

Data Preprocessing: 
We have obtained data from the Organization called START along with a 
Codebook. In the codebook they have mentioned how the missing values are 
represented. We have selected the attributes which have the missing values less 
than 40 percent. The Missing values has been filled with appropriate values. 

Data Cleansing:  
Listed out the number of Categorical attributes and converted their data type into 
category data type. Filled the missing values using Simple Mean and Median 
Imputation and dropped some which has some Null values. 

Weapon Classification: 
Used KNN algorithm to categorize the Weapons used during the attack. Firstly, 
we must split the training and testing data set. And we have calculated the training 
and testing accuracy for different k values and found out the best k value by 
plotting a graph between training and testing accuracy. Lastly created a model for 
different best k value.
 
Time Series Prediction: 
We have analysed the attacks happened in Iraq and Created Time series model 
using Facebook’s Prophet and Predicted the Future attacks. 

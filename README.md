
# KC Houses Business Insights
![image](https://user-images.githubusercontent.com/80731935/138966516-52284254-e7c0-4186-8c6a-524156b9910e.png)

Insights projct to help in the purchase houses dicision.
EDA + Short Report. To see complete analysis and report check the files : KC_Houses.iýnb and KC_Houses_Business_Insights.pdf

## Abstract
<p style = "text-align: Justify">
The aim of the project is to define the best transactions opportunities within the portfolio. To find what houses should be bought, two approach were taken. First, a general comparison between houses with same condition and same region was done. With this approach the estimated profit was, in average, from 15% up to 65%. The second approach takes the effects of the houses features to refine the analysis trying to find high profitable opportunities. Based in the houses features, 10 hypothesis were checked, and for the validated hypothesis the estimated profit, in average, was 25%. Was found the 91% of the houses are in condition 3 and 4. That shows the people preference, and trading with those houses will be easier. Houses built after 2010 are all in condition 3, but the price can be higher than houses built before, even in better condition, what can generate good trade opportunities.
<p>
 
 ## Tabel of Contents
 ![image](https://user-images.githubusercontent.com/80731935/138963852-3c5eb017-478f-4f0a-a01d-326684a58f35.png)


## 1. Introduction
From the historical data of houses sold between may 2014 and may 2015 in King County Washington State, USA, a data set was built and provide the information for this work. By help decision of houses buying process can improve the profit. So, this project intent to help in that decision.
 
## 2. Problem statement
The aim of this project is to generate insights to help in decision of house acquisition and or trade based on statistic variation of prices and houses features.


 ## 3 . Methodology
Was adopted a criterion to defines a trade opportunities as following: the trade opportunities are all the houses that have the price lower than the median price, attending the premise ahead:
  
### Premises and assumptions:
 - The price comparison will be made only for houses with same condition and in the same region (zip code).</br>
 - The outliers will be removed from the data frame considering the price column, and will not be analyzed.</br>
 - The profit was estimated considering the houses should be sold by the median price.</br>

The trade opportunities were selected using two different approach. The first one, was to get the total data frame grouped the data by condition and region and evaluate the median price for each case. Then,  the price of each house was compared with the median price, for a given condition and region , and selecting the trade opportunities. In the second approach a set of hypothesis, based in the houses features, was checked trying to find specifics and high profitable opportunities. The set of hypothesis are in the table bellow.

**Table 1:** Set of hypothesis.</br>
 ![image](https://user-images.githubusercontent.com/80731935/138778563-f08916b2-9248-4ec3-b612-e0a137730358.png)
 
 ## 3 . Results.
### Median price per condition
As there are five different house conditions, it is important to know how the prices behaves depends the houses conditions and the number of houses per condition. Lets visualize that.
 
 ![image](https://user-images.githubusercontent.com/80731935/138779610-b38e2bd6-10e9-4e35-9afc-1c424ca16510.png)
 
<p style = "text-align: justify">As wee can see, the house's price increases with the increase of the number that represents the house condition, indicating that the highest number the better house condition. </p>
The most part of the houses are in the condition 3 and 4, being 65% of houses in condition 3 and 26% in condition 4 </br>


### Profit Estimatin for the first approach.
Using the grouped data by condition and regions, lets define two new features for the houses:</br>
**Status:** that defines if a house should be bought or not. 
**x% lower:** that shows the discount, in other words, how much the house's price is lower the than median price for a given condition and region.
Looking fot houses with status Buy let's visualize the dsicount distribution.
![image](https://user-images.githubusercontent.com/80731935/138861035-1f2f9f4f-64fb-4dab-bd9f-9a99a48ecfdf.png)

By the chart and the table we can conclude:</br>
    • There are 10113 houses with price lower than the median prices.</br>
    • For these 10113 houses, in average, the prices are about 19% lower than the median prices, for a given region and condition.</br>
    • 25% of the houses are with prices equal or lower than 27% of the median prices.</br>
      
Based in the above conclusions, the data status will gain a new definition as follow:</br>
    • If the discount is 27% or higher, the status will be changed to Buy_SRP, that means Strongly Recommended Purchase.</br>
    • The set of houses out of the set of best opportunities, was called regular opportunities.</br>
    
The profit estimation was done with two sets of data: the best opportunities and regular opportunities.See bolow the averaged profit estimation for each case.

**Profit estimation**</br>
**Regular opportunities:</br>**
Averaged estimated profit = 15%</br></br>
**Best opportunities:</br>**
Averaged  estimated profit = 65%</br></br>

### Profit Estimatin for the second approach.
Now, let’s check the set of hypothesis. The aim of these hypothesis is to refine the analysis and try to find specific high profitable opportunities.
The table ahead shows the retsults for the validated hypothesis. (The complete analysis and conclusion for each hypothesis see the Jupyter Notebook KC_Houses.iýnb and the report KC_Houses_Business_Insights.pdf)

**Table 2:** Results of the donfirmed hypothesis.</br>
 ![image](https://user-images.githubusercontent.com/80731935/138780033-3a1760d3-0367-4c2b-96e1-daf8ea46356d.png)
 
 For each case, and included the general approach shown in the beginning of the report, a data set was generated. The files were named as sample_”name”.csv. For instance, for houses that attend the hypothesis H1 the file was named as “sample_h1.csv”, and so on. The files are in the dataset folder, and was used in the dashboard built in the streamlit library.
 ## 4. Discussion
The most part of the houses are in the condition 3 and 4, being 65% of houses in condition 3 and 26% in condition 4. So, there are more trade opportunities with houses in conditions 3 and 4. The business should focus in that kind of houses, due to the highest probability of trade. The conditions 1 and 2 should be discarded, or very well analyzed in each case before buy a house. Considering condition 5, let’s say those houses are high level houses and there is a specific group of clients for them, and the House Rocket should focus a small part of the houses in those houses condition.
In the general approach were found 10113 trade opportunities. So, the number of houses found in the hypothesis, or probably in total, inside the set of houses taken for the first approach. So, looking for data from the hypothesis, we are looking for specific opportunities.
The hypothesis 1 (H1) presents the highest profitable approach. Although, the estimated profit found in the hypothesis 8 is approximately the average of the estimated profit of the general approach and probably don’t represent the effect of the living room area in the price.
In terms of number of bathrooms, the must part of the houses has 1 or more and 2.5 or less bathrooms, indication the preference of people for that feature.

## 5. Conclusion
The companies should focus the business in houses with condition 3 and 4, that represents 91% of total portfolio. 
Houses with condition 1 and 2 should be discarded, or very well analyzed before be bought.
The major part of the houses has at lest one bathroom. The companies should focus the business in houses the have at least one bathroom to increase the probability of trade.
Considering the definition of profit estimation, houses with water front presents the highest estimated profit, being 25%, in average.
Houses built after 2010, are in condition 3, but the price can be higher than houses built before, even in better condition. Buying houses built after 2010, can create good and profitable opportunities.

## 6. Next Steps
To compare the approach of median price with the averaged price for the profit estimation.</br>
Create prediction models for help in the decision of house to be bought.</br>
Create a prediction models for help to find the best moment to buy the houses.</br>
 

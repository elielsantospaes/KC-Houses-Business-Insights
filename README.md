
# KC Houses Business Insights
Projeto de insights sobre compra e venda de imóveis de modo a maximizar os lucros nas operações.

## Abstract
<p style = "text-align: Justify">
The aim of the project is to define the best transactions opportunities within the portfolio. To find what houses should be bought, two approach were taken. First, a general comparison between houses with same condition and same region was done. With this approach the estimated profit was, in average, from 15% up to 65%. The second approach takes the effects of the houses features to refine the analysis trying to find high profitable opportunities. Based in the houses features, 10 hypothesis were checked, and for the validated hypothesis the estimated profit, in average, was 25%. Was found the 91% of the houses are in condition 3 and 4. That shows the people preference, and trading with those houses will be easier. Houses built after 2010 are all in condition 3, but the price can be higher than houses built before, even in better condition, what can generate good trade opportunities.
<p>
 

## 1. Introduction

### Business understanding.
The buy and sold houses has been made by companies 
A dateset with a historical houses sold between May 2014 to May 2015 in King County, Washington State, USA, was used. 
We will predict the sales of houses in King County with an accuracy of at least 75-80% and understand which factors are responsible for higher property value - $650K and above.”


  ## 2 . Methodology
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

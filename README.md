
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
 
 ### Profit Estimatin for the first approach.

**Table 2:** Results of the donfirmed hypothesis.
 ![image](https://user-images.githubusercontent.com/80731935/138780033-3a1760d3-0367-4c2b-96e1-daf8ea46356d.png)

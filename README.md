# BMW Demand-Product Specification optimization Project (Borusan)
With the knowledge of
* Current stock data 
* Orders that were given from previous months.
* Previous sales & stock information

Objective
* Minimize total level of remaining product stocks without having stock-outs.
* Equalize the stock turnover ratios for different spec combinations of same product.

How
* By predicting correct number of future sales.
* By estimating correct distribution of product orders with different specifications.

## Presentation Link
[Presentation to the Customer](https://docs.google.com/presentation/d/1FoMEiofoiogqMjufqdAnbCBDa0-nQ2fz/edit?usp=sharing&ouid=118227050300879592526&rtpof=true&sd=true)

## File Structure
* InitialResultsWithPOCdata: This folder includes codes and results taken with POC data.
* noNeedCodes: This folder contains code that was implemented during the project that did not work well. Codes will not be used.
* AzurePipeline: This folder shows deployment codes to use in the Azure environment. An ML pipeline is created for this.
* Notebooks: These files are up-to-date codes.

## Code Structure
1. initial.py: The notebook includes merging process of input datasets. There are lots of input datasets such as genel infos about products, prices, specifications, model and seri infos. It outputs one main csv file that includes all necessary attributes about products.
2. paketGruplama.py: The notebook includes algorithm for grouping design packages of products. We need to group design packages, because design packages id and definition may change in the past. It also includes some preprocessing steps. It outputs one csv file that is preprocessed input data.
3. modelPaketSaleCount-Prediction.py: The notebook consists of five process,
  * Feature extraction process by using utils.py 
  * Model sales count prediction
  * Design packages sale rate prediction based on models
  * Merge previous two steps to obtain design package sale count prediction
  * Order distribution optimization algorithms and performance metrics
4. modelKombinJantIçkaplamaSiparisDagilim.py: The notebook includes order distribution of lower breakdowns such as color, upholster, rin, and interior lining. The algorithm is rule based. We did not use ML for this. It is implemented according to one month sales and presold inputs.

## Code parameters
* model_start_date: For ML algorithms, from which date the data will be used. We used the dataset from 2019 July.
* pred_range: After how many months will the order be placed? If you are at the end of September and you want to plan orders for November, the parameter will be 2. If you want to plan orders for December, the parameter will be 3.

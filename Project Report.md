## Overview
This project analyzes large financial datasets from two stocks (e.g., Microsoft and Apple), focusing on identifying patterns and detecting anomalies. Specifically, the analysis involves detecting the periods of maximum gain or loss using the divide-and-conquer approach, sorting data using merge sort, and detecting anomalies in volume vs. price data using a closest pair of points algorithm. 

This reports explains the purpose and functionality of each part of the code and why specific algorithms were used as well as a detailed explanation of the results.

##
### 1. Merge Sort for Sorting Data by Date

**Function:** `mergeSort(arr, indices)`

**Purpose:** This function ensures that the stock data is chronologically sorted based on the `Date` column. Sorting the data is essential for time-series analysis because it ensures the price and volume changes are calculated in the correct orer.

**How it works:**
- The function recursively divides the array into two halves (left and right) until the size of the subarrays is 1 (base case of recursion).
- After dividing the array, it merges the subarrays back in sorted order while maintaining their original indices.
- By applying this method, the stock data is efficiently sorted based on the `Date` column, ensuring that later calculations, such as maximum gain periods are performed accurately.
    
##
### 2. Maxium Subarray (1D) - Kadane's Algorithm

**Function:** `maxSubarray1D(arr)`
   
**Purpose:** This function identifies the maximum gain or loss period for a single stock by analyzing its daily price changes. The algorithm is a divide-and-conquer version of Kadane's algorithm, which finds the maximum sum of a contiguous subarray.

**How it works:**
- The algorithm recursively divides the array of daily price changes into two halves and computes the maximum subarray sum for the left half, the right half, and the subarray that crosses the midpoint.
- It selects the maximum of these three values, returning the start and end indices of the subarray and the sum of the maximum gain during that period.
- This method is applied individually to each stock to determine the period where the stock experienced the greatest overall gain (or least loss).
     
##  
### 3. Maximum Subarray (2D) - Combined Stock Analysis

**Function:** `maxSubarray2d(matrix)`
   
**Purpose:** this funciton extends the 1D maximum subarray algorithm to handle two stocks simultaneously by using a 2D matrix of their daily price changes. It identifies the combined maximum gain period for both Microsoft and Apple, showing which stock contributed the most during this period.

**How it works:**
- The 2D matrix cntains daily price changes for Microsoft and Apple. The function iterates through pairs of columns (days) and compresses the rows into a 1D array (sum of the price changes for both stocks on those days).
- The `maxSubarray1D` function is then applied to this compressed array to find the maximum gain across both stocks for each column pair.
- The final results is the period (start and end indices) wehre the combined price changes of both stocks resulted in the largest overall gain, along with the contribution from each stock.

##
### 4. Closest Pair of Points (Divide and Conquer)

**Function:** `closestPairDC(points)`
   
**Purpose:** This function identifies anomalies in the data by finding the two closest points (in terms of Euclidean distance) in the volume and price data. Closest pairs of points may reveal potential market anomalies, such as unusual price movements with minimal volume changes.
   
**How it works:**
- Euclidean Distance Calculation: The distance between two points is calculated using the Euclidean distance formula, which measures how close two points (volume, price pairs) are in 2D space.
- Brute Force for Small Datasets: For smaller datasets (3 or fewer points), the algorithm uses brute force to find the closest pair by calculating the distance between all possible pairs.
- Divide and Conquer: For larger datasets, the algorithm splits the points into left and right halves, recursively finding the closest pair in each half. It also checks for closest pairs across the midpoint using a strip of points within a small distance (`delta`) from the midpoint.
- The function returns the closest pair of points and the distance between them.

**Why it's important:**
- The closest pair algorithm highlights points (volume, price) that are unusually close in terms of volume but may have significantly different prices, or vice versa. This may indicate market inefficiencies, volatility, or unusual trading behavior.

##
### 5. Closest Pair Formatting

**Function:** `closestPairFormat(pair, distance)`
   
**Purpose:** This helper function formats the output of the closest pair results to make it more readable. It converts the scientific notation of volumes and prices into human-readable format and prints the distance between the closest points.

##
### 6. Plotting Stock Performance

**Funcion:** `plotStockPerformance(data, start, end, stock1, stock2)`
  
**Purpose:** This function visualizes the stock price performance for Microsoft and Apple, highlighting the period of maximum gain as a shaded region on the plot.
  
**How it works:**
- It plots the closing prices of both stocks over time, with Date on the x-axis and the closing prices on the y-axis.
- The maximum gain period is highlighted using a shaded region (axvspan) between the start and end dates.
- The plot provides a clear visual representation of when the stocks performed best, helping users quickly identify important time periods for both stocks.

##
### 7. Main Analysis Function

**Function:** `analyzeData(mcsft_file, apple_file)`
   
**Purpose:** This is the main function that ties everything together. It loads the stock data for Microsoft and Apple, processes the data, performs the analysis, and displays the results.
   
**How it works:**
- The stock data is loaded from CSV files, and the Date column is converted to a datetime format to allow for chronological sorting and merging of datasets.
- It uses `mergeSort` to ensure that the data is in chronological order.
- The `maxSubarray1D` function is used to find the maximum gain period for each stock individually.
- The `maxSubarray2D` function identifies the combined maximum gain period across both stocks.
- The function also detects anomalies by calculating the closest pair of points (volume vs. price) for both stocks using the `closestPairDC` function.
- Finally, it prints the results and plots the stock performance, highlighting the maximum gain period.

## 
This code provides a comprehensive analysis of stock performance by identifying periods of maximum gain using Kadane’s algorithm in both 1D (for individual stocks) and 2D (for combined stock data). It also detects anomalies in volume and price data using a divide-and-conquer closest pair algorithm. The use of merge sort ensures the chronological integrity of the data, and the visualization helps highlight key trends in stock performance. This multi-faceted approach allows users to analyze stock data for patterns, detect potential anomalies, and make data-driven decisions.


## Results and Explanation

### 1. Maximum Combined Period

**Result**

- **Start Date:** 2015-08-25
- **End Date:** 2024-07-10
- **Maximum Combined Gain:** 632.82

**Explanation**

The **combined maximum gain** refers to the period where **both Microsoft and Apple** together experienced the highest overall increase in stock prices. This gain is calculated by summing the proce changes for both stocks during this period.

The maximum combined gain occured betwen **August 25, 2015** and **July 10, 2024**. During this time, both stocks contributed a total gain of approximately **632.82**.

This indicates that during this nearly nine-year period, the combined performanced of both stocks was highly positive, reflecting strong growth across both companies.

**Contribution Breakdown:**

**Microsoft Contribution:** 425.78
**Apple Contribution:** 207.05

Microsoft contributed the larger share of the combined gain during this period, accounting for approximately **67%** of the total gain. Apple, while also growing significantly, contributed **33%** of the total gain. This suggests that **Microsoft's stock had a larger growth trajectory** over this period compared to Apple.

##
### 2. Individual Maxiumum Gain Periods

**Microsoft**

- **Start Date:** 2015-04-02
- **End Date:** 2024-07-05
- **Maximum Gain:** 427.27

**Apple**

- **Start Date:** 2026-05-12
- **End Date:** 2014-07-16
- **Maximum Gain:** 212.24

**Explanation:**

These individual results show the **maximum gain periods** for Microsoft and Apple when analyzed separately.
For **Microsoft**, the period between **April 2, 2015** and **July 5, 2024**, resulted in a maximum gain of **427.27**.
For **Apple**, the period between **May 12, 2016** and **July 16, 2024**, resulted in a maximum gain of **212.24**.

From these results, it is clear that **Microsoft** had a much larger individual maximum gain over its peak period compared to Apple. This suggets that **Microsoft's stock performed better** on its own during this period.

**Why Different Dates?**

The **maximum gain periods** for each stock do not fully align because the stocks likely experienced their peak growth at different times. Microsoft's stock began its maximum gain period earlier (April 2015), while Apple's strongest growth started about a year later (May 2016)

##
### Microsoft vs Apple Comparison

**Observation**
- Microsoft had a larger individual maximum gain, **427.27**, compared to Apple's **212.24**.

This highlights that **Microsoft** showed stronger price growth over its peak period, controbuting more to the overall combined gain as well. Apple still experienced significant growth but lagged behind Microsoft during this time.

##
### Anomalies Detected via Closest Pair of Points

The **closest pair algorithm** was used to detect potential anomalies in volume and price data. These anomalies may indicate unusual trading patterns where significant price changes occurred with minimal change in trading volume, or vice versa.

**Microsoft Closest Pair**
- **Volume 1:** 17,270,990 | **Price 1:** 73.26
- **Volume 2:** 17,271,101 | **Price 2:** 57.62
- **Distance:** 25.39

**Explanation**

The closest pair for Microsoft shows tow very close trading volumes (a differene of just **20** shares), but the prices between these two data points diff significantly— by about **$15.64**.

This suggests that despite a very minor difference in trading volume, the stock price dropped notably from **$17.26** to **$56.62**. Such a scenario might indicate **market volatility**, where external factors influenced price significantly without impacting trading volume much. This could be a signal or **price inefficiency** or an unsusual market response.

**Apple Closest Pair**
- **Volume 1:** 94,259,720 | **Price 1:** 43.75
- **Volume 2:** 94,359,810 | **Price 2:** 128.70
- **Distance:** 123.76

**Explanation**

For Apple, the closest pair of points shows nearly identical volumes but a massive price difference of **$84.95**. This suggests a similar pattern where large price movements ocurred without much change in trading volume. The distance between these two data points (123.76) is much larger than Microsoft's, indicating a **significant market anomaly** for Apple.

Such a large discrepancy coulld reflect **external events** like product releases, earnings reports, or macroeconomics factors that drastically altered Apple's stock price without affecting the volume much.

##
### Overall Insights
**1. Microsoft Dominated the Combined Maximum Gain**
- Microsoft was the major contributor to the combined gain during the maximum gain period, accounting for about 67% of the total gain.
- The individual maximum gain periods for each stock do not overlap exactly, indicating that each stock experienced its peak growth at different times.
**2. Anomalies Detected in Both Stocks**
- The closest pair analysis highlights anomalies where significant price movements occured with minimal changes in volume. For both Microsoft and Apple, these price discrepancies suggest moments of **market volatility** or potential inefficiencies.
- Apple's anomaly (with a much larger price difference) suggests a **bigger price shock** occurred without a corresponding volume change, which could indicate a market event or external factor affecting the stock price.

##
The analysis demonstrates that Microsoft had a larger impact on the combined stock performance during the maximum gain period. While both stocks showed strong growth, Microsoft's stock had a greater individual maximum gain. Additinoally, the closest pair analysis revealed potential anomalies in the trading behavior of both stocks, suggesting moments of market volatility or unusual pricing patterns. These findings provide valuable insights into stock performance and potential risks associated with price fluctuations.

##

<img width="994" alt="Screenshot 2024-10-20 at 7 19 11 PM" src="https://github.com/user-attachments/assets/7873055a-801d-4401-a4d6-cd8ff1816df1">


This graph shows the price performance of **Microsoft** (blue) and Apple (orange) over time, with the **maximum gain period** highlighted in green. 

The following is a detailed analysis of the graph:

**1. Stock Price Trends**

**Microsoft**
- The blue line represents Microsoft’s stock price performance from around 2014 through 2024.
- From 2015 onwards, Microsoft’s stock shows steady growth, with significant increases starting in 2016.
- There is a large upward trajectory around 2020, which aligns with the stock market rally in response to technology company growth during and after the COVID-19 pandemic.
- After peaking in 2021, there are some corrections in 2022, followed by a partial recovery.

**Apple**
- The orange line represents Apple’s stock price performance over the same time frame.
- Similar to Microsoft, Apple shows steady growth starting around 2015. However, the magnitude of the price increase is less than Microsoft's.
- Around 2020, Apple also experiences significant growth, though not as dramatic as Microsoft’s.
- Post-2021, Apple also shows a dip, followed by a moderate recovery into 2024.

**2. Maximum Gain Period**
- The green shaded region marks the period identified as the **maximum gain period**, which extends from **2015** to **2024**.
- During this period, both stocks experienced considerable growth, though Microsoft’s stock price growth was more substantial than Apple’s.
- Notably, Microsoft’s stock price had a larger increase over this period, consistent with the data showing that **Microsoft contributed more** to the combined maximum gain.
- The shaded area indicates that most of the price growth, especially for Microsoft, happened after 2015, which corresponds to the beginning of the maximum gain period.

**3. Key Observations**
- **Microsoft’s Dominance**: Microsoft’s stock price is consistently higher than Apple’s throughout the entire period. The steep climb from 2019 to 2021 is particularly notable, where Microsoft’s price surged far beyond Apple’s.
- **COVID-19 Impact**: Both stocks show a significant upward trend around 2020, which could be linked to the surge in demand for technology services and products during the pandemic.
- **Volatility Post-2021**: After peaking in 2021, both stocks show some corrections (price drops) in 2022. These corrections reflect broader market behavior, including reactions to inflation concerns, interest rate hikes, and other macroeconomic factors.
- **Partial Recovery**: By 2023–2024, both stocks show signs of recovery, although the growth rate is slower than the pre-2021 period.

**3. Comparison**
- **Growth Rate**: While both stocks have shown growth, Microsoft’s price has increased more rapidly compared to Apple. This is consistent with the results of the analysis, where Microsoft had a larger individual maximum gain.
- **Volatility**: Both stocks show some level of volatility, with periods of sharp price increases and corrections, but the general long-term trend for both is upward.
- **Apple’s Consistency**: Apple’s growth is more gradual compared to Microsoft. It shows fewer dramatic peaks, indicating that its stock has been more consistent over time, but with less explosive growth than Microsoft.

##
This graph visually supports the analysis of the maximum gain period and the contributions of Microsoft and Apple. Microsoft’s stock experienced a sharper and more significant rise, particularly after 2015, making it the major contributor to the combined maximum gain. Apple, while still growing, did not experience the same level of explosive growth. Both stocks demonstrate typical market behavior with rapid growth periods, corrections, and eventual recoveries, particularly after the pandemic.


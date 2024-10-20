import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
import math


# Use Merge Sort to sort data by date; ensures data is in chronological order
def mergeSort(arr, indices):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        leftIndices = indices[:mid]
        rightIndices = indices[mid:]

        # Recursively divide the array and merge the halves
        mergeSort(left, leftIndices)
        mergeSort(right, rightIndices)

        i = j = k = 0

        # Merge left and right arrays while maintaining order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                indices[k] = leftIndices[i]
                i += 1
            else:
                arr[k] = right[j]
                indices[k] = rightIndices[j]
                j += 1
            k += 1

        # merge any remaining elements
        while i < len(left):
            arr[k] = left[i]
            indices[k] = leftIndices[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            indices[k] = rightIndices[j]
            j += 1
            k += 1
    return indices


# 1D Maximum Subarray (Kadane’s Algorithm using Divide and Conquer)
# Function finds the maximum gain period in 1D (individual stock data)
def maxSubarray1D(arr):
    # Helper function to find max crossing subarray
    def maxCrossingSubarray(arr, low, mid, high):
        leftSum = float('-inf')
        total = 0
        maxLeft = mid
        for i in range(mid, low - 1, -1):
            total += arr[i]
            if total > leftSum:
                leftSum = total
                maxLeft = i

        rightSum = float('-inf')
        total = 0
        maxRight = mid + 1
        for j in range(mid + 1, high + 1):
            total += arr[j]
            if total > rightSum:
                rightSum = total
                maxRight = j

        return maxLeft, maxRight, leftSum + rightSum

    # Recursive function to find max subarray
    def maxSubarray(arr, low, high):
        if low == high:
            return low, high, arr[low]
        else:
            mid = (low + high) // 2
            leftLow, leftHigh, leftSum = maxSubarray(arr, low, mid)
            rightLow, rightHigh, rightSum = maxSubarray(arr, mid + 1, high)
            crossLow, crossHigh, crossSum = maxCrossingSubarray(arr, low, mid, high)

            if leftSum >= rightSum and leftSum >= crossSum:
                return leftLow, leftHigh, leftSum
            elif rightSum >= leftSum and rightSum >= crossSum:
                return rightLow, rightHigh, rightSum
            else:
                return crossLow, crossHigh, crossSum

    return maxSubarray(arr, 0, len(arr) - 1)


# 2D Maximum Subarray for combined analysis of two stocks
# Function analyzes max gain period across both stocks
def maxSubarray2D(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    maxSum = float('-inf')
    finalLeft, finalRight, finalTop, finalBottom = 0, 0, 0, 0

    # Iterate through all possible pairs of columns
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            # Compress rows by adding current column values
            for i in range(rows):
                temp[i] += matrix[i][right]

            # Use 1D max subarray to find the best subarray in the compressed array
            top, bottom, sum_ = maxSubarray1D(temp)

            # Update the best result
            if sum_ > maxSum:
                maxSum = sum_
                finalLeft, finalRight = left, right
                finalTop, finalBottom = top, bottom

    return finalTop, finalBottom, finalLeft, finalRight, maxSum


# Divide and conquer closest pair algorithm
# Function funds the closest pair of points (volume vs price)
def closestPairDC(points):
    # function to calculate Euclidean distance between two points
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # Brute force function to calculate closest distance when points are small
    def bruteForce(points):
        minDistance = float("inf")
        cp = None
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(points[i], points[j])
                if dist < minDistance:
                    minDistance = dist
                    cp = (points[i], points[j])
        return cp, minDistance

    # Function that finds closest points in strip within delta distance
    def closestInStrip(strip, delta):
        minDistance = delta
        cp = None
        # Sort by y coordinate
        strip.sort(key=lambda point: point[1])
        n = len(strip)
        for i in range(n):
            for j in range(i + 1, n):
                # Break if y coordinates are too far apart
                if strip[j][1] - strip[i][1] >= minDistance:
                    break
                dist = distance(strip[i], strip[j])
                if dist < minDistance:
                    minDistance = dist
                    cp = (strip[i], strip[j])
        return cp, minDistance

    # Main recursive function to find closest pair of points
    def closestPairRecursive(pointsSorted):
        n = len(pointsSorted)

        # Base case when there are 3 or fewer points
        if n <= 3:
            return bruteForce(pointsSorted)

        # Divide; split points in half
        mid = n // 2
        midpoint = pointsSorted[mid]

        # Recursively find smallest distance in both left and right halves
        leftHalf = pointsSorted[:mid]
        rightHalf = pointsSorted[mid:]
        closestLeft, deltaLeftHalf = closestPairRecursive(leftHalf)
        closestRight, deltaRightHalf = closestPairRecursive(rightHalf)

        # Find minimum distance in delta distance from midpoint
        delta = min(deltaLeftHalf, deltaRightHalf)
        cp = closestLeft if deltaLeftHalf <= deltaRightHalf else closestRight

        # Create strip of points in delta distance from midpoint
        strip = [point for point in pointsSorted if abs(point[0] - midpoint[0]) < delta]

        # Closest pair in strip and compare with delta
        closestStrip, stripDist = closestInStrip(strip, delta)
        if stripDist < delta:
            return closestStrip, stripDist
        return cp, delta

    # Main function that prepares points and calls recursive function
    def closestPair(points):
        pointsSorted = sorted(points, key=lambda point: point[0])
        return closestPairRecursive(pointsSorted)

    return closestPair(points)


# Plot the stock price performance and maximum gain period
def plotStockPerformance(data, start, end, stock1='Microsoft', stock2='Apple'):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close/Last_msft'], label=f'{stock1} Prices')
    plt.plot(data['Date'], data['Close/Last_apple'], label=f'{stock2} Prices')
    plt.axvspan(data['Date'].iloc[start], data['Date'].iloc[end], color='green', alpha=0.3, label='Max Gain Period')
    plt.title(f"{stock1} and {stock2} Price Performance")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


# Format closest pair for better output readability
def closestPairFormat(pair, distance):
    return f"Volume 1: {pair[0][0]:,.0f}, Price 1: {pair[0][1]:,.2f}\n" \
           f"Volume 2: {pair[1][0]:,.0f}, Price 2: {pair[1][1]:,.2f}\n" \
           f"Distance: {distance:,.2f}"


# Main analysis function to process stock data and detect patterns
def analyzeData(msft_file, apple_file):
    # Load Microsoft and Apple stock data
    msft_data = pd.read_csv(msft_file)
    apple_data = pd.read_csv(apple_file)

    # Convert 'Date' to datetime and align both datasets by date
    msft_data['Date'] = pd.to_datetime(msft_data['Date'])
    apple_data['Date'] = pd.to_datetime(apple_data['Date'])

    # Align the two datasets by their 'Date'
    mergedData = pd.merge(msft_data, apple_data, on='Date', suffixes=('_msft', '_apple'))

    # Apply merge sort on the 'Date' column to maintain chronological order
    sortedIndices = mergeSort(mergedData['Date'].values.copy(), list(range(len(mergedData))))
    mergedData = mergedData.iloc[sortedIndices].reset_index(drop=True)

    # Clean 'Close/Last' columns and convert to float for calculations
    mergedData['Close/Last_msft'] = mergedData['Close/Last_msft'].replace({r'\$': '', ',': ''}, regex=True).astype(
        float)
    mergedData['Close/Last_apple'] = mergedData['Close/Last_apple'].replace({r'\$': '', ',': ''}, regex=True).astype(
        float)

    # Compute daily price changes for both stocks
    msft_changes = np.diff(mergedData['Close/Last_msft'].values)
    apple_changes = np.diff(mergedData['Close/Last_apple'].values)

    # Find individual max gain for Microsoft and Apple
    msft_start, msft_end, msft_maxGain = maxSubarray1D(msft_changes)
    apple_start, apple_end, apple_maxGain = maxSubarray1D(apple_changes)

    # Create a 2D matrix of changes for combined analysis
    matrix = np.vstack((msft_changes, apple_changes))

    # Apply 2D max subarray on the stock data matrix
    top, bottom, left, right, maxGain = maxSubarray2D(matrix)

    # Calculate contributions during the combined max gain period
    msft_contribution = np.sum(msft_changes[left:right + 1])
    apple_contribution = np.sum(apple_changes[left:right + 1])

    # Display maximum combined gain period and contributions
    print(f"Stocks contributing: Microsoft and Apple")
    print(f"Maximum combined gain period: Start Date: {mergedData['Date'].iloc[left]}, End Date: {mergedData['Date'].iloc[right + 1]}")
    print(f"Maximum combined gain: {maxGain}\n")
    print(f"Microsoft contribution during this period: {msft_contribution}")
    print(f"Apple contribution during this period: {apple_contribution}")

    # Compare individual max gains
    print(f"\nIndividual max gain: ")
    print(f"Microsoft max gain period: Start Date: {mergedData['Date'].iloc[msft_start]}, End Date: {mergedData['Date'].iloc[msft_end + 1]}, "
          f"\nMicrosoft max gain: {msft_maxGain}")
    print(f"Apple max gain period: Start Date: {mergedData['Date'].iloc[apple_start]}, End Date: {mergedData['Date'].iloc[apple_end + 1]}, "
          f"\nApple max gain: {apple_maxGain}\n")

    # Determine whether microsoft or apple had a larger max gain
    if msft_maxGain > apple_maxGain:
        print("Microsoft had a larger individual maximum gain.\n")
    else:
        print("Apple had a larger individual maximum gain.\n")

    # Detect anomalies in volume vs. closing price (Microsoft and Apple combined)
    msft_points = np.array(list(zip(mergedData['Volume_msft'].values, mergedData['Close/Last_msft'].values)))
    apple_points = np.array(list(zip(mergedData['Volume_apple'].values, mergedData['Close/Last_apple'].values)))
    combined_points = np.vstack((msft_points, apple_points))

    # Find closest pair of points for Microsoft
    msft_closestPairs, msft_closestDist = closestPairDC(msft_points)
    print(f"Microsoft Closest Pairs:\n{closestPairFormat(msft_closestPairs, msft_closestDist)}\n")

    # Find closest pair of points for Apple
    apple_closestPairs, apple_closestDist = closestPairDC(apple_points)
    print(f"Apple Closest Pairs:\n{closestPairFormat(apple_closestPairs, apple_closestDist)}\n")

    # Plot stock performance and highlight the maximum gain period
    plotStockPerformance(mergedData, left, right)

# Call the function with the file paths for Microsoft and Apple stock data
analyzeData('microsoft.csv', 'apple.csv')
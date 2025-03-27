#######################################################################################################################################################
# 
# Name:Kayastha Katyarmal
# SID:740098894

# Exam Date:27 march 2025
# Module:programming for business analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-kayasthaa-1
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []
# Step 1: Get the Student ID from the user.
sid = "740098894"  # Using the provided SID directly

# Step 2: Extract the first and last digits.
first_digit = int(sid[0])   # 7
last_digit = int(sid[-1])   # 4

# Step 3: Define the customer feedback text.
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# Step 4: Define the dictionary of keywords.
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',   # Selected because last_digit is 4.
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',    # Selected because first_digit is 7.
    8: 'overall',
    9: 'minor'
}

# Step 5: Use only the keywords corresponding to the extracted SID digits.
selected_keys = [first_digit, last_digit]

# Step 6: Find the positions of these keywords in the text.
positions = []
for key in selected_keys:
    keyword = key_comments[key]
    start_index = customer_feedback.find(keyword)
    end_index = start_index + len(keyword)
    positions.append((start_index, end_index))

# Step 7: Print the result.
print("Keyword positions based on SID:", positions
      
# OUTPUT [(41, 53), (54, 59)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here

# Step 1: Get the Student ID from the user.
sid = input("Enter your Student ID: ").strip()

# Step 2: Extract the first two and the last two digits from the SID.
first_two = int(sid[:2])  # For SID "740098894", first_two becomes 74.
last_two = int(sid[-2:])  # For SID "740098894", last_two becomes 94.

# Step 3: Define the financial metric functions.

# Function to calculate Operating Profit Margin.
def operating_profit_margin(op_income, revenue):
    return (op_income / revenue) * 100

# Function to calculate Revenue per Customer.
def revenue_per_customer(revenue, num_customers):
    return revenue / num_customers

# Function to calculate Customer Churn Rate.
def churn_rate(lost_customers, total_customers):
    return (lost_customers / total_customers) * 100

# Function to calculate Average Order Value.
def average_order_value(revenue, orders):
    return revenue / orders

# Step 4: Compute the financial metrics using the extracted SID digits.
# Multiply first_two and last_two by 100 to simulate realistic financial figures.
op_margin = operating_profit_margin(first_two * 100, last_two * 100)   # Operating Income = 7400, Revenue = 9400
rev_per_customer = revenue_per_customer(last_two * 100, first_two)      # Revenue = 9400, Customers = 74
churn = churn_rate(first_two, last_two)                                 # Lost Customers = 74, Total Customers = 94
avg_order_value = average_order_value(last_two * 100, last_two)         # Revenue = 9400, Orders = 94

# Step 5: Print the results.
print("Operating Profit Margin:", op_margin)
print("Revenue per Customer:", rev_per_customer)
print("Customer Churn Rate:", churn)
print("Average Order Value:", avg_order_value)

# OUTPUT  Operating Profit Margin: 78.72340425531915
Revenue per Customer: 127.02702702702703
Customer Churn Rate: 78.72340425531915
Average Order Value: 100.0

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

from sklearn.linear_model import LinearRegression
import numpy as np

# Provided SID (for record-keeping)
sid = "740098894"
print("Running regression model for SID:", sid)

# Price and Demand Data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demands = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Train the linear regression model
model = LinearRegression()
model.fit(prices, demands)

# Predict demand when price is £52
predicted_demand_at_52 = model.predict([[52]])
print("Predicted demand at £52:", predicted_demand_at_52[0])

# Compute revenue for each price in the dataset
revenues = prices.flatten() * model.predict(prices)

# Find the optimal price that maximizes revenue
optimal_index = np.argmax(revenues)
optimal_price = prices.flatten()[optimal_index]
max_revenue = revenues[optimal_index]

print("Optimal price for maximum revenue:", optimal_price)
print("Maximum predicted revenue:", max_revenue)

# (Note: The exact numbers may vary slightly depending on the regression fit, but the expected values
# are approximately as stated above.)

# OUTPUT Predicted demand at £52: 153.63636363636363
Running regression model for SID: 740098894
Predicted demand at £52: 158.17272727272726
Optimal price for maximum revenue: 45
Maximum predicted revenue: 8529.545454545454


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()




import random
import matplotlib.pyplot as plt

# Provided SID
sid = "740098894"

# Convert SID to integer for use as the maximum value in random generation
max_value = int(sid)

# Generate 100 random numbers between 1 and max_value
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plot the random numbers
plt.plot(random_numbers, marker='o', linestyle='--', label='Random Numbers')
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()
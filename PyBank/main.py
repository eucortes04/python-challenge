import os
import csv

#Path to collect dataset
financials_csv_path = os.path.join('Resources','budget_data.csv')

#Reading in CSV
with open(financials_csv_path) as csvfile:
    financials = csv.reader(csvfile, delimiter=",")

    #accounting for header
    csv_header = next(financials)

    #Variables
    totalMonths = 0 #Holds Months count in financials data
    ProfitLossTotal = 0 #Holds total P/L
    greatestProfitMonth = "" #Holds month of highest profit
    greatestProfit = 0 #Holds amount of highest profit
    greatestLossMonth = "" #Holds month of highest loss
    greatestLoss = 0 #Holds amount of highest loss
    previous_PL = 0 #Holds previous amount of P/L for delta calc
    delta_PL = 0 #Holds delta for period
    delta_Total = 0 #Holds total delta for all periods
    

    #iterate through the rows of data (Month-Year , P/L)
    for row in financials:
        #Adding to the month count
        totalMonths +=1

        #Storing current period changes information
        current_PL = int(row[1]) #profit/loss
        month = row[0] #month
        if previous_PL !=0: #skipping first row since there is no previous month for accurate calculation of delta
            delta_PL = current_PL-previous_PL #calc current period delta
            delta_Total +=delta_PL #Adding to total delta for all periods
        previous_PL = current_PL #setting previous P/L for next row

        #Adding to the net P/L
        ProfitLossTotal += current_PL
 
        #Finding greatest Profit
        if delta_PL>greatestProfit:
            greatestProfitMonth = month
            greatestProfit = delta_PL
        #Finding greatest Loss
        if delta_PL<greatestLoss:
            greatestLossMonth = month
            greatestLoss = delta_PL

    #Average change delta total/ total periods (months-1) rounded to 2 decimal places
    #Print out Analysis
    analysisText = f'''
    Financial Analysis
    --------------------------
    Total Months: {totalMonths}
    Total: ${ProfitLossTotal}
    Average Change: ${round(delta_Total/(totalMonths-1),2)} 
    Greatest Increase in Profits: {greatestProfitMonth} (${greatestProfit})
    Greatest Decrease in Profits: {greatestLossMonth} (${greatestLoss})'''

    print(analysisText)
    
    #write analysis Activity 10,12
    output_path = os.path.join("analysis","analysis_output.txt")

    with open(output_path, 'w') as analysisDoc:
        analysisDoc.write(analysisText)

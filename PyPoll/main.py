import os
import csv

#Path to collect dataset
poll_csv_path = os.path.join('Resources','election_data.csv')
print(poll_csv_path)
#Reading in CSV

with open(poll_csv_path) as csvfile:
    poll_results = csv.reader(csvfile,delimiter=",")

    #accounting for header
    csv_header = next(poll_results)

    #Variables
    totalVotes = 0 #holds total votes
    Results = {} #holds election results (candidate, votes)

    #iterate through the rows of data(voterID,county, candidate)
    for row in poll_results:
        #Adding to total vote count
        totalVotes +=1
        
        #current vote candidate
        candidate = row[2]

        #Candidate counts
        if candidate in Results: #if candidate is in the dictionary
            Results[candidate] +=1 #add to vote count
        else:                   #if candidate is not in dictionary
            Results[candidate] = 1 #add and make count 1

    #Election results top half vote count
    totalVotesText = f'''Election Results
------------------------
Total Votes: {totalVotes}
------------------------
'''
    #Election results bottom half winner
    winnerText = f'''------------------------
Winner: {max(Results,key=Results.get)}
------------------------'''
    
    #printing out above text and looping through dictionary
    print(totalVotesText) #print title and vote count
    for x,y in Results.items(): #loop through dictionary
        print(f'{x}: {round((y/totalVotes)*100,1)}% ({y})') #print candidate, %votes, vote count
    print(winnerText) #print winner

    #write results to file
    output_path = os.path.join("analysis","poll_results.txt")

    with open(output_path,'w') as poll_results:
        poll_results.write(totalVotesText)
        for x,y in Results.items():
            print(f'''{x}: {round((y/totalVotes)*100,1)}% ({y})''',file=poll_results)
        poll_results.write(winnerText)




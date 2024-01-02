import os
import csv

filepath = os.path.join('resources', 'election_data.csv')

totalVotes = 0
charlesName = "Charles Casper Stockham"
dianaName = "Diana DeGette"
raymonName = "Raymon Anthony Doane"
charles = 0
diana = 0
raymon = 0

def share(vote):
    return round((vote/totalVotes)*100, 3)

with open(filepath) as electionfile :
    csvreader = csv.reader(electionfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        totalVotes += 1

        if row[2] == charlesName :
            charles += 1
        elif row[2] == dianaName :
            diana += 1
        elif row[2] == raymonName :
            raymon += 1

    charlesShare = share(charles)
    dianaShare = share(diana)
    raymonShare = share(raymon)

    if (charles > diana) & (charles > raymon):
        winner = charlesName
    elif (diana > charles) & (diana > raymon):
        winner = dianaName
    else:
        winner = raymonName

    result = (f"""
          \nElection Results 
          \n-----------------------------
          \nTotal Votes: {totalVotes} 
          \n----------------------------- 
          \nCharles Casper Stockham: {charlesShare}% ({charles}) 
          \nDiana DeGette: {dianaShare}% ({diana})
          \nRaymon Anthony Doane: {raymonShare}% ({raymon})
          \n-----------------------------
          \nWinner: {winner}
          \n-----------------------------
          """)
    print(result)

output_path = os.path.join('analysis','results.txt')
with open(output_path, 'w') as textfile :
   textfile.write(result)
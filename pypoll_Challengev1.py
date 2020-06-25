# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# County options and county votes.
county_options = []
county_votes = {}

# Track county turnout, calculate the largest
largest_county = ""
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#track the county turnout largest  / voter
county_turnout = ""
clargest_vote = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Get the county from each row
        county_name = row[1]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            #add the candidate name to the candidate list
            county_options.append(county_name)

            # add the county to the county vote tally
            county_votes[county_name] = 0

        #add vote to the county's count
        county_votes[county_name] +=1

        # If the candidate does not match any existing candidate, add the
        # the candidate list.

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for county in county_votes:
        #retrieve vote count and percentage.
        county_vote = county_votes[county]
        county_percent = float(county_vote) / float(total_votes) * 100
        
        #print each county's vote count and percentage to the terminal
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end="")

        # Determine winning county vote
        if (county_vote > clargest_vote):
            clargest_vote = county_vote
            county_turnout = county

        # Save the county results to our text file.
        txt_file.write(county_results)

        # #determine vote count, largest turnout
        # if (cvotes > winning_count) and (cvote_percentage . winning_percentage):
        #     cvotes = county_votes[county]

    # Print the winning county results to the termnal
    county_turnout = (
        f"------------------------\n"
        f"Largest county Turnout: {county_turnout}\n"
        f"------------------------\n")
        
    print(county_turnout)

    #save to text file
    txt_file.write(county_turnout)

    for candidate in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)






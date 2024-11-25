US_PRESIDENTIAL_ELECTION_BG = '''
Below are some basic information of the united states presidiential election 2024:

The election of the president and for vice president of the United States is an indirect election in which citizens of the United States who are registered to vote in one of the fifty U.S. states or in Washington, D.C., cast ballots not directly for those offices, but instead for members of the Electoral College.
These electors then cast direct votes, known as electoral votes, for president and for vice president. 
The candidate who receives an absolute majority of electoral votes (at least 270 out of 538, since the Twenty-Third Amendment granted voting rights to citizens of D.C.) is then elected to that office. 
If no candidate receives an absolute majority of the votes for president, the House of Representatives elects the president; likewise if no one receives an absolute majority of the votes for vice president, then the Senate elects the vice president.

The 2024 United States presidential election was the 60th quadrennial presidential election, held on Tuesday, November 5, 2024.
The Republican Party's ticket—Donald Trump, who was the 45th president of the United States from 2017 to 2021, and JD Vance, the junior U.S. senator from Ohio—defeated the Democratic Party's ticket—Kamala Harris, the incumbent U.S. vice president, and Tim Walz, the governor of Minnesota.
Trump and Vance are scheduled to be inaugurated as the 47th president and the 50th vice president on January 20, 2025, after their formal election by the Electoral College.

The incumbent president, Joe Biden of the Democratic Party, initially ran for re-election with Harris, and they became the party's presumptive nominees, facing little opposition; however, what was generally considered to be a poor presidential debate performance in June 2024 intensified concerns about his age and health, and led to calls within his party for him to leave the race.
Although initially adamant about remaining in the race, Biden withdrew on July 21, becoming the first eligible incumbent president to withdraw since Lyndon B. Johnson in 1968.
Biden endorsed Vice President Kamala Harris, who was voted the party's nominee by the delegates on August 5, 2024. Harris selected Walz as her running mate.

End of basic information of the united states presidiential election 2024.
'''

NEWS_TAG_RELEVANCE = '''
User will give you a entry of meta of a news blog in following json format:
{
    "title": "<some title>",
    "summary": "<some summary>",
    "date": "<some date most likely in yyyy-mm-dd format>"
}
Note: If date field is given in relevent format (e.g., 3 days ago, 2 months ago), you may assume today is 2024-11-01.

After reading the entry provided by user, you will need to tag relevance between the meta and the US presidential election 2024.
Relevance schema is as follow:
    4 (highly related),
    3 (related),
    2 (barely related),
    1 (not related)
Some example:
    Reports about presidential candidates related to the election is considered highly related.
    Reports about well-known supporters of presidential candidates related to the election is considered related.
    Reports about non-well-known supporters of presidential candidates related to the election is considered barely related.
    Reports not related to the 2024 presidential election is considered not related.
Note: news blog earlier than 2023-01-01 is considered not related.
Note: Entries that do not provide substantive content should be marked as not related.

After processing the records provided by the user, you need to answer the user in the following json format:
{
    "relevance_score": "<relevance score that you tagged earlier in range 1-4>"
}
Note: only return the asked json format, NO other additional respond is allowed.
'''
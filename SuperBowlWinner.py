superbowl_winners = {
        1967: "Green Bay Packers",
        1968: "Green Bay Packers",
        1969: "New York Jets",
        1970: "Kansas City Chiefs",
        1971: "Baltimore Colts",
        1972: "Dallas Cowboys",
        1973: "Miami Dolphins",
        1974: "Miami Dolphins",
        1975: "Pittsburgh Steelers",
        1976: "Pittsburgh Steelers",
        1977: "Oakland Raiders",
        1978: "Dallas Cowboys",
        1979: "Pittsburgh Steelers",
        1980: "Pittsburgh Steelers",
        1981: "Oakland Raiders",
        1982: "San Francisco 49ers",
        1983: "Washington Redskins",
        1984: "Los Angeles Raiders",
        1985: "San Francisco 49ers",
        1986: "Chicago Bears",
        1987: "New York Giants",
        1988: "Washington Redskins",
        1989: "San Francisco 49ers",
        1990: "San Francisco 49ers",
        1991: "New York Giants",
        1992: "Washington Redskins",
        1993: "Dallas Cowboys",
        1994: "Dallas Cowboys",
        1995: "San Francisco 49ers",
        1996: "Dallas Cowboys",
        1997: "Green Bay Packers",
        1998: "Denver Broncos",
        1999: "Denver Broncos",
        2000: "St. Louis Rams",
        2001: "Baltimore Ravens",
        2002: "New England Patriots",
        2003: "Tampa Bay Buccaneers",
        2004: "New England Patriots",
        2005: "New England Patriots",
        2006: "Pittsburgh Steelers",
        2007: "Indianapolis Colts",
        2008: "New York Giants",
        2009: "Pittsburgh Steelers",
        2010: "New Orleans Saints",
        2011: "Green Bay Packers",
        2012: "New York Giants",
        2013: "Baltimore Ravens",
        2014: "Seattle Seahawks",
        2015: "New England Patriots",
        2016: "Denver Broncos",
        2017: "New England Patriots",
        2018: "Philadelphia Eagles",
        2019: "New England Patriots",
        2020: "Kansas City Chiefs",
        2021: "Tampa Bay Buccaneers",
        2022: "Los Angeles Rams",
        2023: "Kansas City Chiefs",
        2024: "Kansas City Chiefs",
        2025: "Philadelphia Eagles",
        2026: "Seattle Seahawks"
        }

def superbowlWinner(year):
    'Enter a year and find out who won the Super Bowl that year'

    if year in superbowl_winners:
        print(f"\nThe {superbowl_winners[year]} won the Super Bowl in {year}\n")

    else:
        print("\nError: No information for that year\n")    

def superbowlMVP(year):
    'Enter a year and find out who won the Super Bowl MVP that year'
    superbowl_mvp = {
        1967: ("Bart Starr", "QB"),
        1968: ("Bart Starr", "QB"),
        1969: ("Joe Namath", "QB"),
        1970: ("Len Dawson", "QB"),
        1971: ("Chuck Howley", "LB"),
        1972: ("Roger Staubach", "QB"),
        1973: ("Jake Scott", "S"),
        1974: ("Larry Csonka", "RB"),
        1975: ("Franco Harris", "RB"),
        1976: ("Lynn Swann", "WR"),
        1977: ("Fred Biletnikoff", "WR"),
        1978: ("Harvey Martin & Randy White", "DE/DT"),
        1979: ("Terry Bradshaw", "QB"),
        1980: ("Terry Bradshaw", "QB"),
        1981: ("Jim Plunkett", "QB"),
        1982: ("Joe Montana", "QB"),
        1983: ("John Riggins", "RB"),
        1984: ("Marcus Allen", "RB"),
        1985: ("Joe Montana", "QB"),
        1986: ("Richard Dent", "DE"),
        1987: ("Phil Simms", "QB"),
        1988: ("Doug Williams", "QB"),
        1989: ("Jerry Rice", "WR"),
        1990: ("Joe Montana", "QB"),
        1991: ("Ottis Anderson", "RB"),
        1992: ("Mark Rypien", "QB"),
        1993: ("Emmitt Smith", "RB"),
        1994: ("Steve Young", "QB"),
        1995: ("Larry Brown", "CB"),
        1996: ("Brett Favre", "QB"),
        1997: ("Terrell Davis", "RB"),
        1998: ("John Elway", "QB"),
        1999: ("Kurt Warner", "QB"),
        2000: ("Kurt Warner", "QB"),
        2001: ("Ray Lewis", "LB"),
        2002: ("Tom Brady", "QB"),
        2003: ("Dexter Jackson", "CB"),
        2004: ("Tom Brady", "QB"),
        2005: ("Deion Branch", "WR"),
        2006: ("Hines Ward", "WR"),
        2007: ("Peyton Manning", "QB"),
        2008: ("Eli Manning", "QB"),
        2009: ("Santonio Holmes", "WR"),
        2010: ("Drew Brees", "QB"),
        2011: ("Aaron Rodgers", "QB"),
        2012: ("Eli Manning", "QB"),
        2013: ("Joe Flacco", "QB"),
        2014: ("Malcolm Smith", "LB"),
        2015: ("Tom Brady", "QB"),
        2016: ("Von Miller", "LB"),
        2017: ("Tom Brady", "QB"),
        2018: ("Nick Foles", "QB"),
        2019: ("Julian Edelman", "WR"),
        2020: ("Patrick Mahomes", "QB"),
        2021: ("Tom Brady", "QB"),
        2022: ("Cooper Kupp", "WR"),
        2023: ("Patrick Mahomes", "QB"),
        2024: ("Patrick Mahomes", "QB"),
        2025: ("Jalen Hurts", "QB"),
        2026: ("Undecided", "?")
        }
    
    if year in superbowl_mvp:
        player, position = superbowl_mvp[year]
        print(f"\nThe Superbowl MVP in {year} was {player} ({position})\n")

    else:
        print("\nError: No information for that year\n") 

def teamWins():
    'Enter a team name and find out how many Super Bowls they have won and which years'
    teamname = input("Enter an NFL team name: ")
    wins = []

    for year in superbowl_winners:
        if superbowl_winners[year].lower() == teamname.lower():
            wins.append(year)

    if len(wins) > 0:
        print(f"The {teamname.capitalize()} have {len(wins)} Super Bowl wins.")
        print("They won in: ")
        for year in wins:
            print(year, end="\n")
    else:
        print("\nThat team has no Super Bowl wins.\n")
        
while True:
    print("Superbowl Information by Year")
    print("1. Find Superbowl winner")
    print("2. Find Superbowl MVP")
    print("3. Search wins by team")
    print("4. QUIT")

    choice = input("Please enter either '1', '2', '3', or '4': ")

    if choice == "1":
        yearInput = input("Enter a year to find Superbowl winner: ")
        try:
            year = int(yearInput)
            superbowlWinner(year)

        except:
            print("\nPlease try again!\n")

    elif choice == "2":
        yearInput = input("Enter a year to find Superbowl MVP: ")
        try:
            year = int(yearInput)
            superbowlMVP(year)

        except:
            print("\nPlease try again!\n")

    elif choice == "3":
        teamWins()
        


    elif choice == "4":
        print("\nGoodbye!\n")
        break
            

    else:
        print("\nInvalid input, please enter either '1', '2', or '3'\n")




    

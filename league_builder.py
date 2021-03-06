import csv


# this function gets the players' information from the cvs file and stores into the list called 'players'.
def storing_players():
    with open('soccer_players.csv') as csvfile:
        player_reader = csv.reader(csvfile, delimiter=',')
        rows = list(player_reader)

        field_names = ['name', 'height', 'experienced', 'guardian name(s)']
        players = []

        for row in rows[1:]:
            dict = {}
            i = 0
            string = ','.join(row)
            for attribute in string.split(','):
                # storing each of the attributes into dictionary with the specified fieldnames.
                dict[field_names[i]] = attribute
                i += 1
            players.append(dict)
    return players


# this function gets the sorted teams and writes them into the text file called 'teams.txt'
def writing_teams():
    dragons, sharks, raptors = creating_teams()
    with open('teams.txt', 'a') as teamsfile:
        teamsfile.write('Dragons'+"\n")
        for player in dragons:
            teamsfile.write(info_line(player)+"\n")
        teamsfile.write('\n')

        teamsfile.write('Sharks'+"\n")
        for player in sharks:
            teamsfile.write(info_line(player)+"\n")
        teamsfile.write('\n')

        teamsfile.write('Raptors'+"\n")
        for player in raptors:
            teamsfile.write(info_line(player)+"\n")


# creating letter format for parents
def letter_to_parent(player, filename):
    # players = storing_players()
    with open(filename,'a') as file:
        file.write('Dear {},'.format(player['guardian name(s)'])+'\n')
        file.write('{} is in team called {}.'.format(player['name'], team_of(player)))
        file.write(' First practice will be on September 10 at 9 am.'+'\n')
        file.write('Hope to see you soon!'+'\n')
        file.write('Thank you,'+'\n')
        file.write('Coordinator Sena')


# shows the team of the player
def team_of(player):
    dragons, sharks, raptors = creating_teams()
    if player in dragons:
        return 'dragons'
    elif player in sharks:
        return 'sharks'
    elif player in raptors:
        return 'raptors'


# this function divides the team into two based on experience
def dividing_teams():
    exprncd_players = []
    not_exprncd_players = []
    players = storing_players()
    for player in players:
        if player['experienced'] == 'YES':
            exprncd_players.append(player)
        else:
            not_exprncd_players.append(player)
    return exprncd_players, not_exprncd_players


# this function distributes the experienced and not experienced players evenly into 3 teams.
def creating_teams():
    exprncd_players, not_exprncd_players = dividing_teams()

    # every team gets one of the each 3 experienced/not-experienced players

    dragons = exprncd_players[::3]
    dragons.extend(not_exprncd_players[::3])

    sharks = exprncd_players[1::3]
    sharks.extend(not_exprncd_players[1::3])

    raptors = exprncd_players[2::3]
    raptors.extend(not_exprncd_players[2::3])
    return dragons, sharks, raptors


# this function helps formatting the players' certain information into one line
def info_line(player):
    line = "{}, {}, {}".format(player['name'], player['experienced'], player['guardian name(s)'])
    return line


if __name__ == '__main__':
    dividing_teams()
    creating_teams()
    writing_teams()

    # creating letters for each parent
    players = storing_players()
    for player in players:
        player_name = player['name'].split(' ')
        formatted_player_name = '_'.join(player_name).lower()
        letter_to_parent(player, formatted_player_name + ".txt")

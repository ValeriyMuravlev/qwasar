import re
import csv

# this extract of code was taken from video tutorial by juvin_g as I found it helped to solve team separation issue
def is_away_team(away_team, current_team):
    return away_team == current_team

# Create a function analyse_nba_game(play_by_play_moves) which receives an array of play (nba1.txt)
# and will return a dictionary summary of the game players_dict
def analyse_nba_game(play_by_play_moves):

    nba_text = open(play_by_play_moves)
    result = nba_text.read().rstrip()
    game_lines = result.split("\n")

    for item in range(len(game_lines)):
        game_lines[item] = game_lines[item].split("|")

    # print(game_lines[0][len(game_lines[0]) - 1])
    #print(result)

    player_names = re.findall(r'[\Wa-zA-Z]\.\ [^\s^\)]+', result)


    #deleting equal person names in player_name and adding them to list player_list
    players_list = []
    for person in range(len(player_names)):
        if player_names[person] not in players_list:
            players_list.append(player_names[person])

    # print(players_list) now we have only uniques players` names in players_list
    # It is hard to add player RE with special symbols, that`s why we add Р“Рѓ. Abrines in players_list
    players_list.append("Р“Рѓ. Abrines")

    # print(players_list)

    players_data = []
    for player in range(len(players_list)):
        player_dict = {
            "player_name": players_list[player], "FG": 0, "FGA": 0,
            "FG%": None, "3P": 0, "3PA": 0, "3P%": None, "FT": 0,
            "FTA": 0, "FT%": None, "ORB": 0, "DRB": 0, "TRB": 0,
            "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0
        }

        players_data.append(player_dict)

    # print(players_data)

    # starting count points for actions and adding them to players_data list
    for player in range(0, len(players_data)):

        for str in range(0, len(game_lines)):

            if players_data[player]["player_name"] not in game_lines[str][len(game_lines[str]) - 1]:
                continue

            # 3P = 3-Point Field Goals, 3PA - 3-Point Field Goal Attempts
            # FG - Field Goals (includes both 2-point field goals and 3-point field goals)
            # FGA - Field Goal Attempts (includes both 2-point field goal attempts and 3-point field goal attempts)

            if players_data[player]["player_name"] + " makes 3-pt jump shot from" in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["3P"] = players_data[player]["3P"] + 1
                players_data[player]["3PA"] = players_data[player]["3PA"] + 1
                players_data[player]["FG"] = players_data[player]["FG"] + 1
                players_data[player]["FGA"] = players_data[player]["FGA"] + 1

            if players_data[player]["player_name"] + " misses 3-pt jump shot from" in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["3PA"] = players_data[player]["3PA"] + 1
                players_data[player]["FGA"] = players_data[player]["FGA"] + 1

            if players_data[player]["player_name"] + " makes 2-pt" in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["FG"] = players_data[player]["FG"] + 1
                players_data[player]["FGA"] = players_data[player]["FGA"] + 1

            if players_data[player]["player_name"] + " misses 2-pt" in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["FGA"] = players_data[player]["FGA"] + 1

            # 3P% - 3-Point Field Goal Percentage (available since the 1979-80 season in the NBA); the formula is 3P / 3PA.
            try:
                players_data[player]["3P%"] = round(players_data[player]["3P"] / players_data[player]["3PA"], 3)
            except ZeroDivisionError:
                players_data[player]["3P%"] = 0.000

            # FG% - Field Goal Percentage; the formula is FG / FGA
            try:
                players_data[player]["FG%"] = round(players_data[player]["FG"] / players_data[player]["FGA"], 3)
            except ZeroDivisionError:
                players_data[player]["FG%"] = 0.000

            # FT - Free Throws
            # FTA - Free Throw Attempts
            if players_data[player]["player_name"] + " makes free throw" in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["FT"] = players_data[player]["FT"] + 1
                players_data[player]["FTA"] = players_data[player]["FTA"] + 1

            if players_data[player]["player_name"] + " misses free throw" in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["FTA"] = players_data[player]["FTA"] + 1
            if players_data[player]["player_name"] + " makes clear path free throw" in game_lines[str][
                len(game_lines[str]) - 1]:
                players_data[player]["FTA"] = players_data[player]["FTA"] + 1
                players_data[player]["FT"] = players_data[player]["FT"] + 1

            # FT% - Free Throw Percentage; the formula is FT / FTA.
            try:
                players_data[player]["FT%"] = round(
                    players_data[player]["FT"] / players_data[player]["FTA"], 3)
            except ZeroDivisionError:
                players_data[player]["FT%"] = 0.000

            # ORB - Offensive Rebounds
            # TRB - Total Rebounds
            if "Offensive rebound by " + players_data[player]["player_name"] in game_lines[str][
                len(game_lines[str]) - 1]:
                players_data[player]["ORB"] = players_data[player]["ORB"] + 1
                players_data[player]["TRB"] = players_data[player]["TRB"] + 1

            if "Defensive rebound by " + players_data[player]["player_name"] in game_lines[str][
                len(game_lines[str]) - 1]:
                players_data[player]["DRB"] = players_data[player]["DRB"] + 1
                players_data[player]["TRB"] = players_data[player]["TRB"] + 1

            # AST - Assists
            if "assist by " + players_data[player]["player_name"] in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["AST"] = players_data[player]["AST"] + 1

            # STL - Steals
            if "steal by " + players_data[player]["player_name"] in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["STL"] = players_data[player]["STL"] + 1

            # BLK - Blocks
            if "block by " + players_data[player]["player_name"] in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["BLK"] = players_data[player]["BLK"] + 1

            # TOV - Turnovers
            if "Turnover by " + players_data[player]["player_name"] in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["TOV"] = players_data[player]["TOV"] + 1

            #PF - Personal Fouls
            if "foul by " + players_data[player]["player_name"] in game_lines[str][len(game_lines[str]) - 1]:
                players_data[player]["PF"] = players_data[player]["PF"] + 1

        players_data[player]["PTS"] = players_data[player]["3P"] * 3 + (players_data[player]["FG"] - players_data[player]["3P"]) * 2 + players_data[player]["FT"] * 1

    # identifying the teams and its players
    away_team = game_lines[0][3]
    home_team = game_lines[0][4]

    res_dict = {"home_team": {"name": away_team, "players_data": []},
                "away_team": {"name": home_team, "players_data": []}}

    for plr in range(len(players_list)):
        for row in range(len(game_lines)):
            relevant_team = game_lines[row][2]

            if (players_list[plr] not in game_lines[row][len(game_lines[row]) - 1]) or (
                    players_list[plr] + ")" in game_lines[row][len(game_lines[row]) - 1]) or (
                    "for " + players_list[plr] in game_lines[row][len(game_lines[row]) - 1]) or (
                    "foul by " + players_list[plr] in game_lines[row][len(game_lines[row]) - 1]):
                continue

            if is_away_team(away_team, relevant_team):
                res_dict["away_team"]["name"] = away_team
                res_dict["away_team"]["players_data"].append(players_data[plr])
                break
            else:
                res_dict["home_team"]["name"] = home_team
                res_dict["home_team"]["players_data"].append(players_data[plr])
                break

    return res_dict


# returns a dictionary with name and players_data will print it
# with the following format (each column is separated by a tabulation (' ')):
def print_nba_game_stats(team_dict):
    # Team Totals
    team_total = {"home_team": ["Team Totals"], "away_team": ["Team Totals"]}
    total_fg = {"home_team": 0, "away_team": 0}
    total_fga = {"home_team": 0, "away_team": 0}
    total_fg_perc = {"home_team": 0, "away_team": 0}
    total_three_p = {"home_team": 0, "away_team": 0}
    total_three_pa = {"home_team": 0, "away_team": 0}
    total_three_p_perc = {"home_team": 0, "away_team": 0}
    total_ft = {"home_team": 0, "away_team": 0}
    total_fta = {"home_team": 0, "away_team": 0}
    total_ft_perc = {"home_team": 0, "away_team": 0}
    total_orb = {"home_team": 0, "away_team": 0}
    total_drb = {"home_team": 0, "away_team": 0}
    total_trb = {"home_team": 0, "away_team": 0}
    total_ast = {"home_team": 0, "away_team": 0}
    total_stl = {"home_team": 0, "away_team": 0}
    total_blk = {"home_team": 0, "away_team": 0}
    total_tov = {"home_team": 0, "away_team": 0}
    total_pf = {"home_team": 0, "away_team": 0}
    total_pts = {"home_team": 0, "away_team": 0}

    count = 0
    for key in team_dict.keys():

        for item in range(0, len(team_dict[key]['players_data'])):
            total_fg[key] += team_dict[key]['players_data'][item]['FG']
            total_fga[key] += team_dict[key]['players_data'][item]['FGA']

            if team_dict[key]['players_data'][item]['FG%'] is not None:
                total_fg_perc[key] += team_dict[key]['players_data'][item]['FG%']

            total_three_p[key] += team_dict[key]['players_data'][item]['3P']
            total_three_pa[key] += team_dict[key]['players_data'][item]['3PA']

            if team_dict[key]['players_data'][item]['3P%'] is not None:
                total_three_p_perc[key] += team_dict[key]['players_data'][item]['3P%']

            total_ft[key] += team_dict[key]['players_data'][item]['FT']
            total_fta[key] += team_dict[key]['players_data'][item]['FTA']

            if team_dict[key]['players_data'][item]['FT%'] is not None:
                total_ft_perc[key] += team_dict[key]['players_data'][item]['FT%']

            total_orb[key] += team_dict[key]['players_data'][item]['ORB']
            total_drb[key] += team_dict[key]['players_data'][item]['DRB']
            total_trb[key] += team_dict[key]['players_data'][item]['TRB']
            total_ast[key] += team_dict[key]['players_data'][item]['AST']
            total_stl[key] += team_dict[key]['players_data'][item]['STL']
            total_blk[key] += team_dict[key]['players_data'][item]['BLK']
            total_tov[key] += team_dict[key]['players_data'][item]['TOV']
            total_pf[key] += team_dict[key]['players_data'][item]['PF']
            total_pts[key] += team_dict[key]['players_data'][item]['PTS']

            count += 1

        team_total[key].append(total_fg[key])
        team_total[key].append(total_fga[key])
        team_total[key].append(round(total_fg_perc[key] / count, 3))
        team_total[key].append(total_three_p[key])
        team_total[key].append(total_three_pa[key])
        team_total[key].append(round(total_three_p_perc[key] / count, 3))
        team_total[key].append(total_ft[key])
        team_total[key].append(total_fta[key])
        team_total[key].append(round(total_ft_perc[key] / count, 3))
        team_total[key].append(total_orb[key])
        team_total[key].append(total_drb[key])
        team_total[key].append(total_trb[key])
        team_total[key].append(total_ast[key])
        team_total[key].append(total_stl[key])
        team_total[key].append(total_blk[key])
        team_total[key].append(total_tov[key])
        team_total[key].append(total_pf[key])
        team_total[key].append(total_pts[key])

    # printing the final table with key points
    formatted_table = ""
    for team in team_dict.keys():

        formatted_table += team_dict[team]['name'] + "\n"
        formatted_table += "\t".join(team_dict[team]['players_data'][0].keys()) + "\n"

        for name in range(0, len(team_dict[team]['players_data'])):
            a = list(team_dict[team]['players_data'][name].values())
            b = list(map(str, a))
            formatted_table += "\t".join(b)
            formatted_table += "\n"

        formatted_table += "\t".join(map(str, team_total[team])) + "\n"

    return formatted_table


play_by_play_moves = "Warriors_vs_Thunders.txt"
team_dict = analyse_nba_game(play_by_play_moves)

print(print_nba_game_stats(team_dict))



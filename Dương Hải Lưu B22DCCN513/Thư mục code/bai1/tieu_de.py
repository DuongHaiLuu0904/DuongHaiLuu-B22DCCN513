
# Tạo tiêu đề CSV từ tất cả các thuộc tính của Player
header = [
    "name","nation", "team", "position", "age",
    # Playing Time
    "matches_played", "starts", "minutes",
    # Performance
    "non_penalty_goals", "penalty_goals", "assists", "yellow_cards", "red_cards",
    # Expected
    "xG", "npxG", "xAG",
    # Progression
    "PrgC", "PrgP", "PrgR",
    # Per 90 minutes
    "per90_Gls", "per90_Ast", "per90_G+A", "per90_G-PK", "per90_G+A-PK",
    "per90_xG", "per90_xAG", "per90_xG+xAG", "per90_npxG", "per90_npxG+xAG",
    # Goalkeeping
    "GA", "GA90", "SoTA", "Saves", "Save%", "W", "D", "L", "CS", "CS%",
    # Goalkeeping Penalty Kicks
    "PKatt", "PKA", "PKsv", "PKm", "GK_Save%",
    # Shooting Standard
    "Gls", "Sh", "SoT", "SoT%", "Sh/90", "SoT/90", "G/Sh", "G/SoT", "Dist", "FK", "PK", "PKatt",
    # Shooting Expected
    "xG_shooting", "npxG_shooting", "npxG/Sh", "G-xG", "np:G-xG",
    # Passing Total
    "Pass_Cmp", "Pass_Att", "Pass_Cmp%", "TotDist", "PrgDist",
    # Passing Short
    "Short_Cmp", "Short_Att", "Short_Cmp%",
    # Passing Medium
    "Medium_Cmp", "Medium_Att", "Medium_Cmp%",
    # Passing Long
    "Long_Cmp", "Long_Att", "Long_Cmp%",
    # Expected Passing
    'Ast',"xAG", "xA", "A-xAG", "KP", "1/3", "PPA", "CrsPA", "PrgP",
    # Pass Types
    "Pass_Live", "Pass_Dead", "Pass_FK", "Pass_TB", "Pass_Sw", "Pass_Crs", "Pass_TI", "Pass_CK",
    # Pass Outcomes
    "Pass_Cmp_outcome", "Pass_Off", "Pass_Blocks",
    # Defensive Actions
    "Tkl", "TklW", "Def_3rd", "Mid_3rd", "Att_3rd",
    "Challenges_Tkl", "Challenges_Att", "Challenges_Tkl%", "Challenges_Lost",
    # Possession
    "Touches", "Def_Pen", "Def_3rd", "Mid_3rd", "Att_3rd", "Att_Pen", "Live_Touches",
    # Take-ons
    "Take_Att", "Take_Succ", "Take_Succ%", "Take_Tkld", "Take_Tkld%",
    # Carries
    "Carries", "Carries_TotDist", "Carries_ProDist", "Carries_ProgC", "Carries_1/3", "Carries_CPA", "Carries_Mis", "Carries_Dis",
    # Miscellaneous Stats
    "Fls", "Fld", "Off", "Crs", "OG", "Recov", "Aerial_Won", "Aerial_Lost", "Aerial_Won%"
]
header2 = [
    "name","numberOfPlayer", "Poss", "age",
    # Playing Time
    "matches_played", "starts", "minutes",
    # Performance
    "non_penalty_goals", "penalty_goals", "assists", "yellow_cards", "red_cards",
    # Expected
    "xG", "npxG", "xAG",
    # Progression
    "PrgC", "PrgP", "PrgR",
    # Per 90 minutes
    "per90_Gls", "per90_Ast", "per90_G+A", "per90_G-PK", "per90_G+A-PK",
    "per90_xG", "per90_xAG", "per90_xG+xAG", "per90_npxG", "per90_npxG+xAG",
    # Goalkeeping
    "GA", "GA90", "SoTA", "Saves", "Save%", "W", "D", "L", "CS", "CS%",
    # Goalkeeping Penalty Kicks
    "PKatt", "PKA", "PKsv", "PKm", "GK_Save%",
    # Shooting Standard
    "Gls", "Sh", "SoT", "SoT%", "Sh/90", "SoT/90", "G/Sh", "G/SoT", "Dist", "FK", "PK", "PKatt",
    # Shooting Expected
    "xG_shooting", "npxG_shooting", "npxG/Sh", "G-xG", "np:G-xG",
    # Passing Total
    "Pass_Cmp", "Pass_Att", "Pass_Cmp%", "TotDist", "PrgDist",
    # Passing Short
    "Short_Cmp", "Short_Att", "Short_Cmp%",
    # Passing Medium
    "Medium_Cmp", "Medium_Att", "Medium_Cmp%",
    # Passing Long
    "Long_Cmp", "Long_Att", "Long_Cmp%",
    # Expected Passing
    'Ast', "xAG", "xA", "A-xAG", "KP", "1/3", "PPA", "CrsPA", "PrgP",
    # Pass Types
    "Pass_Live", "Pass_Dead", "Pass_FK", "Pass_TB", "Pass_Sw", "Pass_Crs", "Pass_TI", "Pass_CK",
    # Pass Outcomes
    "Pass_Cmp_outcome", "Pass_Off", "Pass_Blocks",
    # Defensive Actions
    "Tkl", "TklW", "Def_3rd", "Mid_3rd", "Att_3rd",
    "Challenges_Tkl", "Challenges_Att", "Challenges_Tkl%", "Challenges_Lost",
    # Possession
    "Touches", "Def_Pen", "Def_3rd", "Mid_3rd", "Att_3rd", "Att_Pen", "Live_Touches",
    # Take-ons
    "Take_Att", "Take_Succ", "Take_Succ%", "Take_Tkld", "Take_Tkld%",
    # Carries
    "Carries", "Carries_TotDist", "Carries_ProDist", "Carries_ProgC", "Carries_1/3", "Carries_CPA", "Carries_Mis", "Carries_Dis",
    # Miscellaneous Stats
    "Fls", "Fld", "Off", "Crs", "OG", "Recov", "Aerial_Won", "Aerial_Lost", "Aerial_Won%"
]

def row(player):
    return [
    player.name,player.nation, player.team, player.position, player.age,
    # Playing Time
    player.playing_time["matches_played"], player.playing_time["starts"], player.playing_time["minutes"],
    # Performance
    player.performance["non_penalty_goals"], player.performance["penalty_goals"], player.performance["assists"],
    player.performance["yellow_cards"], player.performance["red_cards"],
    # Expected
    player.expected["xG"], player.expected["npxG"], player.expected["xAG"],
    # Progression
    player.progression["PrgC"], player.progression["PrgP"], player.progression["PrgR"],
    # Per 90 minutes
    player.per_90["Gls"], player.per_90["Ast"], player.per_90["G+A"], player.per_90["G-PK"],
    player.per_90["G+A-PK"], player.per_90["xG"], player.per_90["xAG"], player.per_90["xG+xAG"],
    player.per_90["npxG"], player.per_90["npxG+xAG"],
    # Goalkeeping Performance
    player.goalkeeping["Performance"]["GA"], player.goalkeeping["Performance"]["GA90"],
    player.goalkeeping["Performance"]["SoTA"], player.goalkeeping["Performance"]["Saves"],
    player.goalkeeping["Performance"]["Save%"], player.goalkeeping["Performance"]["W"],
    player.goalkeeping["Performance"]["D"], player.goalkeeping["Performance"]["L"],
    player.goalkeeping["Performance"]["CS"], player.goalkeeping["Performance"]["CS%"],
    # Goalkeeping Penalty Kicks
    player.goalkeeping["Penalty Kicks"]["PKatt"], player.goalkeeping["Penalty Kicks"]["PKA"],
    player.goalkeeping["Penalty Kicks"]["PKsv"], player.goalkeeping["Penalty Kicks"]["PKm"],
    player.goalkeeping["Penalty Kicks"]["Save%"],
    # Shooting Standard
    player.shooting["Standard"]["Gls"], player.shooting["Standard"]["Sh"],
    player.shooting["Standard"]["SoT"], player.shooting["Standard"]["SoT%"],
    player.shooting["Standard"]["Sh/90"], player.shooting["Standard"]["SoT/90"],
    player.shooting["Standard"]["G/Sh"], player.shooting["Standard"]["G/SoT"],
    player.shooting["Standard"]["Dist"], player.shooting["Standard"]["FK"],
    player.shooting["Standard"]["PK"], player.shooting["Standard"]["PKatt"],
    # Shooting Expected
    player.shooting["Expected"]["xG"], player.shooting["Expected"]["npxG"],
    player.shooting["Expected"]["npxG/Sh"], player.shooting["Expected"]["G-xG"],
    player.shooting["Expected"]["np:G-xG"],
    # Passing Total
    player.passing["Total"]["Cmp"], player.passing["Total"]["Att"],
    player.passing["Total"]["Cmp%"], player.passing["Total"]["TotDist"],
    player.passing["Total"]["PrgDist"],
    # Passing Short
    player.passing["Short"]["Cmp"], player.passing["Short"]["Att"],
    player.passing["Short"]["Cmp%"],
    # Passing Medium
    player.passing["Medium"]["Cmp"], player.passing["Medium"]["Att"],
    player.passing["Medium"]["Cmp%"],
    # Passing Long
    player.passing["Long"]["Cmp"], player.passing["Long"]["Att"],
    player.passing["Long"]["Cmp%"],
    # Expected Passing
    player.passing["Expected"]["Ast"], player.passing["Expected"]["xAG"],
    player.passing["Expected"]["xA"], player.passing["Expected"]["A-xAG"],
    player.passing["Expected"]["KP"], player.passing["Expected"]["1/3"],
    player.passing["Expected"]["PPA"], player.passing["Expected"]["CrsPA"],
    player.passing["Expected"]["PrgP"],
    # Pass Types
    player.pass_types["Pass Types"]["Live"], player.pass_types["Pass Types"]["Dead"],
    player.pass_types["Pass Types"]["FK"], player.pass_types["Pass Types"]["TB"],
    player.pass_types["Pass Types"]["Sw"], player.pass_types["Pass Types"]["Crs"],
    player.pass_types["Pass Types"]["TI"], player.pass_types["Pass Types"]["CK"],
    # Pass Outcomes
    player.pass_types["Outcomes"]["Cmp"], player.pass_types["Outcomes"]["Off"],
    player.pass_types["Outcomes"]["Blocks"],
    # Defensive Actions
    player.defensive_actions["Tackles"]["Tkl"], player.defensive_actions["Tackles"]["TklW"],
    player.defensive_actions["Tackles"]["Def 3rd"], player.defensive_actions["Tackles"]["Mid 3rd"],
    player.defensive_actions["Tackles"]["Att 3rd"],
    player.defensive_actions["Challenges"]["Tkl"], player.defensive_actions["Challenges"]["Att"],
    player.defensive_actions["Challenges"]["Tkl%"], player.defensive_actions["Challenges"]["Lost"],
    # Possession
    player.possession["Touches"]["Touches"], player.possession["Touches"]["Def Pen"],
    player.possession["Touches"]["Def 3rd"], player.possession["Touches"]["Mid 3rd"],
    player.possession["Touches"]["Att 3rd"], player.possession["Touches"]["Att Pen"],
    player.possession["Touches"]["Live"],
    player.possession["Take-Ons"]["Att"], player.possession["Take-Ons"]["Succ"],
    player.possession["Take-Ons"]["Succ%"], player.possession["Take-Ons"]["Tkld"],
    player.possession["Take-Ons"]["Tkld%"],
    player.possession["Carries"]["Carries"], player.possession["Carries"]["TotDist"],
    player.possession["Carries"]["ProDist"], player.possession["Carries"]["ProgC"],
    player.possession["Carries"]["1/3"], player.possession["Carries"]["CPA"],
    player.possession["Carries"]["Mis"], player.possession["Carries"]["Dis"],
    # Miscellaneous Stats
    player.misc_stats["Performance"]["Fls"], player.misc_stats["Performance"]["Fld"],
    player.misc_stats["Performance"]["Off"], player.misc_stats["Performance"]["Crs"],
    player.misc_stats["Performance"]["OG"], player.misc_stats["Performance"]["Recov"],
    player.misc_stats["Aerial Duels"]["Won"], player.misc_stats["Aerial Duels"]["Lost"],
    player.misc_stats["Aerial Duels"]["Won%"]
]

def row2(squad):
    return [
    squad.name,squad.numberOfPlayer, squad.poss, squad.age,
    # Playing Time
    squad.playing_time["matches_played"], squad.playing_time["starts"], squad.playing_time["minutes"],
    # Performance
    squad.performance["non_penalty_goals"], squad.performance["penalty_goals"], squad.performance["assists"],
    squad.performance["yellow_cards"], squad.performance["red_cards"],
    # Expected
    squad.expected["xG"], squad.expected["npxG"], squad.expected["xAG"],
    # Progression
    squad.progression["PrgC"], squad.progression["PrgP"], squad.progression["PrgR"],
    # Per 90 minutes
    squad.per_90["Gls"], squad.per_90["Ast"], squad.per_90["G+A"], squad.per_90["G-PK"],
    squad.per_90["G+A-PK"], squad.per_90["xG"], squad.per_90["xAG"], squad.per_90["xG+xAG"],
    squad.per_90["npxG"], squad.per_90["npxG+xAG"],
    # Goalkeeping Performance
    squad.goalkeeping["Performance"]["GA"], squad.goalkeeping["Performance"]["GA90"],
    squad.goalkeeping["Performance"]["SoTA"], squad.goalkeeping["Performance"]["Saves"],
    squad.goalkeeping["Performance"]["Save%"], squad.goalkeeping["Performance"]["W"],
    squad.goalkeeping["Performance"]["D"], squad.goalkeeping["Performance"]["L"],
    squad.goalkeeping["Performance"]["CS"], squad.goalkeeping["Performance"]["CS%"],
    # Goalkeeping Penalty Kicks
    squad.goalkeeping["Penalty Kicks"]["PKatt"], squad.goalkeeping["Penalty Kicks"]["PKA"],
    squad.goalkeeping["Penalty Kicks"]["PKsv"], squad.goalkeeping["Penalty Kicks"]["PKm"],
    squad.goalkeeping["Penalty Kicks"]["Save%"],
    # Shooting Standard
    squad.shooting["Standard"]["Gls"], squad.shooting["Standard"]["Sh"],
    squad.shooting["Standard"]["SoT"], squad.shooting["Standard"]["SoT%"],
    squad.shooting["Standard"]["Sh/90"], squad.shooting["Standard"]["SoT/90"],
    squad.shooting["Standard"]["G/Sh"], squad.shooting["Standard"]["G/SoT"],
    squad.shooting["Standard"]["Dist"], squad.shooting["Standard"]["FK"],
    squad.shooting["Standard"]["PK"], squad.shooting["Standard"]["PKatt"],
    # Shooting Expected
    squad.shooting["Expected"]["xG"], squad.shooting["Expected"]["npxG"],
    squad.shooting["Expected"]["npxG/Sh"], squad.shooting["Expected"]["G-xG"],
    squad.shooting["Expected"]["np:G-xG"],
    # Passing Total
    squad.passing["Total"]["Cmp"], squad.passing["Total"]["Att"],
    squad.passing["Total"]["Cmp%"], squad.passing["Total"]["TotDist"],
    squad.passing["Total"]["PrgDist"],
    # Passing Short
    squad.passing["Short"]["Cmp"], squad.passing["Short"]["Att"],
    squad.passing["Short"]["Cmp%"],
    # Passing Medium
    squad.passing["Medium"]["Cmp"], squad.passing["Medium"]["Att"],
    squad.passing["Medium"]["Cmp%"],
    # Passing Long
    squad.passing["Long"]["Cmp"], squad.passing["Long"]["Att"],
    squad.passing["Long"]["Cmp%"],
    # Expected Passing
    squad.passing["Expected"]["Ast"], squad.passing["Expected"]["xAG"],
    squad.passing["Expected"]["xA"], squad.passing["Expected"]["A-xAG"],
    squad.passing["Expected"]["KP"], squad.passing["Expected"]["1/3"],
    squad.passing["Expected"]["PPA"], squad.passing["Expected"]["CrsPA"],
    squad.passing["Expected"]["PrgP"],
    # Pass Types
    squad.pass_types["Pass Types"]["Live"], squad.pass_types["Pass Types"]["Dead"],
    squad.pass_types["Pass Types"]["FK"], squad.pass_types["Pass Types"]["TB"],
    squad.pass_types["Pass Types"]["Sw"], squad.pass_types["Pass Types"]["Crs"],
    squad.pass_types["Pass Types"]["TI"], squad.pass_types["Pass Types"]["CK"],
    # Pass Outcomes
    squad.pass_types["Outcomes"]["Cmp"], squad.pass_types["Outcomes"]["Off"],
    squad.pass_types["Outcomes"]["Blocks"],
    # Defensive Actions
    squad.defensive_actions["Tackles"]["Tkl"], squad.defensive_actions["Tackles"]["TklW"],
    squad.defensive_actions["Tackles"]["Def 3rd"], squad.defensive_actions["Tackles"]["Mid 3rd"],
    squad.defensive_actions["Tackles"]["Att 3rd"],
    squad.defensive_actions["Challenges"]["Tkl"], squad.defensive_actions["Challenges"]["Att"],
    squad.defensive_actions["Challenges"]["Tkl%"], squad.defensive_actions["Challenges"]["Lost"],
    # Possession
    squad.possession["Touches"]["Touches"], squad.possession["Touches"]["Def Pen"],
    squad.possession["Touches"]["Def 3rd"], squad.possession["Touches"]["Mid 3rd"],
    squad.possession["Touches"]["Att 3rd"], squad.possession["Touches"]["Att Pen"],
    squad.possession["Touches"]["Live"],
    squad.possession["Take-Ons"]["Att"], squad.possession["Take-Ons"]["Succ"],
    squad.possession["Take-Ons"]["Succ%"], squad.possession["Take-Ons"]["Tkld"],
    squad.possession["Take-Ons"]["Tkld%"],
    squad.possession["Carries"]["Carries"], squad.possession["Carries"]["TotDist"],
    squad.possession["Carries"]["ProDist"], squad.possession["Carries"]["ProgC"],
    squad.possession["Carries"]["1/3"], squad.possession["Carries"]["CPA"],
    squad.possession["Carries"]["Mis"], squad.possession["Carries"]["Dis"],
    # Miscellaneous Stats
    squad.misc_stats["Performance"]["Fls"], squad.misc_stats["Performance"]["Fld"],
    squad.misc_stats["Performance"]["Off"], squad.misc_stats["Performance"]["Crs"],
    squad.misc_stats["Performance"]["OG"], squad.misc_stats["Performance"]["Recov"],
    squad.misc_stats["Aerial Duels"]["Won"], squad.misc_stats["Aerial Duels"]["Lost"],
    squad.misc_stats["Aerial Duels"]["Won%"]
]
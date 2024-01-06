import pandas as pd
data_train = pd.read_csv('data/csgo_round_train.csv')
data_test = pd.read_csv('data/csgo_round_test.csv')

data_train
data_train.info()

unused_columns = ["ct_weapon_r8revolver", "t_weapon_r8revolver", "t_weapon_usps", "ct_weapon_p2000", "t_weapon_p2000", "ct_weapon_negev",                  "t_weapon_negev", "ct_weapon_mp5sd", "t_weapon_mp5sd", "ct_weapon_m249", "t_weapon_m249", "ct_weapon_g3sg1", "t_weapon_g3sg1",                "ct_weapon_cz75auto", "t_weapon_cz75auto", "ct_weapon_bizon", "t_weapon_bizon", "ct_weapon_elite", "t_weapon_elite", "ct_weapon_nova", "t_weapon_nova", "ct_weapon_sawedoff", "t_weapon_sawedoff", "ct_weapon_scar20", "t_weapon_scar20", "ct_weapon_tec9", "t_weapon_fiveseven", "ct_weapon_mag7", "t_weapon_mag7", "ct_weapon_p90", "t_weapon_p90", "ct_weapon_glock", "t_weapon_glock","ct_weapon_ump45", "t_weapon_ump45", "ct_weapon_usps", "t_weapon_usps", "ct_weapon_fiveseven", "ct_weapon_xm1014", "t_weapon_xm1014", "ct_weapon_galilar", "t_weapon_galilar", "ct_weapon_famas", "t_weapon_famas", "ct_weapon_mac10", "t_weapon_mp7", "t_weapon_mp9", "ct_grenade_decoygrenade", "t_grenade_decoygrenade", "t_weapon_tec9", "t_weapon_aug", "t_weapon_m4a1s", "t_weapon_m4a4", "ct_weapon_mp9", "ct_weapon_mp7", "ct_weapon_sg553", "ct_weapon_p250", "t_weapon_p250"]

data_train_uwu = data_train.copy()
data_train_uwu = data_train_uwu.drop(unused_columns, axis=1)
data_train_uwu["ct_grenade_incendiarygrenade"] = data_train_uwu["ct_grenade_incendiarygrenade"] + data_train_uwu["ct_grenade_molotovgrenade"]
data_train_uwu["t_grenade_incendiarygrenade"] = data_train_uwu["t_grenade_incendiarygrenade"] + data_train_uwu["t_grenade_molotovgrenade"]
data_train_uwu = data_train_uwu.drop(["ct_grenade_molotovgrenade", "t_grenade_molotovgrenade"], axis=1)
data_train = data_train_uwu.copy()

from vizual.vizual_lib import VizualLib

vizual = VizualLib(data_train, "round_winner")
vizual.heat_map()
data_train.info()
features = ["ct_score", "t_score", "map", "bomb_planted", "ct_money", "t_money", "ct_health", "t_health", "ct_armor", "t_armor", "ct_helmets", "t_helmets", "ct_defuse_kits", "ct_players_alive", "t_players_alive", "ct_grenade_hegrenade", "t_grenade_hegrenade", "ct_grenade_flashbang", "t_grenade_flashbang", "ct_grenade_smokegrenade", "t_grenade_smokegrenade", "ct_grenade_incendiarygrenade", "t_grenade_incendiarygrenade", "ct_weapon_ak47", "t_weapon_ak47", "ct_weapon_awp", "t_weapon_awp", "ct_weapon_m4a1s", "ct_weapon_m4a4", "ct_weapon_deagle", "t_weapon_deagle", ]
data_train_y = data_train["round_winner"]
data_train = data_train[[features, "round_winner"]]
data_train
vizual = VizualLib(data_train, "round_winner")
vizual.heat_map()
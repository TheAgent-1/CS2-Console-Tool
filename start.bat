steamcmd\\steamcmd.exe +force_install_dir ../cs2_server/ +login anonymous +app_update 730 validate +quit
cd server\\game\\bin\\win64
start /wait cs2.exe -dedicated -usercon -console -secure -dev +game_type 0 +game_mode 1 +sv_logfile 1 -serverlogging +sv_setsteamaccount 392CDDAF8900FA00311EA404293006A7 + sv_cheats 1 +map de_ancient +exec perf.cfg +exec bot_ai.cfg
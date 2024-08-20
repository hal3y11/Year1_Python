bandwith = 1000
users = 200
app_A = 200000
app_B = 100000
app_C = 350000

bandwith_bps = bandwith * 1000000
old_apps = app_A + app_B
current_usage = old_apps * users
current_availability = bandwith_bps - current_usage
all_apps = app_A + app_B + app_C
new_bandwith_usedbps = all_apps * users
new_bandwith_usedmbps = new_bandwith_usedbps / 1000000
new_bandwith_availabillity = bandwith - new_bandwith_usedmbps

print("The network capacity in bps: " + str(bandwith_bps))
print("The current usage in bps: " + str(current_usage))
print("The current availability in bps: " + str(current_availability))
print("The new applications requirements in bps: " + str(app_C))
print("The bandwidth available if the new application is installed (in Mbps): " + str(new_bandwith_availabillity))
#Hockey GDT Template generator, courtesy of /u/Tullyswimmer:
#Version 1.0, written Jan 16, 2017

import re

print "\nWelcome to the hockey GDT generator, please follow the instructions on the screen."
print "\nNOTE: All input will show up *exactly* as typed in. Please be careful. You can always run it again if you want."
print "--------------------------------------------------------"

def time_adjust(h,m,z):
	h = int(h)
	m = int(m)
	ta_AT = 0
  	ta_ET = 0
	ta_CT = 0
	ta_MT = 0
	ta_PT = 0
	
	if z == "ET":
		ta_AT = h + 1
		ta_ET = h
		ta_CT = h - 1
		ta_MT = h - 2
		ta_PT = h - 3
		return ta_AT, ta_ET, ta_CT, ta_MT, ta_PT
	elif z == "CT":
		ta_AT = h + 2
		ta_ET = h + 1
		ta_CT = h
		ta_MT = h - 1
		ta_PT = h - 2
		return ta_AT, ta_ET, ta_CT, ta_MT, ta_PT
	elif z == "MT":
		ta_AT = h + 3
		ta_ET = h + 2
		ta_CT = h + 1
		ta_MT = h
		ta_PT = h - 1
		return ta_AT, ta_ET, ta_CT, ta_MT, ta_PT
	elif z == "PT":
		ta_AT = h + 4
		ta_ET = h + 3
		ta_CT = h + 2
		ta_MT = h + 1
		ta_PT = h
		return ta_AT, ta_ET, ta_CT, ta_MT, ta_PT
	else:
		print "invalid time or timezone\n"
		return ta_AT, ta_ET, ta_CT, ta_MT, ta_PT
	

home_team = raw_input("Home team: ")
away_team = raw_input("Away team: ")
time = raw_input("Local time: ")
timezone = raw_input("Time zone (use ET/CT/MT/PT): ")
date = raw_input("Date (MM/DD/YYYY): ")
home_sub = raw_input("Home subreddit: ")
away_sub = raw_input("Away subreddit: ")
home_icon = "[](%s)" % home_sub
away_icon = "[](%s)" % away_sub


date_parsed = date.split("/")

time_vals = time.split(":")
minute_val = re.sub("\D", "", time_vals[1])
minute_val = minute_val.rstrip()

time_list = time_adjust(time_vals[0],minute_val,timezone)
time_list = list(time_list)

t = 0
while t <= 4:
	c = time_list[t]
	if c < 1:
		c = c + 12
		c = str(c)
		time_list[t] = c + ":" + minute_val + "_AM"
		t += 1
	else:
		c = str(c)
		time_list[t] = c + ":" + minute_val + "_PM"
		t += 1
#print time_list
filename = "GDT_" + date_parsed[2] + date_parsed[1] + date_parsed[0] + ".txt"
template = open(filename, 'wb')
template.write("# [%s](%s) at [%s](%s), %s" % (away_team, away_sub, home_team, home_sub, date))

template.write("## Time:")
template.write("|PST|MST|CST|EST|AST|")
template.write(":--:|:--:|:--:|:--:|:--:")
template.write("|%s|%s|%s|%s|%s|" % (time_list[4], time_list[3], time_list[2], time_list[1], time_list[0]))

template.write("# Scoring Summary:")
template.write("|Score|Period|Time|Team|Player|Assists|")
template.write(":--:|:--:|:--:|:--:|:--:|:--:")
template.write(" | | | | | ")

template.write("# Penalty Summary:")
template.write("Time|Period|Team|Player|Call|PIM|")
template.write(":--:|:--:|:--:|:--:|:--:|:--:")
template.write(" | | | | | ")

template.write(" #Shots:")
template.write("|Team|1st|2nd|3rd|OT|Total|")
template.write(":--:|:--:|:--:|:--:|:--:|:--:")
template.write("%s ||||||" % home_icon)
template.write("%s ||||||" % away_icon)

template.write(" #Projected lineups: ")
template.write("(will be moved to comment later)" )
template.write("|%s LW|%s C|%s RW|" % (home_icon, home_icon, home_icon))
template.write(":--:|:--:|:--:")
template.write("L1|L1|L1")
template.write("L2|L2|L2")
template.write("L3|L3|L3")
template.write("L4|L4|L4\n")

template.write("%s LD|%s RD" % (home_icon, home_icon))
template.write(":--:|:--:")
template.write("D1|D1")
template.write("D1|D1")
template.write("D1|D1\n")

template.write("|%s G|" % home_icon)
template.write(":--:")
template.write("|SG|")
template.write("|BG|\n")

template.write("|%s injuries|" % home_icon)
template.write(":--:")
template.write("||\n")

template.write("|%s LW|%s C|%s RW|" % (away_icon, away_icon, away_icon))
template.write(":--:|:--:|:--:")
template.write("L1|L1|L1")
template.write("L2|L2|L2")
template.write("L3|L3|L3")
template.write("L4|L4|L4\n")

template.write("%s LD|%s RD" % (away_icon, away_icon))
template.write(":--:|:--:")
template.write("D1|D1")
template.write("D1|D1")
template.write("D1|D1\n")

template.write("|%s G|" % away_icon)
template.write(":--:")
template.write("|SG|")
template.write("|BG|\n")

template.write("|%s injuries|" % away_icon)
template.write(":--:")
template.write("||\n")

template.write("# Highlights:")

template.write("this GDT based off of a template created by /u/tullyswimmer's script")

print "\n\nYour template is ready at %s" % filename
print "You still manually have to put in lineups, penalties, shots, and goals\n\n"


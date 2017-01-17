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

def date_check(d,good):
	if not re.match('[0-1][0-9]\/[0-3][0-9]\/[2][0][1-9][0-9]', d):
		good_date = False
		print "invalid date, please try again"
		return good_date
	else:
		 good_date = True
		 return good_date

def sub_check(team, real_sub):
	if not re.match('\/r\/[?:a-z]*', team):
		real_sub = False
		print "Please use the correct '/r/' notation for the sub"
		return real_sub
	else:
		real_sub = True
		return real_sub

def time_check(gametime,good_time):
	if not (re.match('[0-1][0-2]\:[0-5][0-9]\s[A,P][M]', gametime) or re.match('[0-9]\:[0-5][0-9]\s[A,P][M]', gametime)):
		print "invalid time"
		good_time = False
		return good_time
	else:
		good_time = True
		return good_time

def zone_check(gamezone, good_zone):
	if not re.match('[E,C,M,P][T]', gamezone):
		print "invalid time zone"
		good_zone = False
		return good_zone
	else:
		good_zone = True
		return good_zone


home_team = raw_input("Home team: ")
away_team = raw_input("Away team: ")
gametime = False
gamezone = False

while gametime == False:
	time = raw_input("Local time (i.e. 7:00 PM): ")
	gametime = time_check(time, gametime)

while gamezone == False:
	timezone = raw_input("Time zone (use ET/CT/MT/PT): ")
	gamezone = zone_check(timezone,gamezone)

good_date = False
while good_date == False:
	date = raw_input("Date (MM/DD/YYYY): ")
	good_date = date_check(date, good_date)

arena = raw_input("Arena: ")

good_home_sub = False
good_away_sub = False

while good_home_sub == False:
	home_sub = raw_input("Home subreddit: ")
	home_sub = home_sub.lower()
	good_home_sub = sub_check(home_sub, good_home_sub)

while good_away_sub == False:
	away_sub = raw_input("Away subreddit: ")
	away_sub = away_sub.lower()
	good_away_sub = sub_check(away_sub, good_away_sub)

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
		time_list[t] = c + ":" + minute_val + " AM"
		t += 1
	else:
		c = str(c)
		time_list[t] = c + ":" + minute_val + " PM"
		t += 1
#print time_list

create_date = date_parsed[2] + date_parsed[1] + date_parsed[0]

filename = "GDT_" + create_date + ".txt"
template = open(filename, 'wb')
template.write("# [%s](%s) at [%s](%s)\n\n %s - %s" % (away_team, away_sub, home_team, home_sub, date, arena))

template.write("\n\n# Time:\n")
template.write("|PST|MST|CST|EST|AST|\n")
template.write(":--:|:--:|:--:|:--:|:--:\n")
template.write("|%s|%s|%s|%s|%s|\n\n" % (time_list[4], time_list[3], time_list[2], time_list[1], time_list[0]))

template.write("# Scoring Summary:\n")
template.write("|Score|Period|Time|Team|Player|Assists|\n")
template.write(":--:|:--:|:--:|:--:|:--:|:--:\n")
template.write(" | | | | | \n\n")

template.write("# Penalty Summary:\n")
template.write("Time|Period|Team|Player|Call|PIM|\n")
template.write(":--:|:--:|:--:|:--:|:--:|:--:\n")
template.write(" | | | | | \n\n")

template.write("#Shots:\n")
template.write("|Team|1st|2nd|3rd|OT|Total|\n")
template.write(":--:|:--:|:--:|:--:|:--:|:--:\n")
template.write("%s ||||||\n" % home_icon)
template.write("%s ||||||\n\n" % away_icon)

template.write("#Projected lineups: \n")
template.write("(will be moved to comment later)\n\n" )
template.write("|%s LW|%s C|%s RW|||%s LW|%s C|%s RW|\n" % (home_icon, home_icon, home_icon, away_icon, away_icon, away_icon))
template.write(":--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:\n")
template.write("|||||||||\n")
template.write("|||||||||\n")
template.write("|||||||||\n")
template.write("|||||||||\n\n")

template.write("%s LD|%s RD|||%s LD|%s RD\n" % (home_icon, home_icon, away_icon, away_icon))
template.write(":--:|:--:|:--:|:--:|:--:|:--:|:--:\n")
template.write("|||||||\n")
template.write("|||||||\n")
template.write("|||||||\n\n")

template.write("|%s G||%s G|\n" % (home_icon, away_icon))
template.write("|:--:|:--:|:--:|:--:|:--:|\n")
template.write("||||\n")
template.write("||||\n\n")

template.write("|%s injuries|||%s injuries|\n" % (home_icon, away_icon))
template.write(":--:|:--:|:--:|:--:\n")
template.write("|||||\n\n")

template.write("# Highlights:\n")

template.write("\nthis GDT based off of a template created by /u/tullyswimmer's script\n")

print "\n\nYour template is ready at %s" % filename
print "You still manually have to put in lineups, penalties, shots, and goals\n\n"

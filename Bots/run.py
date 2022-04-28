from telegramBot import TelegramBot
#Calling the bot
obj_telegram = TelegramBot()

print("Initiating bot...")
print("Choose target group")

#Calling the functions
#1st function to call the groups
group_target = obj_telegram.get_groups()
#2nd function to get the members
members = obj_telegram.get_members(group_target)

print("%s members found in the group." % len(members))
print("Choose the group which you want to add the new members:")

#select one group to send the members
my_group = obj_telegram.get_groups()

#add members command
for member in members:
    added = obj_telegram.add_member_to_group(member, my_group)
    if added:
        print("Member %s successfully added" % member.id)
from telegramBot import TelegramBot

obj_telegram = TelegramBot()

print("Initiating bot...")
print("Choose target group")
group_target = obj_telegram.get_groups()
members = obj_telegram.get_members(group_target)

print("%s members found in the group." % len(members))

print("Choose the group which you want to add the new members:")
my_group = obj_telegram.get_groups()

for member in members:
    added = obj_telegram.add_member_to_group(member, my_group)
    if added:
        print("Member %s successfully added" % member.id)
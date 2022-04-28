from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import time
from configTlgBot import api_hash, api_id, phone

#creating a class for the bot
class TelegramBot():
    #connect with telegram client
    #External file with the API of your own number for telegram (configTlgBot.py)
    def __init__(self)->None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)
        self.connect()

    #First connection only, type the code to connect the trusted device
    def connect(self):
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)
            self.client.sign_in(self.phone, input("Type the code:"))
        return True

    #get the groups in telegram channels
    def get_groups(self):
        groups = []
        chats = self.client(GetDialogsRequest(offset_date=None, offset_id=0, offset_peer=InputPeerEmpty(),limit=5, hash=0))
        for chat in chats.chats:
            #print(chat)
            try: #choosing only mega groups (public groups)
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        #choose one of the groups found
        print("Choose a group:")
        i=0
        for group in groups:
            print(str(i)+' - '+ group.title)
            i+=1

        choice = input("Type the index number of a group: ")
        group_target = groups[int(choice)]

        return group_target

    #get the members of the selected group
    def get_members(self, target_group):
        all_participants = self.client.get_participants(target_group, aggressive=False)
        return all_participants

    #add the members of the selected group to another group
    def add_member_to_group(self, user, target_group):
        target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

        try:
            print("Adding user %s" % user.id)
            user_to_add = InputPeerUser(user.id,user.access_hash)
            self.client(InviteToChannelRequest(target_group_entity, [user_to_add]))

            #time to not get into flood error. Useful for 2-3 minutes
            time.sleep(120)

            return True

        #error if it's doing too many tries
        except PeerFloodError:
            print("Flood error. Sleeping for one hour.")
            time.sleep(3600)
            return False

        #error if a user has a privacy restriction
        except UserPrivacyRestrictedError:
            print("User doesn't allow to be added in the group.")
            return False

        except Exception as e:
            print(str(e))
            return False



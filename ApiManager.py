import requests
import pprint
import shared
import webbrowser

pp = pprint.PrettyPrinter(indent=4)
API_URL = "https://api.intra.42.fr/"

class ApiManager():
    token = ""
    message_ids = []

    def get_token(self):
        CALLBACK = "https%3A%2F%2Fprofile.intra.42.fr"
        webbrowser.open(API_URL + "oauth/authorize?client_id="+shared.uid+"&redirect_uri="+CALLBACK+"&response_type=code&scope=public%20forum")
        code = input("Enter code here:")
        data = {
            'grant_type': 'authorization_code',
            'client_id': shared.uid,
            'client_secret': shared.secret,
            'code': code,
            'redirect_uri': 'https://profile.intra.42.fr'
        }
        r = requests.post("https://api.intra.42.fr/oauth/token", data)
        print("Token:", r.content)
        json = r.json()
        self.token = json['access_token']

    def get_topic_messages(self, topic_id):
        print(topic_id)
        topics_messages_url = API_URL + "v2/topics/" + topic_id + "/messages"

        headers = {'Authorization': 'Bearer ' + self.token}
        r = requests.get(topics_messages_url, headers=headers)
        print("Topics:", r.status_code, r.reason)
        ret = r.json()
        print("Topics count:", len(ret))
        pp.pprint(ret)
        for x in ret:
            id = x['id']
            self.message_ids.append(id)

    def new_message(self, topic_id, content):
        new_message_url = API_URL + "v2/topics/" + topic_id + "/messages"
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }

        data = {
            'message': {
                'author_id': None,
                'content': content,
                'messageable_id': "7",
                'messageable_type': "Topic"
            }
        }
        r = requests.post(new_message_url, headers=headers, json=data)
        print("New Msg:", r.status_code, r.reason, r.content)
        # ret = r.json()
        # pp.pprint(ret)


    def upvote(self, message_id_start):
        for i in range(0,200):
            new_upvote_url = API_URL + "v2/messages/" + str(message_id_start) + "/votes"
            print(new_upvote_url)
            headers = {
                'Authorization': 'Bearer ' + self.token,
                'Content-Type': 'application/json'
            }

            vote = {
                "kind": "upvote",
                "message_id": message_id_start,
                "user_id": "29440"
            }
            r = requests.post(new_upvote_url, headers=headers, json=vote)
            print("Upvote:", r.status_code, r.reason)
            message_id_start += 1

    def get_me(self):
        me_url = API_URL + "v2/me"
        print(self.token)
        headers = {'Authorization': 'Bearer ' + self.token}
        r = requests.get(me_url, headers=headers)
        print("Me:", r.status_code, r.reason)
        # ret = r.json()
        # pp.pprint(ret)


import ApiManager as api
import BibleParser as bible

if __name__ == '__main__':
    bible = bible.BibleParser()
    book = bible.readBible()

    manager = api.ApiManager()
    manager.get_token()
    topic_id = '20914'
    manager.get_topic_messages(topic_id)
    # manager.get_user(29441)
    # manager.new_message(topic_id, "TEST")
    # for i in range(0, 200):
    #     manager.new_message(topic_id, book[i])
    for i in range(0, 70):
        manager.upvote(29543+i)





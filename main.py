import ApiManager as api
import BibleParser as bible

if __name__ == '__main__':
    bible = bible.BibleParser()
    book = bible.readBible()

    manager = api.ApiManager()
    manager.get_token()
    topic_id = '20914'
    # manager.get_topic_messages(topic_id)
    # for i in range(0, 200):
    #     manager.new_message(topic_id, book[i])
    manager.upvote(127496)





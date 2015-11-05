from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def __init__(self, file):
        #StreamListener.__init__(self)
        self.file = file

    def on_data(self, data):
        try:
            with open(self.file, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 

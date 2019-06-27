from fbchat import Client,log
from fbchat.models import *
import apiai,codecs,json

class Jarvis(Client):
	
	def apiaicon(self):
		self.CLIENT_ACCESS_TOKEN="e1f0a56c9ce14c3f9a9c491e228a1142"
		self.ai=apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
		self.request=self.ai.text_request()
		self.request.lang='de'
		self.request.session_id="<SESSION ID,UNIQUE FOR EACH USER>"
	
	def onMessage(self,author_id=None,message_object=None,thread_id=None,thread_type=ThreadType.USER,**kwargs):
		self.markAsRead(author_id)
		
		log.info("Message {} from {} in {}".format(message_object,thread_id,thread_type))
		
		self.apiaicon()
		
		msgText=message_object.text
		
		self.request.query=msgText
		
		response=self.request.getresponse()
	
		reader = codecs.getdecoder("utf-8")
		obj=json.load(response)
		reply=obj['result']['fulfillment']['speech']
		
		if author_id!=self.uid:
			self.send(Message(text=reply),thread_id=thread_id,thread_type=thread_type)
			
		self.markAsDelivered(author_id,thread_id)
			
client=Jarvis('Your Email','Your Password')
client.listen()
		

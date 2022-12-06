#you can't manipulate files 
#it never fully loads the file so very cost effective
import xml.sax
#we need a handler and a parser
#parser translates the file
#handler = xml.sax.ContentHandler() would work but
#instead, we will customize our handler
class GroupHandler(xml.sax.ContentHandler):
	def startElement(self,name,attrs):
		self.current = name
		if self.current == "person":
			print("----preson--\n")
			print("ID: {}".format(attrs['id']))
	
	def characters(self, content):
		if self.current == "name":
			self.name == content
		elif self.current == "age":
			self.age == content
		elif self.current == "weight":
			self.weight == content
		elif self.current == "height":
			self.height == content
			
	def endElement(self, name):
		if self.current == "name":
			print("Name: {}".format(self.name))
		if self.current == "name":
			print("Name: {}".format(self.name))
			

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')

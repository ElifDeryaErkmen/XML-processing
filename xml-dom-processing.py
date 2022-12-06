#DOM-XML-proccesing.py
import xml.dom.minidom

from matplotlib.font_manager import _Weight

domtree = xml.dom.minidom.parse("data.xml")
group = domtree.documentElement#group is the root of the domtree

persons = group.getElementByTag('person')

for person in persons:
        print("----------PERSON---------")
        if person.hasAttribute('id'):
            print("ID: {}".format(person.getAttribute('id')))

        print("Name: {}".format(person.getElementsByTagName('name').childNodes[0].data))
        print("Age: {}".format(person.getElementsByTagName('age').childNodes[0].data))
        print("Weight: {}".format(person.getElementsByTagName('weight').childNodes[0].data))
        print("Height: {}".format(person.getElementsByTagName('height').childNodes[0].data))
persons(2).getElementsByTagName('name')[0].childNode[0].nodeValue = "New Name"
persons(0).setAttribute('id','100')#we have to pass it as string
#we have changed the values stored in the ram
domtree.writexml(open('data.xml','w'))
#we have changed the xml file

#create new elemets and add them
newperson = domtree.createElement('person')
newperson.setAttribute('id','6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('princess Diana'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('19'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('195'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('90'))

newperson.appendchild(name)
newperson.appendchild(age)
newperson.appendchild(weight)
newperson.appendchild(height)

group.appendChild(newperson)

domtree.writexml(open('data.xml','w'))

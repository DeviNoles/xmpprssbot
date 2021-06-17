import xmpp
jabberid = ""
password = ""
receiver = ""
message  = " hello world "

def receive_muc(self, muc_room):

    client=xmpp.protocol.JID(self.jid)

    cl = xmpp.Client(client.getDomain(), debug=[])

    cl.connect()

    cl.auth(client.getNode(),self.passw)


    cl.sendInitPresence()

    cl.RegisterHandler('message', self.messageCB)

    room = muc_room
    print("Joining " + room)

    cl.send(xmpp.Presence(to="%s %s" % (room, self.jid)))
    self.send_muc("I'm online !", room)

    self.GoOn(cl)




jid = xmpp.protocol.JID(jabberid)
connection = xmpp.Client(server=jid.getDomain())
connection.connect()
connection.auth(user=jid.getNode(), password=password, resource=jid.getResource())
connection.send(xmpp.protocol.Message(to=receiver,body=message))
connection.sendInitPresence()
room = "memes"
print("Joining " + room)


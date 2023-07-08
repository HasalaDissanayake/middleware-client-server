# middleware-client-server

### Task 1: 

The Client-Server Application
1. Implement a client-server socket application using a preferred programming language. 
The server will listen for connections on a pre-defined PORT where the client will use the 
server IP and the PORT to connect to the server.
2. The implementation only needs a Command Line Interface (CLI) to show the activities 
between the Server and the Client applications. Using a Graphical User Interface (GUI) 
based implementation will not influence the assignment to be graded higher than a CLI 
based implementation.
3. Start the Server by passing the PORT as a command line argument.
E.g. 
my_server_app 5000 
4. Start a Client to connect with the server by passing Server IP and Server PORT as 
command line arguments.
E.g. 
my_client_app 192.168.10.2 5000 
5. After starting the Client, whatever text typed on the client CLI should be displayed on the 
server side CLI as standard system output text.
6. The primary objective is to demonstrate the client and server communicating with each 
other.
7. Client should perpetually run until the “terminate” keyword is typed by a user. 
Subsequent to typing the keyword, the client should disconnect from the server and 
terminate.

### Task 2: 

Publishers and Subscribers
1. Improve the client-server implementation for the Server to handle multiple concurrent 
Client connections.
2. Multiple client applications should be able to connect to the server and the typed text in a 
given client CLI should be displayed on the Server terminal CLI.
3. The client application should take the third command line argument to indicate whether 
the client will act as either “Publisher” or “Subscriber”.
E.g. 
my_client_app 192.168.10.2 5000 PUBLISHER
my_client_app 192.168.10.2 5000 SUBSCRIBER
4. Further, the server should echo the messages sent by any “Publisher” clients to all the 
“Subscriber” clients terminals. For example, when a single server is connected with 10 
client applications, when client terminal that is in Publisher mode type a text, it should 
be displayed on all remaining client terminals that are connected as Subscribers.
5. The Publisher messages should be only shown on Subscriber terminals, not on any 
Publisher terminals.

### Task 3: 

Publishers and Subscribers Filtered on Topics/Subjects
1. Improve the implementation of Task 2 to include “topic/subject” based filtering of 
messages among Publishers and Subscribers.
2. The client implementation should be improved to include the forth command line 
argument of the topic/subject of either the publisher or subscriber.
E.g. 
my_client_app 192.168.10.2 5000 PUBLISHER TOPIC_A
my_client_app 192.168.10.2 5000 SUBSCRIBER TOPIC_A
3. The client application that is a publisher should be sending the messages to the server on
a specific topic/subject to route to interested subscriber clients on the same 
topic/subject.
4. There can be publishers and subscribers interested in different messages connected 
concurrently to the server.

### Task 4: 

Enhance the Architecture to Gain Improvement in Availability and Reliability 
A single server-based architecture for the distribution of messages among Publishers and 
Subscribers developed in this assignment has a single point of failure - the server. Propose a 
new distributed architecture for the Pub/Sub implementation to gain improved availability 
and reliability over the single server node failure deficiency. Only required to draw and 
describe the new architecture and improvements to the implementation is not expected.

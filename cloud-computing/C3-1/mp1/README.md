David Liang 
C3-1 Project 1 - Membership protocol
Implementing a specific protocol between all-to-all heartbeats, gossip-style heartbeats, and SIM. 

I am going to implement gossip-style as it's alot more straightforward compared to SWIM and it's better than heartbeat in my opinion. It takes up to O(lg n) to propagate compared to all to all and it is easier to implement than SWIM for my current state.

Sidenote: Due now poorly the comments are written here, I have written in my comments to clarify what I gotta do to make this work. and some trivial things in the sense.

## Notes for self 
What i am getting from the instruction 
1. don't touch application.cpp/h, Enum.cpp/h, and everything else
2. touch only MP1Node.cpp/h for the most part 
3. right now just read up on what to do and what to do stuff.

TODO: Understand how sending a message works and how to reply back to the node that is requesting to join I believe
Basically, the introducer will send a JOINREQ in which i have to implement and reply back with a JOINREP. Implementing JOINREP requires that I specify the cluster list and let them join in. 

## How does it work
### Selected Protocol
1. Nodes periodically gossip their membership list 
2. on receipt, the local membership list is updated

Each node or member in this case has a membership table. Each membership table has 3 columns: address, heartbeat counter, and local time when that heartbeat counter was updated
For each "gossip" to each node, the later heartbeat will replace each less than heartbeat counter and set the time as new. if each heartbeat is less than the "gossip" do nothing.
3. For failures, if a heartbeat has not increased for more than Tfail seconds, then it is marked as failure. After Tcleanup, then it is deleted to avoid of it coming back due to other node containing that specific address.

### What does the current Implementation do or the template code? 
1. It obviously emulates a distributed system that repeatedly sends message to each other for whatever the global time is
2. Then depending on which test case, it will fail specific and random nodes to test for my implementation of failure detection cases. 
    1. This is what i will do
3. After all is done, it will delete everything and clean up

## Questions to self
1. How are the params class set? The program seems to run apps and somehow all the values are set concurrent? no idea. 
    1. there is a constructor that sets all the values
2. Do I just have to set up the protocol itself? 
    1. Yeah, since the memberNode, membership, and membershiList are set up. This means I would have to understand what exactly they're doing and implement the protocol based on them as I cannot modify it.
3. Where does the heartbeat start at in the code? 
    1. Mp1::nodeLoop() should be the location
4. What does recvCallBack really do? It handles different types of messages but what does that mean in the grand plan of things? 
    1. It handles the ACK from a node to join the group I guess? 
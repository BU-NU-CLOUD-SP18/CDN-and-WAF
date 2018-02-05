# CDN with WAF


## Content Distribution Network with Web Application Firewall

CDNs are very crucial to companies that do large scale data distribution, especially companies in streaming media industry such as Netflix. The fundamental idea is that it is faster to pull data from servers that are geographically closer or more accessible to you. In order to meet the demands for high speed and quality of content companies have begun to develop and spin out their own versions of CDN servers in order to distribute data among. Current service providers includes Akamai technologies, Amazon’s AWS, Verizon, etc.  

<hr>

### 1.Vision and Goals Of The Project:
The aim of our project is to design and develop our own version of a CDN with the emphasis on cyber security. The workload will be distributed among virtual cloud instances acting as cache servers. Multiple servers will form a cluster and each of them  has its own role, this includes Data Store, DNS management, REST Web server, and Cache servers. We will develop a backlog visualization tool which allows developers to be able to view common cyber attacks and show mitigations of those attacks. The CDN will be run on cloud servers, particularly, MOC (Massachusetts Open Cloud).<br><br>
Our CDN will need to satisfy the following requirements:

 - 1. Effectively balance workload across multiple computing resources. 
 - 2. Instantiate virtual instances to construct cache servers dynamically. 
 - 3. Log behavior that seems out of order.
 - 4. Provide a RESt-like or REST API to the clients for managing servers.
 - 5. Provide visual interface for demo purposes, developed in React.js.

Our ultimate goal is to generate our own limited CDN with integrated Web Application Firewall and provide an API to manage web services for prospective customers.
<hr>

### 2. Users/Personas Of The Project:

CDN with WAF will be used by the website owner who  want to be able to scale their web services without adding their own infrastructure or want to scale their load for flash crowds without investing a lot of money for the hardware.
<hr>

### 3. Scope and Features Of The Project:
 - We will use virtual machines instances on MOC OpenStack to simulate server behavior in our system.
 - We will be using load generating tools to simulate load of a large number of clients of the customer to validate provide scaling of the customers website.
 - We will customize our own DNS services to guarantee best fetching speed for clients. 
 - We will develop firewall, leveraging mod_security or some WAF technology to filter and track common cyber attacks against our CDN system. 
 - Users can access our provided services via RESTful web APIs deployed.
 - Our system will be presented with web based GUI. 

<hr>

### 4. Solution Concept
#### Current Solution:
Our current proposed solution involves following different components that can be combined to form one complete service.
#### Management Server:
A simple Ubuntu server that has access to other services using ssh  or some other method with which it can poll server status data.

 - The system will keep polling to check the load on cache servers, if the servers  exceeds a certain threshold, the system will start new instances of the cache servers (which will be saved as images).
 - It will load the configuration for the cache servers from the stored configurations which are created when a new user .
 - Every new instance should have the ssh public key for the management server so that it is able to poll for cpu, memory and bandwidth usage (Can just be manually stored in the instance image).
 
#### Origin Server 
Main web server that is being cached in the Varnish Cache servers.

 - This can be a simple model website where we are trying to balance load using cache server.
 - This is where we will test if the website is able to handle high loads (Send huge amounts of traffic here and see if the cache servers are able to distribute the load).
 - A Raspberry Pi with a simple web server can be used to simulate an origin server.

#### Varnish Cache Server
Simple low CPU powered instances with varnish cache installed and pointing to an origin server.

 - These can be be low powered so that they are overloaded easily and we can test the dynamic load balancing feature easily.
 - The management service should have access to all the cache servers so it can poll for current server status to each of them.

#### REST API with React User Interface
Simple front end for the client to be able to check the status for the cache servers (the load, the traffic, CPU, memory, Bandwidth Usage, the number of cache instances that are up). The management server has all the data that the client needs so we could just create a simple flask server on the management and send all the data to a simple web app that the client has access to. (User authentication can be added later)

#### DNS Server
An Ubuntu VM instance can do this job.

- We need the server to be able to direct traffic to a cache server.
- The rules that this server uses to direct traffic can be complex (e.g. based on geolocation of the client, previous visits), but initially, Round Robin should work fine and can be improved upon later if there’s more time.

<figure>
	<a ><img src="/images/BlockDiagram.jpg" alt=""></a>
</figure>

<hr>

### 5. Acceptance criteria
 - Shows clear efficiency in load balancing and latency versus system without CDN.
 - Demonstrates the availability to filter cyber attacks.
 - Provides clients accessible RESTful APIs.  

<hr>

### 6.Demo Plans
Demonstrate Web user interface to display back-end modules and processes.

 - Basic user management functions without infrastructure
 - Data Store Server
 - Management and DNS Management Server

Demonstrate client-side usage with Cache access. 
 - Without load balancing
 - With load balancing but without security layers
 - With security layers

Load Scaling Demonstration (autoscale)


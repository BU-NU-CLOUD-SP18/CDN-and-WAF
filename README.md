# CDN with WAF


## Content Distribution Network with Web Application Firewall

CDNs are crucial, to companies that do large scale data distribution, especially companies in the streaming media industry such as Netflix. The fundamental idea is that it is faster to pull data from servers that are geographically closer or more accessible to you. In order to meet the demands for high speed and quality of content, companies have begun to develop and spin out their own versions of CDN in order to distribute data among servers. Current service providers includes Akamai technologies, Amazon’s AWS, CloudFlare, etc.  

<hr>

### 1.Vision and Goals Of The Project:
The aim of our project is to design and develop our own version of a CDN with the emphasis on cyber security. The workload will be distributed among virtual cloud instances acting as cache servers. Multiple servers will form a cluster and each of them  has its own role, this includes Data Store, DNS management, REST API, Web application server, and Cache servers. We will develop a visualization tool which allows developers to be able to view common cyber attacks and show mitigations of those attacks. The CDN will be run on cloud servers, specifically the MOC (Massachusetts Open Cloud).
Our CDN will need to satisfy the following requirements:
- 1. Effectively balance workload across multiple computing resources.
- 2. Instantiate virtual instances to construct cache servers dynamically. 
- 3. Log behavior that seems unusual.
- 4. Provide a REST-like or REST API to the clients for managing servers.
- 5. Provide visual interface for demo purposes.

Our ultimate goal is to generate our own limited CDN with integrated Web Application Firewall and provide an API to manage web services for prospective customers.

<hr>

### 2. Users/Persons Of The Project:

CDN with WAF will be used by the website owner who want to be able to scale their web services without adding their own infrastructure or want to scale their load for flash crowds without a large capital investment.
<hr>

### 3. Scope and Features Of The Project:

- We will use virtual machines instances on MOC OpenStack to simulate the origin server behavior in our system.
- We will use OpenStack API to generate new instances to achieve auto scaling feature.
- We will customize our own DNS services to guarantee best fetching speed for clients. 
- We will develop firewall, leveraging mod_security or some WAF technology to filter and track common cyber attacks against the customers of our CDN system. 
- Users can access our provided services via RESTful web APIs.
- Our system will be accessed with web based GUI. 

<hr>

### 4. Solution Concept
#### Current Solution:
Our current proposed solution involves following different components that can be combined to form one complete service,
#### Management Server:
A simple Ubuntu server that has access to other services using ssh  or some other method with which it can poll server status data. 

 - The system will keep polling to check the load on cache servers, if the servers  exceeds a certain threshold, the system will start additional instances of the cache servers (which will be saved as images).
 - It will load the configuration for the cache servers from the stored configurations which are created when a new user enters the system .
 - Every new instance should have the ssh public key for the management server so that it is able to poll for cpu, memory and bandwidth usage (Can just be manually stored in the instance image).
 
#### Origin Server 
The origin server is the main web server that is being cached in the Varnish Cache servers.

 - This can be a simple model website where we are trying to balance load using cache server.
 - This is where we will test if the website is able to handle high load (Send huge amounts of traffic here and see if the cache servers are able to distribute the load).
 - A simple static web page can be used to simulate an origin server.

#### Varnish Cache Server
Simple low CPU powered instances with varnish cache installed and pointing to an origin server.

 - These can be be low powered so that they are overloaded easily and we can test the dynamic load balancing feature easily.
 - The management service should have access to all the cache servers so it can poll for current server status to each of them.

#### REST API with React User Interface
The user interface  for the client to be able to check the status for the cache servers (the load, the traffic, CPU, memory, bandwidth usage, the number of cache instances that are up). The management server has all the data that the client needs so we could just create a simple flask server on the management and send all the data to a simple web app that the client has access to. (User authentication can be added later)

#### DNS Server
An Ubuntu VM instance can do this job.

- We need the server to be able to direct traffic to a cache server.
- The rules that this server uses to direct traffic can be complex (e.g. based on geolocation of the client, previous visits), but initially, Round Robin should work fine and can be improved upon later if there’s more time.

<figure>
	<a ><img src="/images/BlockDiagram.jpg" alt=""></a>
</figure>

<hr>

### 5. Acceptance criteria
 - Finish each component in system architecture diagram.
 - Shows clear efficiency in load balancing and latency versus system without CDN.
 - Provides clients web portals and accessible RESTful APIs.  

<hr>

### CDN Service Procedure  

1) Customer has a site at abc.jadedhang.com
  * Has A record pointing  abc.jadedhang.com to 1.1.1.1 as the origin server
2) Register with our CDN
  * configure abc.jadedhang.com to be hosted with the CDN
  * In the UI customer configures hosted sitename and origin server
    ( abc.jadedhang.com and www.jadedhang.com )
  * Mgmt portal tells customer the CNAME pointer to configure for hosted site name   ( probably abc.jadedhang.com.4n4nd.me ) 
3) Customer adds A record for www.jadedhang.com as 1.1.1.1
4) Customer deletes A record for abc.jadedhang.com
5) Customer creates CNAME record for abc.jadedhang.com pointing to abc.jadedhang.com.4n4nd.me

### 6.Timeline
* Sprint1
  * Project design
* Sprint2
  * Merged components and set up instances in MOC
  * Flask Server setup
  * A Varnish Instance was tested as a caching server for a simple HTML website
* Sprint3
  * Setup DNS server
  * PostgresQL database integration
  * Tested Varnish Instance with a sample website
* Sprint4
  * Connect customer’s origin server to our CDN
  * Combine web server database to dns server
  * Redirect user’s request to our cache server 
* Sprint5
  * Configured Varnish Security Firewall
  * Tested VSF event with log
  * Developed auto-scaling 

# Team Members

* Anand Sanmukhani
* Berk Gur
* Hao "Edward" Xu
* Samit "Jade" Dhangwattanotai
* Xuanhao Mi


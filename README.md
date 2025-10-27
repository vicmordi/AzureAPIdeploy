Building a Secure Two-Tier Application Architecture on Microsoft Azure

This project is focused on designing and implementing a secure two-tier architecture for a Journal API application using Microsoft Azure. The goal was to simulate how production grade systems separate public facing services from private data storage for improved security and reliability.

The project involved creating a complete environment from scratch, starting with a new Resource Group, Virtual Network, and subnets. I designed a network that included a public subnet for the API server and a private subnet for the PostgreSQL database. The API VM was given a public IP to host the FastAPI application and frontend through Nginx, while the database VM was deployed without a public IP, ensuring it remained private and accessible only within the virtual network.

To secure communication, I configured Network Security Groups (NSGs) to strictly control inbound and outbound traffic. HTTP traffic was allowed only to the API subnet, while database access on port 5432 was restricted to requests coming solely from the API subnet. A NAT Gateway was added to enable secure outbound connectivity for system updates on the private database VM, and Azure Bastion was configured to allow management access without exposing SSH ports to the internet.

On the API VM, I deployed the FastAPI backend using Uvicorn and Gunicorn under systemd for reliability and configured Nginx to serve the frontend and route API requests. The PostgreSQL database was installed, configured to listen on the private IP, and secured by limiting access to the API VM only.

This project reflects a real-world best practice where the frontend and API are public for user access, but the data layer remains fully private. Such architectures are essential in modern cloud systems to prevent data breaches, enforce least-privilege access, and maintain high security standards across application environments.

#Azure #CloudSecurity #FastAPI #PostgreSQL #Networking #DevOps #Infrastructure #SystemDesign #Python #Nginx #DataProtection


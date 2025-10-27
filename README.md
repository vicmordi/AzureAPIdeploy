Building a Secure Two-Tier Application Architecture on Microsoft Azure

This project is focused on designing and implementing a secure two-tier architecture for a Journal API application using Microsoft Azure. The goal was to simulate how production grade systems separate public facing services from private data storage for improved security and reliability.

The project involved creating a complete environment from scratch, starting with a new Resource Group, Virtual Network, and subnets. I designed a network that included a public subnet for the API server and a private subnet for the PostgreSQL database. The API VM was given a public IP to host the FastAPI application and frontend through Nginx, while the database VM was deployed without a public IP, ensuring it remained private and accessible only within the virtual network.

To secure communication, I configured Network Security Groups (NSGs) to strictly control inbound and outbound traffic. HTTP traffic was allowed only to the API subnet, while database access on port 5432 was restricted to requests coming solely from the API subnet. A NAT Gateway was added to enable secure outbound connectivity for system updates on the private database VM, and Azure Bastion was configured to allow management access without exposing SSH ports to the internet.

On the API VM, I deployed the FastAPI backend using Uvicorn and Gunicorn under systemd for reliability and configured Nginx to serve the frontend and route API requests. The PostgreSQL database was installed, configured to listen on the private IP, and secured by limiting access to the API VM only.

This project reflects a real-world best practice where the frontend and API are public for user access, but the data layer remains fully private. Such architectures are essential in modern cloud systems to prevent data breaches, enforce least-privilege access, and maintain high security standards across application environments.

#Azure #CloudSecurity #FastAPI #PostgreSQL #Networking #DevOps #Infrastructure #SystemDesign #Python #Nginx #DataProtection



![WhatsApp Image 2025-10-27 at 17 05 15_1cf76242](https://github.com/user-attachments/assets/2dafcfab-fa23-4e15-831d-26111d3717a0)


<img width="1919" height="857" alt="Screenshot 2025-10-23 002133" src="https://github.com/user-attachments/assets/c974da9a-008a-4d38-a17a-5099c3b67bf8" />

<img width="1915" height="834" alt="Screenshot 2025-10-23 002200" src="https://github.com/user-attachments/assets/4dfe6965-d8de-44ac-b501-8185bc6aa48c" />

<img width="1919" height="833" alt="Screenshot 2025-10-23 002224" src="https://github.com/user-attachments/assets/d233067f-66c1-40bf-a242-dfb450aa915b" />

<img width="1919" height="863" alt="Screenshot 2025-10-23 002241" src="https://github.com/user-attachments/assets/10026e4b-19aa-4ad6-8296-d985deaf89c5" />

<img width="1919" height="784" alt="Screenshot 2025-10-23 002326" src="https://github.com/user-attachments/assets/da0db1af-1637-451e-b037-3fe04b153f60" />

<img width="1919" height="857" alt="Screenshot 2025-10-23 002443" src="https://github.com/user-attachments/assets/5c1c938b-ecf2-492c-aeb3-51e17d5caaae" />

<img width="1919" height="858" alt="Screenshot 2025-10-23 002501" src="https://github.com/user-attachments/assets/ebfc297d-278a-411e-b8b3-a8069419b7eb" />

<img width="1908" height="910" alt="Screenshot 2025-10-22 193231" src="https://github.com/user-attachments/assets/6e6d230e-126c-40f4-8e5a-b48d2685f795" />

<img width="1903" height="915" alt="Screenshot 2025-10-22 193935" src="https://github.com/user-attachments/assets/de63a9bc-f445-4fa3-94e4-726297a5f3c2" />

<img width="1918" height="970" alt="Screenshot 2025-10-23 002556" src="https://github.com/user-attachments/assets/c265931e-face-45fe-9524-3b469b54f671" />

<img width="1911" height="911" alt="Screenshot 2025-10-23 002543" src="https://github.com/user-attachments/assets/dde724ff-2070-4450-90fb-a108bf7754da" />

<img width="1907" height="909" alt="Screenshot 2025-10-23 002527" src="https://github.com/user-attachments/assets/d2f8b1e0-7c48-445b-be23-eb30da739be4" />



https://github.com/user-attachments/assets/2f50a0ae-479f-4555-a204-39b324f5a85f











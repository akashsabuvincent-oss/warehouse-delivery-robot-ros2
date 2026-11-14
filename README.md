# Warehouse Delivery Robot – ROS 2

## About the Project

This project demonstrates a simple Warehouse Delivery Robot system developed using ROS 2 and Python.

The system uses custom Messages, Services, and Actions to manage package loading, publish robot status, and perform delivery tasks.

## Features

- Publishes the robot's status every second.
- Receives and displays robot status using a Subscriber.
- Accepts packages weighing up to 10 kg.
- Allows a maximum of 5 packages.
- Rejects packages that exceed the weight or package limit.
- Performs delivery tasks using ROS 2 Actions.
- Provides continuous delivery feedback, including remaining distance and completion percentage.

## Technologies Used

- ROS 2
- Python
- Ubuntu Linux
- rclpy
- Custom ROS 2 Interfaces

## Project Structure

```text
akash_warehouse_ws/
│
├── src/
│ ├── warehouse_interfaces/
│ │ ├── msg/
│ │ │ └── DeliveryStatus.msg
│ │ ├── srv/
│ │ │ └── LoadPackage.srv
│ │ ├── action/
│ │ │ └── Deliver.action
│ │ ├── CMakeLists.txt
│ │ └── package.xml
│ │
│ └── warehouse_nodes/
│ ├── warehouse_nodes/
│ │ ├── status_publisher.py
│ │ ├── status_subscriber.py
│ │ ├── deliver_action_server.py
│ │ └── deliver_action_client.py
│ ├── setup.py
│ └── package.xml
│
├── .gitignore
└── README.md
```

##Testing

The following tests were performed:

- Publisher and Subscriber communication.
- Successful package loading.
- Rejection of packages exceeding 10 kg.
- Rejection after reaching the maximum limit of 5 packages.
- Successful delivery using ROS 2 Actions.
- Delivery feedback and completion result.
- Rejection of invalid delivery goals, including zero distance.

## Conclusion

This project helped demonstrate the practical use of ROS 2 communication methods: Topics, Services, and Actions. It also provided hands-on experience with custom interfaces, Python nodes, and package management in ROS 2.

**Project:** Warehouse Delivery Robot  
**Platform:** ROS 2  
**Language:** Python

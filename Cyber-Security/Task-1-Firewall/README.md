# OIBSIP Cyber Security Task 1 - Firewall Simulator

## Project Overview

This project is a simple Firewall Simulator developed using Python.

The firewall checks incoming network packet details such as:

- IP Address
- Port Number
- Protocol

Based on predefined firewall rules, the packet is either:

- ALLOWED
- BLOCKED

The project also records every firewall decision in a log file.

## Objective

The objective of this project is to understand the basic working principle of a firewall and how network traffic can be filtered using predefined security rules.

## Technologies Used

- Python 3
- JSON
- File Handling
- Object-Oriented Programming

## Features

- Load firewall rules from a JSON file
- Check incoming network packets
- Match IP addresses
- Match port numbers
- Match network protocols
- Allow trusted traffic
- Block restricted traffic
- Default BLOCK policy
- Validate port numbers
- Validate TCP/UDP protocols
- Record firewall decisions in a log file

## Project Structure

```text
Task-1-Firewall/
│
├── firewall.py
├── firewall_rules.json
├── firewall_log.txt
├── README.md
└── requirements.txt
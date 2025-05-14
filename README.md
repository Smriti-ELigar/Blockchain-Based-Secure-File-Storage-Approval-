# Blockchain-Based Secure File Storage & Approval System with IPFS

This project is a blockchain-powered file storage and approval system integrated with IPFS (InterPlanetary File System) for decentralized and secure file management. The system ensures transparency, immutability, and security in file handling while leveraging smart contracts for access control and approvals.

Key Features
✅ User Authentication & Metamask Integration – Users can register, log in, and link their MetaMask wallet for transactions.
✅ File Upload & Storage via IPFS – Uploaded files are securely stored on IPFS, generating a unique hash for retrieval.
✅ Blockchain-Based Approval System – Admins can approve or reject file uploads, ensuring verified content.
✅ Incentive Mechanism – Users earn rewards (Bloc Doc Coin - BDC) for high-quality file contributions.
✅ Activity Logging – Tracks all actions (uploads, approvals, access) in an SQLite database for auditing.
✅ Role-Based Access – Distinct functionalities for faculty, admin, and users, with restricted access levels.
✅ Circular Announcements – Admins can broadcast circulars, ensuring effective communication.
✅ Facial Recognition Login (Upcoming) – Face recognition authentication using FaceNet & DeepFace for enhanced security.

Technology Stack
🟢 Backend: Python (Flask), Web3.py, SQLite
🟡 Frontend: HTML, CSS, JavaScript
🔵 Blockchain: Ethereum (Ganache for testing), Solidity (Smart Contracts)
🔗 IPFS Integration: Decentralized file storage
🖥 Face Recognition (Upcoming): DeepFace/FaceNet

System Architecture
User uploads file → File stored in IPFS → Hash stored on blockchain
Admin reviews and approves/rejects → Visibility updated on blockchain
Users access approved files → Logs maintained for security

Future Enhancements
🔹 AI-based document classification
🔹 Smart contract enhancements for advanced permissions
🔹 Full implementation of Face Recognition authentication

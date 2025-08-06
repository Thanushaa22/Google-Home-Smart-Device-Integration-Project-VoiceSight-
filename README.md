# Google-Home-Smart-Device-Integration-Project-VoiceSight
This project involves the successful integration and submission of a smart home device to the Google Home platform using the Google Smart Home ecosystem. It supports device control via Google Assistant and maintains synchronization using HomeGraph APIs

Voice Sight

This demonstrates the successful integration of a smart IoT device into the **Google Home ecosystem**, enabling voice-based control via **Google Assistant**. The project includes support for device discovery, execution, and status reporting using **Google Smart Home APIs**, and has been verified through the **Test Suite for Smart Home (TSSH)**.

---

## 📌 Project Overview

This project allows users to control smart devices (such as lights or fans) through Google Assistant voice commands. The integration covers the entire smart home stack, including:

- Device SYNC (discovery)
- QUERY (current state)
- EXECUTE (actions like turning ON/OFF)
- Real-time state reporting with **Request Sync** and **Report State**

---

## 🚀 Features

- 🔐 OAuth 2.0 based Account Linking
- 🔁 Device SYNC, EXECUTE, and QUERY Intent Handling
- 📡 Real-time updates using Report State & Request Sync
- 📱 Device appears and functions in Google Home App
- ✅ Pass Rate in Google’s Test Suite for Smart Home (TSSH)

---

## 📦 Tech Stack

| Component       | Description |
|----------------|-------------|
| **Backend**     | Node.js with Express or Firebase Cloud Functions |
| **Database**    | Firebase Firestore |
| **Auth**        | OAuth 2.0 (Google-style authorization code flow) |
| **Smart Home**  | Google Smart Home API |
| **Testing**     | Test Suite for Smart Home (TSSH), HomeGraph Viewer |
| **Tunnel**      | Ngrok or LocalTunnel (for local HTTPS endpoints) |

---

## 🧠 Supported Device & Traits

| Device Type     | Traits Implemented     |
|------------------|-------------------------|
| `action.devices.types.OUTLET` | `action.devices.traits.OnOff` |
| `action.devices.types.LIGHT`  | `action.devices.traits.OnOff`, `action.devices.traits.Brightness` |

You can modify and extend this project to support more device types and traits such as `ColorSetting`, `FanSpeed`, etc.

---

## 🧪 Testing & Certification

- ✅ Passed SYNC, QUERY, and EXECUTE test cases
- ✅ Verified Report State and Request Sync functionality
- ✅ Device appears as expected in Google Home App
- ✅ Fully compliant with Google Smart Home guidelines

---

## 🧑‍💻 Your Role

> 👩‍💻 **Developed**  
> Designed and developed the entire smart home backend, implemented OAuth-based account linking, and ensured compliance with Google’s smart home requirements.

---



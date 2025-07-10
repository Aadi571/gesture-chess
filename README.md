# gesture-chess

A fully **interactive chess game** you can play **hands-free** — control every move using just your **hand gestures** detected through your webcam!

---

## 📌 **Project Highlights**

- 🎥 **Gesture-Based Controls**  
  Select, move, and place chess pieces with your hand — no mouse or keyboard needed!

- 👋 **Real-Time Hand Tracking**  
  Uses **OpenCV** and **MediaPipe** to detect your hand, track your index finger, and map it to the chessboard squares.

- 🤖 **AI Opponent**  
  Play as White using gestures while the computer controls the Black pieces using the `python-chess` library.

- ✨ **Visual Feedback**  
  See live highlights for:
  - Selected pieces
  - Valid moves
  - Active squares under your finger

- ♟️ **Fully Functional Chess Rules**  
  Handles legal moves, captures, promotions, and basic AI replies.

---

## ⚙️ **Tech Stack**

- **Python**
- [OpenCV](https://opencv.org/) – Webcam video feed
- [MediaPipe](https://google.github.io/mediapipe/) – Real-time hand landmark detection
- [Pygame](https://www.pygame.org/) – Visual chessboard & piece rendering
- [python-chess](https://python-chess.readthedocs.io/) – Chess logic, move validation, and AI engine

---

## 🚀 **How It Works**

1️⃣ **Track Hand Landmarks**  
Your webcam feeds frames to MediaPipe, which detects your hand and returns 21 landmarks per hand. The fingertip coordinates are mapped to the chessboard grid.

2️⃣ **Map to Chess Squares**  
Your index finger’s position is converted into a board square. Long-hover or palm gestures confirm piece selection and placement.

3️⃣ **AI Reply**  
After you make a move, the AI plays the next valid legal move automatically.

4️⃣ **Real-Time Feedback**  
Visual highlights in the Pygame window show your selection, possible moves, and the piece being moved.

---

## 📂 **Project Structure**

**

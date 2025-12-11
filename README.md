# 🐢 Algorithm Race: Sorting Visualizer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Turtle](https://img.shields.io/badge/Graphics-Turtle-green?style=for-the-badge)
![NumPy](https://img.shields.io/badge/Math-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

> **A real-time visualization of sorting algorithms using Python's Turtle graphics and NumPy arrays.**

---

## 🚀 Overview

The **Algorithm Race** is a visual tool designed to demonstrate how sorting algorithms process data. By representing numbers as vertical bars, users can watch the **Bubble Sort** algorithm compare, swap, and order elements in real-time. It bridges the gap between raw logic (NumPy) and visual feedback (Turtle).

## ✨ Key Features

* **📊 Dynamic Data Generation:** Uses **NumPy** to generate random arrays of integers for every run.
* **🐢 Real-Time Animation:** Visualizes every single swap operation using **Turtle Graphics**.
* **⚡ Optimized Rendering:** Utilizes `screen.tracer()` logic to render frames instantly for smooth animation.
* **🧼 Auto-Cleaning:** Automatically clears the canvas between frames to prevent visual clutter.


---

## 🛠️ Tech Stack

| Component | Library | Purpose |
| :--- | :--- | :--- |
| **Graphics** | `turtle` | Drawing the bars and handling the animation loop. |
| **Logic** | `numpy` | Generating random datasets and handling array operations. |
| **Time** | `time` | Controlling the speed of the animation. |

---

## 💻 How to Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/Algorithm-Race.git](https://github.com/your-username/Algorithm-Race.git)
    cd Algorithm-Race
    ```

2.  **Install Dependencies**
    You only need NumPy (Turtle is built into Python).
    ```bash
    pip install numpy
    ```

3.  **Run the Visualizer**
    ```bash
    python main.py
    ```

---

## 🧠 Code Highlight: Visual Swapping

The core logic combines the standard Bubble Sort algorithm with a drawing function update. This allows us to see the "Swap" happening live.

```python
if data_array[j] > data_array[j + 1]:
    # 1. Swap the data in memory (NumPy)
    data_array[j], data_array[j + 1] = data_array[j + 1], data_array[j]

    # 2. Update the visuals immediately
    draw_bar(data_array)
    
    # 3. Pause slightly so the human eye can see it
    time.sleep(0.05)
```
🚀 Future Roadmap

[ ] Add Merge Sort and Quick Sort algorithms.

[ ] Add a Tkinter Control Panel to switch between algorithms.

[ ] Add sound effects for every swap!

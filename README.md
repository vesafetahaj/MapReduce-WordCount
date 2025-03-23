# 📝 MapReduce WordCount

A simple yet powerful implementation of the classic **Word Count** problem using the **MapReduce programming model** written in **Python**. This project illustrates how distributed computing principles can be applied to process large volumes of textual data.

## 📚 Description

The **WordCount** algorithm counts how many times each word appears in a given text file. This implementation simulates the MapReduce paradigm using Python scripts to represent the `Mapper`, `Reducer`, and the logic that brings them together, mimicking how Hadoop would process jobs in a distributed fashion.

The simulation is in three main phases of MapReduce:

1. **Map**: Process input data and emit key-value pairs.
2. **Shuffle & Sort**: Sort the key-value pairs by key.
3. **Reduce**: Aggregate values associated with each key.

---

## 🏗️ Architecture Overview

![image](https://github.com/user-attachments/assets/0f8f6b56-6a2f-4867-a20a-cd7c0a3b7bd7)

---

## 🧬 Detailed Design

![mapreduce design drawio](https://github.com/user-attachments/assets/9122b47f-6330-4a42-a3fe-805ea225db22)

1. mapper.py
Reads lines from standard input (stdin)
Splits each line into words
Emits output in the form: word 1

# Example line output: 
hello    1
world    1

2. PowerShell Pipeline
In the terminal, the pipeline does the following:
Get-Content ../data/input.txt | py mapper.py | Sort-Object | py reducer.py > final_output.txt

- Get-Content: Reads each line of the input file
- py mapper.py: Emits key-value pairs (word\t1)
- Sort-Object: Groups identical keys together, like Hadoop's shuffle/sort phase
- py reducer.py: Aggregates counts for each word

Output is redirected to final_output.txt

3. reducer.py
Reads sorted word\t1 lines
Sums counts for identical words
Emits final word\tcount line

---

## ⚙️ Prerequisites
- Python 3.7+
- Git (for cloning the repo)
- PyCharm IDE (optional but recommended)

You can install the necessary Python version via:
  sudo apt update
  sudo apt install python3

---

## 🚀 How to Run (PyCharm Terminal)
1. Clone the Repository
git clone https://github.com/vesafetahaj/MapReduce-WordCount.git
cd MapReduce-WordCount

2. Ensure your input file exists:
../data/input.txt
You can edit the file path if needed.

3. Run the MapReduce pipeline inside the PyCharm terminal:
Get-Content ../data/input.txt | py mapper.py | Sort-Object | py reducer.py > final_output.txt

4. Check results:
Get-Content final_output.txt

---

## 📂 Output Example

input.txt

hello world
hello again

final_output.txt

again    1
hello    2
world    1

---

## 🎯 Learning Goals

1. Understand the structure of a MapReduce pipeline
2. Practice basic stream processing in Python
3. Simulate real-world big data tools using simple components

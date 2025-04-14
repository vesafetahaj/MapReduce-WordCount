# 📝 MapReduce WordCount

A simple yet powerful implementation of the classic **Word Count** problem using the **MapReduce programming model** written in **Python**. This project illustrates how distributed computing principles can be applied to process large volumes of textual data.

---

## 📚 Description

The **WordCount** algorithm counts how many times each word appears in a given text file. This implementation simulates the MapReduce paradigm using Python scripts to represent the `Mapper`, `Reducer`, and the logic that brings them together, mimicking how Hadoop would process jobs in a distributed fashion.

The simulation is in three main phases of MapReduce:

1. **Map**: Process input data and emit key-value pairs.
2. **Shuffle & Sort**: Sort the key-value pairs by key.
3. **Reduce**: Aggregate values associated with each key.


## 🏗️ Architecture Overview

![image](https://github.com/user-attachments/assets/0f8f6b56-6a2f-4867-a20a-cd7c0a3b7bd7)

---

## 🧬 Detailed Design

![mapreduce design drawio](https://github.com/user-attachments/assets/9122b47f-6330-4a42-a3fe-805ea225db22)

This diagram illustrates how the MapReduce WordCount process works:

**Input Split:** Each line of the input text is sent to a separate mapper instance.

**Map Phase:** Mappers emit key-value pairs like word → 1 for every word.

**Shuffle & Sort:** Key-value pairs are grouped and sorted by word.

**Reduce Phase:** Reducers sum the counts for each word.

**Final Output:** A list of words and their total occurrences is produced.

### With combiner for optimization:
![image](https://github.com/user-attachments/assets/270d7f19-c2ee-4806-a6f7-c39d7a211e12)


---

## 🧮 Complexity Analysis

#### ⏱️ Time Complexity

| **Phase**          | **Operation**                         | **Time Complexity** |
|--------------------|----------------------------------------|---------------------|
| **Map**            | Tokenize and emit `word → 1` pairs     | `O(N)`              |
| **Shuffle & Sort** | Group and sort intermediate pairs      | `O(N log N)`        |
| **Reduce**         | Aggregate values for each word         | `O(N)`              |
| **Total**          | *(dominated by shuffle/sort phase)*    | `O(N log N)`        |

- `N` = total number of words  
- `M` = number of unique words

---

#### 💾 Space Complexity

| **Phase**          | **Memory Usage**                          | **Space Complexity** |
|--------------------|-------------------------------------------|----------------------|
| **Map Output**     | Store all intermediate `word → 1` pairs   | `O(N)`               |
| **Shuffle Buffer** | Hold grouped data before reducing         | `O(N)`               |
| **Reduce Output**  | Store final count for each unique word    | `O(M)`               |
| **Total**          |                                           | `O(N + M)`           |

---

## ⚙️ Prerequisites
- Python 3.7+
- Git (for cloning the repo)
- PyCharm IDE (optional but recommended)

You can install the necessary Python version via:
```bash
sudo apt update
sudo apt install python3
```

To install GUI dependencies:
```bash
pip install -r requirements.txt
```
---

## 🖥️ GUI Mode

The project includes a beautiful, interactive **Streamlit-based GUI** for a user-friendly experience:

### ✨ Features:
- **📥 Input Page**: Upload `.txt` files or manually input text.
- **📋 Word Table Page**:
  - Live search functionality
  - Styled and scrollable results table
- **📊 Charts Page**:
  - Bar chart, Pie chart, Horizontal bar chart
  - Execution time analysis chart
- **📤 Download Page**:
  - Export results as CSV
  - Preview top 10 words before download

### 🎨 Interface Design:
- Dark burgundy themed UI with smooth hover effects 
- Navigation with icon-labeled items
- Responsive layout designed with user experience in mind


---

## 🚀 How to Run

### ▶️ CLI Mode (via PyCharm terminal or PowerShell)
```bash
git clone https://github.com/vesafetahaj/MapReduce-WordCount.git
cd MapReduce-WordCount
Get-Content data/input.txt | py src/mapper.py | Sort-Object | py src/reducer.py > final_output.txt
```

### ▶️ GUI Mode
```bash
cd gui
streamlit run gui_app.py
```

---

## 📂 Output Example

**input.txt**
```
hello world
hello again
```

**final_output.txt**
```
again    1
hello    2
world    1
```

---

## 🎯 Learning Goals

1. Understand the structure of a MapReduce pipeline
2. Practice basic stream processing in Python
3. Build a modern frontend to visualize distributed data logic
4. Learn to integrate CLI and GUI views of the same data pipeline

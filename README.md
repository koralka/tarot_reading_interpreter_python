# Tarot Reading Interpreter (Python)
## 📌 Project Description
This project is a **simple Python program** designed to help interpret tarot readings by summarising card meanings based on their **position in a spread**.

It was created as a **personal coding exercise** to practice Python fundamentals while incorporating an interest in tarot.

### ✨ What does it do?  
🔹 **Acts as a tarot reference tool** by displaying structured card meanings within a spread.   
🔹 **Does not "interpret" your reading** but helps provide insight based on traditional tarot meanings.   
🔹 **Works best with a physical tarot deck**, but includes an **optional random card selection feature** for fun.   


## 🃏 How It Works
1. **Choose a tarot spread** (Celtic Cross, Three-Card Spread, or Five-Card Spread).
2. **Enter the names of the cards you drew**, or type "random" if you want the program to select a card for you.
3. The program **retrieves the meanings** of the cards based on:
  - Their **general interpretation** (upright & reversed).
  - Their **placement in the spread** (e.g., "The Present," "Hopes & Fears").
4. You can **save the reading to a file** for future reference.


## 📂 Files in This Repository
This repository contains the following files:
- _tarot_reader.py_ – The main Python script that runs the tarot reading interpreter.
- _cards.csv_ – A dataset containing:
  - Tarot card **names**
  - **Element** (e.g., Fire, Water) 🔥💨💧
  - **Arcana type** (Major or Minor Arcana)
  - **Upright & reversed meanings**

📌 **Note**: The script **relies on _cards.csv_**, so make sure both files are in the **same folder** when running the program.


## 🎯 Project Goals & Learning Objectives
This project was developed to practice:   
✅ **Handling user input** interactively   
✅ **Reading and processing CSV files** in Python 📂   
✅ **Using dictionaries** to structure and store data 📊   
✅ **Implementing basic string matching** for flexible user input   
✅ **Writing outputs to a text file** for saving readings ✍️   
✅ **Improving terminal output formatting** for better readability   

While simple, this project serves as **a foundation** for further improvements.


## 📜 Notes & Acknowledgements
- **This project is just for fun** and is not intended as a serious divination tool.
- The **random card selection feature is optional** — it was primarily added as a way to test my Python skills.
- Ideally, users should **have access to a tarot deck** for a more meaningful reading experience.

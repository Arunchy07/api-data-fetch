# 🧠 API Data Fetch Task (Python)

This project demonstrates how to **fetch and display user data** from a public API using Python.  
It covers working with **GET APIs**, **JSON data**, **loops**, and **error handling** using the `requests` library.

---

## 🚀 Task Description

### Objective
Fetch data from the API endpoint and display selected user details in a readable format.

**API Endpoint:**
https://jsonplaceholder.typicode.com/users
---

## 📋 Features

✅ Fetches user data via HTTP GET  
✅ Displays the following fields for each user:
- Name  
- Username  
- Email  
- City (from `address.city`)  

✅ Handles API errors (e.g., failed response or empty list)  
✅ (Bonus) Displays users whose city name starts with the letter **‘S’**

---

## 🧑‍💻 Example Output
User 1:
Name: Leanne Graham
Username: Bret
Email: Sincere@april.biz

City: Gwenborough
User 2:
Name: Ervin Howell
Username: Antonette
Email: Shanna@melissa.tv

City: Wisokyburgh

Users from cities starting with 'S':

Clementine Bauch (South Elvis)


---

## ⚙️ Requirements

### Software
- Python **3.7+**
- Internet connection

### Python Package
| Library | Purpose | Install Command |
|----------|----------|----------------|
| `requests` | For API calls | `pip install requests` |

You can also install all dependencies at once:
```bash
pip install -r requirements.txt


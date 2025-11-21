## ForneceJuntos

A **ForneceJuntos** web application developed to facilitate the search and registration of beverage suppliers. The platform allows users to search for suppliers based on various criteria, such as Corporate Tax ID (CNPJ), Company Name (Razão Social), City, and Beverage Type.

---

## ✨ Features

The application provides the following core functionalities:

* **🔍 Search Suppliers**: Users can search for registered suppliers using filters like **CNPJ**, **Company Name**, **City**, and **Beverage Type**.
* **➕ Add Supplier**: Allows the secure registration of new suppliers into the database.
* **🗑️ Delete Supplier**: Provides the functionality to definitively exclude a supplier from the platform.
* **📄 Supplier Listing**: Displays a complete list of registered suppliers, summarizing key information (CNPJ, Company Name, City, and Beverage Category).
* **ℹ️ Supplier Details**: Presents a detailed view of all information associated with a selected supplier.

---

## 💻 Technologies

The project is built using a robust and reliable stack:

| Component | Technology | Version / Description |
| :--- | :--- | :--- |
| **Frontend** | HTML, CSS, JavaScript | Standard web technologies for the user interface. |
| **Backend** | Python, Django | Python framework for the server-side logic. |
| **Database** | MySQL | Relational database management system for data persistence. |

---

## 🚀 Getting Started

Follow these steps to set up and run the **ForneceJuntos** application locally.

### Prerequisites

Ensure you have the following installed on your machine:

* **Python** (Version 3.8)
* **Django** (Version 3.2)
* **MySQL** instance configured (or a similar setup).

### Step-by-Step Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/RenzoDTavares/ForneceJuntos.git
    cd fornecejuntos
    ```

2.  **Setup Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Database Configuration:**
    * Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Run the application:**

    ```bash
    python manage.py runserver
    ```

The application should now be accessible at `http://127.0.0.1:8000/`.

---

## 📸 Screenshots

| Screen | Description |
| :--- | :--- |
| **Initial Screen** | The main page showing the supplier listing and search options. |
| **Registration Screen** | Form to register a new supplier with all required fields. |
| **Details Screen** | View showing comprehensive supplier details, including action buttons. |
| **Editing Screen** | Form pre-populated with existing supplier data for modification. |

### Images

* **Initial Screen:**
  ![Initial Screen](https://github.com/user-attachments/assets/1f9712ad-c33e-4cf6-a3e0-60c3e48fb15a)

* **Registration Screen:**
  ![Registration Screen](https://github.com/user-attachments/assets/eb85858f-61db-48fa-8cbd-5d3d39ac9424)

* **Details Screen:**
  ![Details Screen](https://github.com/user-attachments/assets/d024c560-93ee-4755-8af1-a118c4cffbc2)

* **Editing Screen:**
  ![Editing Screen](https://github.com/user-attachments/assets/1c078980-4a95-4e77-b5cd-bb9f09a296b4)

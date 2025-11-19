
#  Vegetable & Fruit Prices Dashboard

An interactive **Streamlit dashboard** for visualizing historical **vegetable and fruit prices** across Indian markets.

This dashboard allows users to filter items, choose date ranges, explore price trends, compare average prices, and view summary statistics.

---

##  Features

###  Interactive Filters
- Select multiple vegetable/fruit items  
- Choose a custom date range  
- Automatically updates all charts and metrics  

###  Visualizations
- **Line Chart** – Shows price trends over time  
- **Bar Chart** – Compares average prices of selected items  
- **Scrollable Data Table**  
- **Summary Metrics** – Min, Max & Average price  

---

##  Technologies Used

- Python  
- Streamlit  
- Pandas  
- Matplotlib  
- CSV Dataset (Veg_fruits_price_India.csv)

---

##  Project Structure

```
vegetable_fruit_dashboard/
│── app.py                     # Main Streamlit file
│── Veg_fruits_price_India.csv # Dataset
│── README.md                  # Documentation
```

---

##  How to Run the Project

### 1 Install dependencies

```bash
pip install streamlit pandas matplotlib
```

### 2 Run the Streamlit app

```bash
streamlit run app.py
```

---

##  Dataset Description

The dataset contains:

- Item Name  
- Market  
- Date  
- Price  

Ensure that **Veg_fruits_price_India.csv** is placed in the same directory as `app.py`.

---

##  Dashboard Preview  
*(You can add screenshots here later.)*

---

##  Contributing

Contributions, issues, and feature requests are welcome!

---

##  License

Distributed under the MIT License.


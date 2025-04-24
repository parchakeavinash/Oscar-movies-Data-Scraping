# 🎬 Oscar-Winning Films Scraper (Selenium + Python)

This project is a **web scraping script** built using **Selenium** to automatically extract movie data (Title, Nominations, and Awards) from [ScrapeThisSite](https://www.scrapethissite.com/pages/ajax-javascript/).

It demonstrates best practices in:
- Dynamic content scraping
- Element wait strategies
- Modular Python scripting

---

## 📌 What It Does

✅ Clicks each year (2010–2015) from a dynamic list  
✅ Waits smartly using `WebDriverWait` (no more blind `time.sleep()`)  
✅ Extracts movie names, number of nominations, and awards  
✅ Saves the data into a CSV file  
✅ Handles errors gracefully using `try/except`  

---

## 🧠 Tech Stack

- **Python 3.7+**
- **Selenium**
- **webdriver-manager** (auto-downloads ChromeDriver)
- **CSV** (for output)

---

## 📁 Output Example

A sample of `movie_data.csv`:

| Movie Name | Nominations | Awards |
|------------|-------------|--------|
| The Artist | 10          | 5      |
| Hugo       | 11          | 5      |
| ...        | ...         | ...    |

---

## ⚙️ How to Run

1. **Clone this repo:**
```bash
git clone https://github.com/your-username/oscar-scraper.git
cd oscar-scraper

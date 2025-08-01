# ☕ KalcerC – System Loyalty Point Coffee Shop

KalcerC is a modern, culture-driven loyalty point system built for a coffee shop environment.  
It helps track, manage, and reward customer loyalty to enhance engagement and drive repeat visits.

---

## 📌 Features

- Earn and redeem loyalty points for every purchase
- Customer dashboard to view points and transaction history
- Admin panel to manage rewards and customers
- Modern minimalist UI/UX with a Gen Z aesthetic
- Secure authentication and session management
- API-first design for potential mobile app integration

---

## ⚙️ Tech Stack

- **Frontend:** Html, Tailwind CSS
- **Backend:** Django
- **Database:** sqlite3 
- **Other:** -

---

## 🚀 Getting Started

### Prerequisites

- Python >= 3.12
- sqlite

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/kalcerc-loyalty-system.git
cd kalcerc-loyalty-system

# Install environment (if using conda)
conda env create -f environment.yml

# Run Database Migration
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
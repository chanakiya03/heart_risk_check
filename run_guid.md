# Running the Heart Project

Follow these steps to get the application up and running on a Windows machine.

## 1. Prepare the Python environment (backend)

Open PowerShell and cd to the backend folder:

```powershell
PS> cd D:\projects\heart\backend
```

1. **Create & activate a virtualenv**

   ```powershell
   PS> python -m venv .venv
   PS> .\.venv\Scripts\Activate.ps1
   ```

2. **Install Python dependencies**

   ```powershell
   (.venv) PS> pip install -r requirements.txt
   ```

## 2. Initialize the Django project

1. **Apply migrations / create database**

   ```powershell
   (.venv) PS> python manage.py migrate
   ```

2. (Optional) **Create an admin user**

   ```powershell
   (.venv) PS> python manage.py createsuperuser
   ```

## 3. (Optional) Train / generate the ML model

```powershell
(.venv) PS> python api\ml\train.py
```

Artifacts will be written to `backend/api/ml/` (`model.pkl`, `scaler.pkl`, `features.pkl`).

## 4. Try a prediction (smoke test)

```powershell
(.venv) PS> python test_prediction.py
```

## 5. Run the API server

```powershell
(.venv) PS> python manage.py runserver
```

## 6. Frontend (React)

Open a new terminal, then:

```powershell
PS> cd D:\projects\heart\frontend
PS> npm install
PS> npm start
```
  http://localhost:3001
---

> 🔁 Make sure backend is running before using the frontend.
> Deactivate the Python venv with `deactivate` when finished.
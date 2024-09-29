
# LuTools

**LuTools** is a collection of essential online tools designed to enhance your daily productivity. Hosted under [lutools.luca137.com](https://lutools.luca137.com), LuTools offers accessible and reliable utilities that you can use anytime, anywhere.

## Table of Contents

- [LuTools](#lutools)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technology Stack](#technology-stack)
  - [Folder Structure](#folder-structure)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Setup Backend](#setup-backend)
    - [Setup Frontend](#setup-frontend)
  - [Usage](#usage)
    - [Running Locally](#running-locally)
    - [Accessing the Tools](#accessing-the-tools)
  - [Deployment](#deployment)
    - [Frontend Deployment on Vercel](#frontend-deployment-on-vercel)
    - [Backend Deployment on Render.com](#backend-deployment-on-rendercom)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **Text to Markdown Converter:** Easily convert plain text to Markdown format.
- **Email Sender:** Send customized emails directly from the platform.
- **Additional Tools:** More utilities to be added regularly based on user feedback.

## Technology Stack

- **Frontend:**
  - [SvelteKit](https://kit.svelte.dev/)
  - [Tailwind CSS](https://tailwindcss.com/)
  - [Vite](https://vitejs.dev/)
  - Hosted on [Vercel](https://vercel.com/)

- **Backend:**
  - [Python](https://www.python.org/)
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [Supabase](https://supabase.io/) (for database management)
  - Hosted on [Render.com](https://render.com/)

- **DevOps:**
  - [GitHub](https://github.com/) for version control
  - [GitHub Actions](https://github.com/features/actions) for CI/CD
  - Custom logging with Python’s `logging` module

## Folder Structure

```bash
LUTOOLS
├── backend_env
│   ├── __pycache__
│   ├── Include
│   ├── Lib
│   ├── Scripts
│   └── utils
│       ├── logger_config.py
│       ├── env
│       ├── .gitignore
│       ├── main.py
│       ├── pyvenv.cfg
│       └── requirements.txt
└── frontend
    ├── .github
    ├── svelte-kit
    ├── node_modules
    ├── src
    ├── static
    ├── .gitignore
    ├── .npmrc
    ├── package-lock.json
    ├── package.json
    ├── README.md
    ├── svelte.config.js
    └── vite.config.js
```

- **backend_env:** Contains the Python backend, including virtual environment and utility scripts.
- **frontend:** Houses the SvelteKit frontend application with all necessary configurations and dependencies.

## Installation

### Prerequisites

- **Node.js** (v14 or later)
- **Python** (v3.8 or later)
- **Git**

### Clone the Repository

```bash
git clone https://github.com/lucianoaf8/lutools.git
cd lutools
```

### Setup Backend

1. **Navigate to Backend Directory:**

    ```bash
    cd backend_env
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv backend_env
    ```

3. **Activate the Virtual Environment:**

    - **Windows:**

        ```bash
        backend_env\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source backend_env/bin/activate
        ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Environment Variables:**

    Create a `.env` file in the `backend_env` directory with the following variables:

    ```env
    SECRET_KEY=your_secret_key
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key
    ```

### Setup Frontend

1. **Navigate to Frontend Directory:**

    ```bash
    cd ../frontend
    ```

2. **Install Dependencies:**

    ```bash
    npm install
    ```

3. **Configure Environment Variables:**

    Create a `.env` file in the `frontend` directory with the following variable:

    ```env
    VITE_API_BASE_URL=https://your-backend-url.com
    ```

## Usage

### Running Locally

1. **Start the Backend Server:**

    ```bash
    cd backend_env
    uvicorn main:app --reload
    ```

    The backend will be accessible at `http://localhost:8000`.

2. **Start the Frontend Development Server:**

    ```bash
    cd ../frontend
    npm run dev -- --open
    ```

    The frontend will open in your default browser at `http://localhost:5173`.

### Accessing the Tools

Once both servers are running, navigate to `http://localhost:5173` to access LuTools. Use the provided interface to interact with the available tools such as the Text to Markdown Converter and Email Sender.

## Deployment

### Frontend Deployment on Vercel

1. **Sign Up/Login to Vercel:**
   - Visit [Vercel](https://vercel.com/) and create an account or log in.

2. **Import Project:**
   - Connect your GitHub account.
   - Import the `frontend` directory from the `lutools` repository.

3. **Configure Settings:**
   - Set the framework preset to **SvelteKit**.
   - Add environment variables (`VITE_API_BASE_URL`) in the Vercel dashboard.

4. **Deploy:**
   - Vercel will automatically build and deploy your frontend.
   - Configure the custom domain `lutools.luca137.com` through Vercel’s domain settings.

### Backend Deployment on Render.com

1. **Sign Up/Login to Render.com:**
   - Visit [Render](https://render.com/) and create an account or log in.

2. **Create a New Web Service:**
   - Select **New** > **Web Service**.
   - Connect your GitHub repository and select the `backend_env` directory.

3. **Configure Build and Start Commands:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`

4. **Set Environment Variables:**
   - Add `SECRET_KEY`, `SUPABASE_URL`, and `SUPABASE_KEY` in Render’s environment settings.

5. **Deploy:**
   - Render will build and deploy your backend application.
   - Note the backend URL provided by Render and update the frontend’s `VITE_API_BASE_URL` accordingly.

## Contributing

Contributions are welcome! Please follow these steps to contribute to LuTools:

1. **Fork the Repository:**

    Click the "Fork" button at the top right of the repository page on GitHub.

2. **Clone Your Fork:**

    ```bash
    git clone https://github.com/your-username/lutools.git
    cd lutools
    ```

3. **Create a New Branch:**

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Your Changes:**

    Implement your feature or bug fix.

5. **Commit Your Changes:**

    ```bash
    git add .
    git commit -m "Add your descriptive commit message"
    ```

6. **Push to Your Fork:**

    ```bash
    git push origin feature/your-feature-name
    ```

7. **Create a Pull Request:**

    Go to the original repository on GitHub and click "Compare & pull request."

## License

This project is licensed under the [MIT License](LICENSE).

---

**Notes:**

- **Environment Variables:** Ensure that all sensitive information is stored securely and not exposed in the repository. Use `.env` files locally and configure environment variables through your hosting provider for production.
  
- **Logging:** The backend includes a custom logging setup to monitor application performance and capture errors. Logs are stored in the `logs/` directory, organized by date.

- **Testing:** Regularly test both frontend and backend functionalities to ensure reliability and performance.

- **Documentation:** Additional documentation can be added as the project evolves, including API specifications, detailed usage guides for each tool, and developer notes.

Feel free to reach out or open an issue on the GitHub repository if you encounter any problems or have suggestions for improvements!

---

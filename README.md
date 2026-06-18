# PROJECT-MAHABHARAT

A wisdom-sharing web application inspired by the Mahabharata, leveraging AI-powered insights and traditional Hindu philosophy.

## Overview

**PROJECT-MAHABHARAT** is a Flask-based web application that combines the timeless wisdom of the Mahabharata with modern AI technology. The platform provides users with motivational advice, life lessons, and Sanskrit shlokas (verses) based on characters and teachings from the ancient Hindu epic.

## Features

- 🔐 **User Authentication**: Secure login and signup system
- 💬 **AI-Powered Wisdom**: Get personalized advice using Google Gemini AI, inspired by Mahabharata characters
- 📚 **Pravachanas**: Browse and explore collected teachings and wisdom
- 📊 **Dashboard**: Personalized user dashboard with tracked wisdom
- 🎯 **Feeling Manager**: Track and manage emotional states with wisdom recommendations
- 👨‍💼 **Admin Panel**: Manage users, pravachanas, and platform content
- 🎨 **Responsive UI**: Modern, intuitive user interface

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MongoDB Atlas
- **AI Integration**: Google Generative AI (Gemini)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Session-based with secure password handling

## Prerequisites

- Python 3.8+
- MongoDB Atlas account
- Google Gemini API key
- Node.js (for frontend dependencies)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PROJECT-MAHABHARAT
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   FLASK_SECRET_KEY=your-secret-key-here
   MONGO_URI=your-mongodb-atlas-uri
   GEMINI_API_KEY=your-gemini-api-key
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

## Project Structure

```
PROJECT-MAHABHARAT/
├── app.py                 # Main Flask application
├── gemini_handler.py      # AI wisdom generation handler
├── auth/                  # Authentication utilities
├── routes/                # Flask blueprints
│   ├── login.py
│   ├── dashboard.py
│   ├── wisdom.py
│   └── admin_routes.py
├── templates/             # HTML templates
├── static/                # CSS, JavaScript, images
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Usage

### For Users
1. Sign up for an account
2. Log in to your dashboard
3. Explore wisdom from the Mahabharata
4. Use the feeling manager to get personalized advice
5. Track your favorite teachings

### For Administrators
1. Access the admin panel at `/admin`
2. Manage users and content
3. Add new pravachanas (teachings)
4. Monitor platform activity

## Key Endpoints

- `/` - Home page
- `/signup` - User registration
- `/login` - User login
- `/dashboard` - User dashboard
- `/wisdom` - Wisdom exploration
- `/admin` - Admin panel

## AI Features

The application uses Google's Gemini 3 Flash Preview model to generate AI-based wisdom that:
- Provides motivational advice using Mahabharata character examples
- Delivers life lessons inspired by the epic
- Generates relevant Sanskrit shlokas

## Environment Variables

| Variable | Description |
|----------|-------------|
| `FLASK_SECRET_KEY` | Secret key for Flask session management |
| `MONGO_URI` | MongoDB Atlas connection string |
| `GEMINI_API_KEY` | Google Generative AI API key |

## Deployment

The application is configured for deployment on Render.yaml. See `render.yaml` for deployment configuration.

## Security

- User passwords are securely hashed
- Session-based authentication
- Environment variables for sensitive data
- CORS and security headers configured

## Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All features are tested
- Documentation is updated

## License

[Add your license information here]

## Author

by thanush

## Support

For issues, questions, or suggestions, please create an issue in the repository.

---

**May the wisdom of the Mahabharata guide your path!**

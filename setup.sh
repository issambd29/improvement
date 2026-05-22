#!/bin/bash
# الارتقاء — Setup Script for macOS / Linux

echo "╔══════════════════════════════════════╗"
echo "║         الارتقاء — Setup             ║"
echo "║   Islamic Self-Improvement OS        ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌  Python 3 is not installed. Please install from https://python.org"
    exit 1
fi
echo "✓ Python: $(python3 --version)"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt -q

# Run migrations
echo "Setting up database..."
python manage.py migrate --run-syncdb

# Create superuser prompt
echo ""
echo "════════════════════════════════════════"
echo "Do you want to create an admin account? (y/n)"
read -r CREATE_ADMIN
if [[ "$CREATE_ADMIN" == "y" || "$CREATE_ADMIN" == "Y" ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "════════════════════════════════════════"
echo "✅  Setup complete!"
echo ""
echo "To start the app, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then open http://127.0.0.1:8000 in your browser."
echo "════════════════════════════════════════"

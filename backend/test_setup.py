print("Hello, League Analytics Hub!")
print("Testing if Python works...")

# Test if packages are installed
try:
    import flask
    print("✓ Flask is installed")
except ImportError:
    print("✗ Flask is NOT installed")

try:
    import requests
    print("✓ Requests is installed")
except ImportError:
    print("✗ Requests is NOT installed")

try:
    import pandas
    print("✓ Pandas is installed")
except ImportError:
    print("✗ Pandas is NOT installed")

print("\nSetup test complete!")
# Ensure script execution policy is set to RemoteSigned or Unrestricted
# Run this with admin privileges if needed:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Write-Host "Starting installation..." -ForegroundColor Green

# Update Chocolatey and install required dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
if (-Not (Get-Command "choco" -ErrorAction SilentlyContinue)) {
    Write-Host "Chocolatey is not installed. Installing Chocolatey..." -ForegroundColor Cyan
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# Install Python if not already installed
if (-Not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    choco install python -y
}

# Install emoji-compatible fonts (Segoe UI Emoji comes pre-installed on most modern Windows systems)
Write-Host "Ensuring emoji-compatible fonts are installed..." -ForegroundColor Yellow
# Check for Segoe UI Emoji font
$fontInstalled = Get-ChildItem -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" | Where-Object { $_.PSChildName -like "*Segoe UI Emoji*" }
if (-Not $fontInstalled) {
    Write-Host "Segoe UI Emoji font not found. Please ensure your system has the required fonts for emoji rendering." -ForegroundColor Red
}

# Set up Python virtual environment
Write-Host "Setting up Python virtual environment..." -ForegroundColor Yellow
python -m venv oco
Set-Location oco
.\Scripts\Activate.ps1

# Install required Python packages
Write-Host "Installing Python packages..." -ForegroundColor Yellow
pip install -r ../requirements.txt

# Notify user of completion
Write-Host "Installation complete! Your environment is ready." -ForegroundColor Green

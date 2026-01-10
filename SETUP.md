# Auto-Updating GitHub Profile Setup

Your GitHub profile now auto-updates every 6 hours with real-time data!

## What Auto-Updates

✅ **Time-Based Greeting**: "Good morning/afternoon/evening" based on IST time  
✅ **Weather**: Current temperature and conditions for Dehradun, India  
✅ **GitHub Contribution Graph**: Real-time from ghchart.rshah.org  
✅ **Streak Stats**: Automatically pulled from your GitHub activity

## How It Works

### GitHub Actions Workflow
The `.github/workflows/update-readme.yml` file runs automatically:
- **Schedule**: Every 6 hours
- **Triggers**: Also runs on push to main or manual dispatch
- **Updates**: Fetches weather, time, and regenerates SVG

### APIs Used
1. **GitHub REST API**: For user stats (built-in, no key needed)
2. **OpenWeatherMap API**: For Dehradun weather (requires free API key)
3. **ghchart.rshah.org**: For contribution graph (no key needed)

## Setup Instructions

### 1. Get OpenWeatherMap API Key (Free)
1. Go to https://openweathermap.org/api
2. Sign up for a free account
3. Get your API key from the dashboard

### 2. Add Secret to GitHub
1. Go to your repository: https://github.com/phnxsahil/phnxsahil
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `OPENWEATHER_API_KEY`
5. Value: Paste your API key
6. Click **Add secret**

### 3. Enable GitHub Actions
1. Go to **Actions** tab in your repository
2. If prompted, click **I understand my workflows, go ahead and enable them**
3. The workflow will run automatically every 6 hours

### 4. Manual Trigger (Optional)
To update immediately:
1. Go to **Actions** tab
2. Click **Update README Stats** workflow
3. Click **Run workflow** → **Run workflow**

## Current Features

**Dynamic Content:**
- Greeting changes based on time (morning/afternoon/evening)
- Weather shows current temp and emoji (☀️/☁️/🌧️/❄️)
- Contribution graph updates in real-time
- All stats refresh automatically

**Professional Design:**
- Clean, minimal chat bubble interface
- 1.8-2.2s typing indicator timing
- Smooth fade animations
- Perfect dark/light mode support

## Troubleshooting

**Weather not updating?**
- Make sure you added the `OPENWEATHER_API_KEY` secret
- Check Actions tab for any errors

**Workflow not running?**
- Ensure GitHub Actions are enabled in Settings
- Check the Actions tab for workflow runs

**Want to change update frequency?**
- Edit `.github/workflows/update-readme.yml`
- Change the cron schedule (currently `0 */6 * * *` = every 6 hours)

---

**Note**: The first run might take a few minutes. Check the Actions tab to see the workflow in progress!

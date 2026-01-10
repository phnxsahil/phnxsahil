# Isometric GitHub Contributions

## The Real Solution

Jason Long's isometric 3D building blocks come from his **isometric-contributions** browser extension:
- GitHub: https://github.com/jasonlong/isometric-contributions
- It's a browser extension that transforms the GitHub contribution graph in real-time
- Works by injecting JavaScript into GitHub pages

## Options for Your Profile

### Option 1: Use the Browser Extension (Recommended for Personal Use)
1. Install: https://github.com/jasonlong/isometric-contributions
2. View your profile with the extension enabled
3. Take a screenshot and embed it as a static image

### Option 2: GitHub Skyline (Official 3D Model)
- Visit: https://skyline.github.com/phnxsahil/2025
- Downloads a 3D STL model of your contributions
- Can render to PNG and embed

### Option 3: Custom Python Script (What I Created)
I've created `generate_isometric.py` that generates isometric SVG:
- Run: `python generate_isometric.py`
- Generates `isometric-contributions.svg`
- Can be embedded in your README

### Option 4: Use Existing Services
Currently using:
- **github-readme-activity-graph**: Colorful contribution graph
- **github-readme-streak-stats**: Real-time streak data

## Current Implementation

Your profile uses real-time GitHub API services that auto-update:
- ✅ Colorful contribution activity graph
- ✅ Streak statistics
- ✅ Auto-updates every 6 hours via GitHub Actions

The isometric effect is beautiful but requires either:
1. A browser extension (client-side only)
2. Custom rendering script (needs to run periodically)
3. Static screenshot (doesn't auto-update)

**Recommendation**: The current colorful graphs with real-time data are more practical and professional than static isometric views.

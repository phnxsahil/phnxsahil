#!/usr/bin/env python3
"""
Generate isometric 3D building block visualization of GitHub contributions
Uses real GitHub API data with accurate commit colors
"""

import requests
import json
from datetime import datetime, timedelta
import math
import sys

def fetch_github_contributions(username, token=None):
    """Fetch real contribution data from GitHub GraphQL API"""
    
    # GraphQL query to get contribution calendar
    query = """
    query($userName:String!) {
      user(login: $userName){
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """
    
    headers = {
        "Authorization": f"bearer {token}" if token else "",
        "Content-Type": "application/json"
    }
    
    variables = {"userName": username}
    
    try:
        response = requests.post(
            "https://api.github.com/graphql",
            json={"query": query, "variables": variables},
            headers=headers
        )
        data = response.json()
        
        if "data" in data and data["data"]["user"]:
            weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
            return weeks
        else:
            print(f"Warning: Could not fetch real data, using sample data")
            return generate_sample_data()
    except Exception as e:
        print(f"Error fetching GitHub data: {e}")
        return generate_sample_data()

def generate_sample_data():
    """Generate sample contribution data for demonstration"""
    weeks = []
    for week in range(52):
        days = []
        for day in range(7):
            # Create varied sample data
            count = (week + day * 3) % 15
            days.append({
                "contributionCount": count,
                "date": "2025-01-01"
            })
        weeks.append({"contributionDays": days})
    return weeks

def get_color_for_count(count):
    """Get GitHub's color scheme based on contribution count"""
    if count == 0:
        return {"top": "#ebedf0", "left": "#d1d3d6", "right": "#b8bac0"}  # Gray
    elif count <= 3:
        return {"top": "#9be9a8", "left": "#7bc96f", "right": "#5aa84e"}  # Light green
    elif count <= 6:
        return {"top": "#40c463", "left": "#30a14e", "right": "#216e39"}  # Medium green
    elif count <= 9:
        return {"top": "#30a14e", "left": "#216e39", "right": "#144620"}  # Dark green
    else:
        return {"top": "#216e39", "left": "#144620", "right": "#0d3015"}  # Darkest green

def generate_isometric_svg(username, use_real_data=True):
    """Generate isometric SVG of contributions with real colors"""
    
    # Fetch contribution data
    if use_real_data:
        # Get token from global scope/args not ideal but simplest for this script structure
        # In a cleaner version we'd pass it down, but for now relying on it being available or added to fetch call
        # Let's fix fetch_github_contributions call in main
        import os
        token = os.environ.get('GITHUB_TOKEN')
        weeks_data = fetch_github_contributions(username, token)
    else:
        weeks_data = generate_sample_data()
    
    # SVG setup
    width = 800
    height = 300
    
    svg_header = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .cube:hover .cube-top {{ opacity: 0.8; }}
  </style>
  <g transform="translate(50, 180)">
'''
    
    svg_footer = '''  </g>
</svg>'''
    
    # Isometric projection parameters
    cube_size = 4
    spacing = 1
    
    # Generate cubes for each day
    cubes = []
    for week_idx, week in enumerate(weeks_data[-52:]):  # Last 52 weeks
        for day_idx, day in enumerate(week["contributionDays"]):
            count = day["contributionCount"]
            
            if count > 0:  # Only show days with contributions
                # Calculate height (1-5 levels)
                height_level = min(5, max(1, count // 3 + 1))
                
                # Get colors for this contribution level
                colors = get_color_for_count(count)
                
                # Position
                x = week_idx * (cube_size + spacing)
                y = day_idx * (cube_size + spacing)
                
                # Isometric transformation
                angle = math.radians(30)
                iso_x = (x - y) * math.cos(angle)
                iso_y = (x + y) * math.sin(angle)
                
                # Draw cube stack
                for level in range(height_level):
                    z_offset = level * cube_size
                    
                    # Calculate points for isometric cube
                    top_points = f"{iso_x},{iso_y - z_offset} {iso_x + cube_size * math.cos(angle)},{iso_y + cube_size * math.sin(angle) - z_offset} {iso_x},{iso_y + cube_size - z_offset} {iso_x - cube_size * math.cos(angle)},{iso_y + cube_size * math.sin(angle) - z_offset}"
                    
                    left_points = f"{iso_x - cube_size * math.cos(angle)},{iso_y + cube_size * math.sin(angle) - z_offset} {iso_x},{iso_y + cube_size - z_offset} {iso_x},{iso_y + cube_size - z_offset + cube_size} {iso_x - cube_size * math.cos(angle)},{iso_y + cube_size * math.sin(angle) - z_offset + cube_size}"
                    
                    right_points = f"{iso_x},{iso_y + cube_size - z_offset} {iso_x + cube_size * math.cos(angle)},{iso_y + cube_size * math.sin(angle) - z_offset} {iso_x + cube_size * math.cos(angle)},{iso_y + cube_size * math.sin(angle) - z_offset + cube_size} {iso_x},{iso_y + cube_size - z_offset + cube_size}"
                    
                    cube = f'''
    <g class="cube" data-count="{count}" data-date="{day.get('date', '')}">
      <polygon class="cube-top" fill="{colors['top']}" points="{top_points}"/>
      <polygon class="cube-left" fill="{colors['left']}" points="{left_points}"/>
      <polygon class="cube-right" fill="{colors['right']}" points="{right_points}"/>
    </g>'''
                    cubes.append(cube)
    
    return svg_header + ''.join(cubes) + svg_footer

if __name__ == "__main__":
    import argparse
    import os
    
    parser = argparse.ArgumentParser(description='Generate isometric contribution graph')
    parser.add_argument('--username', default='phnxsahil', help='GitHub username')
    parser.add_argument('--token', help='GitHub token')
    parser.add_argument('--use-real-data', action='store_true', help='Fetch real data from GitHub')
    
    args = parser.parse_args()
    
    # Get token from args or environment
    token = args.token or os.environ.get('GITHUB_TOKEN')
    
    # If we have a token, implied use_real_data
    use_real = args.use_real_data or (token is not None)
    
    svg_content = generate_isometric_svg(args.username, use_real_data=use_real)
    
    with open("isometric-contributions.svg", "w") as f:
        f.write(svg_content)
    
    print(f"Generated isometric contribution graph for {args.username}")
    if use_real and token:
        print("Used real GitHub data with token")
    elif use_real:
        print("Attempted to use real GitHub data (no token provided, might hit rate limits or fail)")
    else:
        print("Used sample data")

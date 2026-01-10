#!/usr/bin/env python3
"""
Generate isometric 3D building block visualization of GitHub contributions
Similar to Jason Long's isometric-contributions browser extension
"""

import requests
import json
from datetime import datetime, timedelta
import math

def fetch_github_contributions(username):
    """Fetch contribution data from GitHub API"""
    # This would use GitHub GraphQL API to get contribution calendar
    # For now, we'll use a simpler approach with the REST API
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    return response.json()

def generate_isometric_svg(username, year=2025):
    """Generate isometric SVG of contributions"""
    
    # SVG setup
    width = 800
    height = 400
    
    svg_header = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .cube-top {{ fill: #0079ff; }}
      .cube-left {{ fill: #005bb5; }}
      .cube-right {{ fill: #003d7a; }}
      .cube-top:hover {{ fill: #39a0ff; }}
    </style>
  </defs>
  <g transform="translate(100, 50)">
'''
    
    svg_footer = '''  </g>
</svg>'''
    
    # Isometric projection parameters
    cube_size = 8
    spacing = 2
    
    # Generate cubes for each day (simplified example)
    cubes = []
    for week in range(52):
        for day in range(7):
            # Height based on contribution count (0-4)
            height = (week + day) % 5  # Placeholder data
            
            if height > 0:
                x = week * (cube_size + spacing)
                y = day * (cube_size + spacing)
                
                # Isometric transformation
                iso_x = (x - y) * math.cos(math.radians(30))
                iso_y = (x + y) * math.sin(math.radians(30)) - (height * cube_size)
                
                # Draw cube (top, left, right faces)
                cube = f'''
    <g class="cube" data-count="{height}">
      <!-- Top face -->
      <polygon class="cube-top" points="
        {iso_x},{iso_y}
        {iso_x + cube_size * math.cos(math.radians(30))},{iso_y + cube_size * math.sin(math.radians(30))}
        {iso_x},{iso_y + cube_size}
        {iso_x - cube_size * math.cos(math.radians(30))},{iso_y + cube_size * math.sin(math.radians(30))}
      "/>
      <!-- Left face -->
      <polygon class="cube-left" points="
        {iso_x - cube_size * math.cos(math.radians(30))},{iso_y + cube_size * math.sin(math.radians(30))}
        {iso_x},{iso_y + cube_size}
        {iso_x},{iso_y + cube_size + height * cube_size}
        {iso_x - cube_size * math.cos(math.radians(30))},{iso_y + cube_size * math.sin(math.radians(30)) + height * cube_size}
      "/>
      <!-- Right face -->
      <polygon class="cube-right" points="
        {iso_x},{iso_y + cube_size}
        {iso_x + cube_size * math.cos(math.radians(30))},{iso_y + cube_size * math.sin(math.radians(30))}
        {iso_x + cube_size * math.cos(math.radians(30))},{iso_y + cube_size * math.sin(math.radians(30)) + height * cube_size}
        {iso_x},{iso_y + cube_size + height * cube_size}
      "/>
    </g>'''
                cubes.append(cube)
    
    return svg_header + ''.join(cubes) + svg_footer

if __name__ == "__main__":
    username = "phnxsahil"
    svg_content = generate_isometric_svg(username)
    
    with open("isometric-contributions.svg", "w") as f:
        f.write(svg_content)
    
    print(f"Generated isometric contribution graph for {username}")

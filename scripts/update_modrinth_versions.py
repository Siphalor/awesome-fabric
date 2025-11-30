#!/usr/bin/env python3
"""
Script to update Modrinth mod version tags in README.md
Extracts Modrinth links (🏰), fetches latest supported Minecraft version,
and updates/appends version tags (🔝 X.X.X)
"""

import re
import os
import sys
import requests
from typing import Optional, Tuple, List


def get_modrinth_project_id(url: str) -> Optional[str]:
    """Extract project ID/slug from Modrinth URL"""
    match = re.search(r'modrinth\.com/mod/([^)]+)', url)
    return match.group(1) if match else None


def get_latest_minecraft_version(project_id: str, api_token: Optional[str] = None) -> None | Tuple[str] | Tuple[str, str]:
    """Fetch latest supported Minecraft version from Modrinth API"""
    headers = {}
    if api_token:
        headers['Authorization'] = api_token

    try:
        # Get project info
        response = requests.get(
            f'https://api.modrinth.com/v2/project/{project_id}',
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        project_data = response.json()
        game_versions: List[str] = project_data['game_versions']
        latest_version = game_versions[-1]

        if is_snapshot_version(latest_version):
            # Find the latest non-snapshot version
            latest_non_snapshot: Optional[str] = None
            for version in reversed(game_versions):
                if not is_snapshot_version(version):
                    latest_non_snapshot = version
                    break

            if latest_non_snapshot is None:
                # No non-snapshot version found, return only snapshot
                return (latest_version,)
            else:
                return latest_non_snapshot, latest_version
        else:
            return (latest_version,)

    except requests.RequestException as e:
        print(f"Error fetching data for {project_id}: {e}", file=sys.stderr)
        return None


def is_snapshot_version(version: str) -> bool:
    return not re.match(r'^\d+\.\d+(?:\.\d+)?$', version)


def update_readme(readme_path: str, api_token: Optional[str] = None):
    """Update README.md with latest Minecraft versions"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    updated_lines = []

    # Pattern to match lines with Modrinth links
    modrinth_pattern = re.compile(r'(.*\[`🏰`\]\((https://modrinth\.com/mod/[^)]+)\))(\s+`🔝\s+[^`]+`)?(.*)$')

    for line in lines:
        match = modrinth_pattern.match(line)
        if match:
            prefix = match.group(1)  # Everything up to and including the Modrinth link
            modrinth_url = match.group(2)
            old_version_tag = match.group(3)  # Existing version tag if present
            suffix = match.group(4)  # Everything after version tag

            # Extract project ID
            project_id = get_modrinth_project_id(modrinth_url)
            if project_id:
                print(f"Fetching version for {project_id}...", file=sys.stderr)
                versions = get_latest_minecraft_version(project_id, api_token)

                if versions:
                    # Format version tag based on number of versions returned
                    if len(versions) == 2:
                        # Latest non-snapshot and latest snapshot
                        version_text = f"{versions[0]} / {versions[1]}"
                    else:
                        # Only one version (either latest non-snapshot or only snapshots available)
                        version_text = versions[0]

                    new_version_tag = f" `🔝 {version_text}`"
                    updated_lines.append(f"{prefix}{new_version_tag}{suffix}")

                    print(f"  → Updated to {version_text}", file=sys.stderr)
                else:
                    updated_lines.append(line)
                    print(f"  → Could not fetch version", file=sys.stderr)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)

    # Write updated content
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))

    print("\nREADME.md updated successfully!", file=sys.stderr)


def main(readme_path: str):
    api_token = os.environ.get('MODRINTH_API_TOKEN')

    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found", file=sys.stderr)
        sys.exit(1)

    update_readme(readme_path, api_token)


if __name__ == '__main__':
    main(readme_path=sys.argv[1] if len(sys.argv) >= 2 else 'README.md')

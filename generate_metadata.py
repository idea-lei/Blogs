import os
import json
import subprocess
from datetime import datetime

def get_blog_metadata():
    metadata = []
    repo_root = os.getcwd()
    
    # Iterate through all directories in the root
    for dir_name in os.listdir(repo_root):
        dir_path = os.path.join(repo_root, dir_name)
        if os.path.isdir(dir_path):
            readme_path = os.path.join(dir_path, "README.md")
            
            if os.path.exists(readme_path):
                # Get pinned status
                pinned = any(f.lower() == "pinned" for f in os.listdir(dir_path))
                
                # Get last commit date using git log
                try:
                    git_cmd = ["git", "log", "-1", "--format=%cd", "--date=iso-strict", "--", dir_name]
                    result = subprocess.check_output(git_cmd, stderr=subprocess.STDOUT, text=True)
                    last_commit = result.strip()
                except subprocess.CalledProcessError:
                    last_commit = datetime.now().isoformat()
                
                # Collect tags from filenames (excluding README.md and pinned)
                tags = set()
                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)
                    if filename not in ["README.md", "pinned"] and os.path.isfile(file_path):
                        # Split filename by semicolons and clean tags
                        for tag in filename.split(';'):
                            cleaned_tag = tag.strip()
                            if cleaned_tag:
                                tags.add(cleaned_tag)
                
                # Add to metadata
                metadata.append({
                    "Title": dir_name,
                    "LastUpdate": last_commit,
                    "Pinned": pinned,
                    "Tags": ";".join(sorted(tags))
                })
    
    return sorted(metadata, key=lambda x: x["LastUpdate"], reverse=True)

if __name__ == "__main__":
    metadata = get_blog_metadata()
    with open("metadata.json", "w") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
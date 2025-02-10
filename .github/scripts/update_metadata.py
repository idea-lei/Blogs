import os
import re
import json

def main():
    # Path references
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
    
    metadata_path = os.path.join(repo_root, 'metadata.json')
    tags_path = os.path.join(repo_root, 'tags.json')

    # Will store all blogs' metadata
    metadata_list = []
    
    # Will store all distinct tags (in uppercase)
    all_tags = set()

    # Regex: Capture date in group(1) and the rest of the title in group(2)
    # Example: "2025-01-01 My Awesome Blog Title"
    folder_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})(?:\s+(.*))?$')

    # Scan the repo root for potential blog directories
    for entry in os.scandir(repo_root):
        if entry.is_dir() and not entry.name.startswith('.'):
            match = folder_pattern.match(entry.name)
            if match:
                date_part = match.group(1)
                # The second group is the actual blog title (excluding the date)
                blog_title_part = match.group(2) or ""  # default to "" if None

                # Check if pinned file exists
                pinned_file_path = os.path.join(entry.path, 'pinned')
                pinned = os.path.isfile(pinned_file_path)
                
                # Look for a file ending in ".tags" to extract tags
                blog_tags_str = ""
                for f in os.listdir(entry.path):
                    if f.endswith('.tags'):
                        # Remove extension to get tags string, e.g., ".NET;Blazor"
                        tag_part = os.path.splitext(f)[0]  # ".NET;Blazor"
                        blog_tags_str = tag_part
                        # Add tags to global set
                        for t in tag_part.split(';'):
                            normalized = t.strip().upper()
                            if normalized:
                                all_tags.add(normalized)
                        break  # assuming only one .tags file per folder

                # Build the metadata entry
                metadata_list.append({
                    "Title": blog_title_part.strip(),  # remove leading/trailing spaces
                    "CreationDate": date_part,
                    "Pinned": pinned,
                    "Tags": blog_tags_str
                })

    # (Optional) Sort metadata_list — e.g., descending by date.
    # metadata_list.sort(key=lambda x: x["CreationDate"], reverse=True)

    # Write out metadata.json
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata_list, f, indent=4, ensure_ascii=False)

    # Write out tags.json (sorted list of uppercase tags)
    tags_list = sorted(all_tags)
    with open(tags_path, 'w', encoding='utf-8') as f:
        json.dump(tags_list, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()

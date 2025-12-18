#!/usr/bin/env python3
import os
import sys

POSTS_DIR = "docs/posts"
STATE_FILE = "post_list.txt"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return None  # None = first run

def save_state(posts):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(posts)))

def main():
    # List current Markdown posts
    current_posts = {f for f in os.listdir(POSTS_DIR) if f.endswith(".md")}

    old_posts = load_state()

    # First run: bootstrap, no posts sent
    if old_posts is None:
        save_state(current_posts)
        sys.exit(0)  # exit silently

    # Determine new posts that haven’t been announced yet
    new_posts = current_posts - old_posts

    # Save the updated state
    save_state(current_posts)

    # Output new posts filenames
    for post in sorted(new_posts):
        print(post)

if __name__ == "__main__":
    main()
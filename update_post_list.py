#!/usr/bin/env python3
import os

POSTS_DIR = "docs/posts"
STATE_FILE = "post_list.txt"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return set(line.strip() for line in f if line.strip())
    return None  # None = first run

def save_state(posts):
    with open(STATE_FILE, "w") as f:
        f.write("\n".join(sorted(posts)))

def main():
    current_posts = {os.path.basename(f) for f in os.listdir(POSTS_DIR) if f.endswith(".md")}
    old_posts = load_state()

    # First run: initialize state and exit without posting
    if old_posts is None:
        print("Bootstrap mode: initializing state file. No posts will be sent.")
        save_state(current_posts)
        return  # exit without outputting posts

    # Determine new posts
    new_posts = current_posts - old_posts
    save_state(current_posts)

    # Output new posts (filenames) for other scripts
    for post in sorted(new_posts):
        print(post)

if __name__ == "__main__":
    main()
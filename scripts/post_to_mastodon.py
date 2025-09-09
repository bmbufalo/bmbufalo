#!/usr/bin/env python3
import os
import sys
import frontmatter
from mastodon import Mastodon

POSTS_DIR = "docs/posts"

MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
MASTODON_API_BASE = os.getenv("MASTODON_API_BASE", "https://mastodon.social")

if not MASTODON_ACCESS_TOKEN:
    print("[ERROR] MASTODON_ACCESS_TOKEN not set")
    sys.exit(1)

mastodon = Mastodon(
    access_token=MASTODON_ACCESS_TOKEN,
    api_base_url=MASTODON_API_BASE
)

for md_file in sys.argv[1:]:
    path = os.path.join(POSTS_DIR, md_file)
    if not os.path.isfile(path):
        print(f"[WARN] Skipping missing file: {path}")
        continue

    post = frontmatter.load(path)
    title = post.get("title", md_file)
    slug = os.path.basename(md_file).replace(".md", ".html")
    url = f"https://brian.bufalo.me/posts/{slug}"

    # Skip if mastodon_url already exists (idempotent)
    if "mastodon_url" in post.metadata:
        print(f"[INFO] Already posted to Mastodon: {title}")
        continue

    status = f"📢 New blog post: {title}\n\n{url}"

    try:
        if "image" in post.metadata:
            media = mastodon.media_post(post.metadata["image"])
            mastodon_post = mastodon.status_post(status, media_ids=[media])
        else:
            mastodon_post = mastodon.status_post(status)
    except Exception as e:
        print(f"[ERROR] Failed to post '{title}' to Mastodon: {e}")
        continue

    # Save Mastodon post URL in frontmatter
    post.metadata["mastodon_url"] = mastodon_post.url
    with open(path, "w", encoding="utf-8") as f:
        frontmatter.dump(post, f)

    print(f"[INFO] Posted '{title}' to Mastodon: {mastodon_post.url}")
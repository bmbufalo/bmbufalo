#!/usr/bin/env python3
import os
import sys
import frontmatter
from mastodon import Mastodon

POSTS_DIR = "docs/posts"

MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
MASTODON_API_BASE = os.getenv("MASTODON_API_BASE", "https://mastodon.social")

mastodon = Mastodon(
    access_token=MASTODON_ACCESS_TOKEN,
    api_base_url=MASTODON_API_BASE
)

for md_file in sys.argv[1:]:
    path = os.path.join(POSTS_DIR, md_file)
    post = frontmatter.load(path)
    title = post.get("title", md_file)
    slug = os.path.basename(md_file).replace(".md", ".html")
    url = f"https://brian.bufalo.me/posts/{slug}"

    status = f"📢 New blog post: {title}\n\n{url}"

    # Post to Mastodon (with optional image)
    if "image" in post.metadata:
        try:
            media = mastodon.media_post(post.metadata["image"])
            mastodon_post = mastodon.status_post(status, media_ids=[media])
        except Exception as e:
            print(f"[WARN] Could not upload image: {e}")
            mastodon_post = mastodon.status_post(status)
    else:
        mastodon_post = mastodon.status_post(status)

    # Save the Mastodon post URL to frontmatter
    mastodon_post_url = mastodon_post.url
    post.metadata["mastodon_url"] = mastodon_post_url
    with open(path, "w", encoding="utf-8") as f:
        frontmatter.dump(post, f)

    print(f"[INFO] Posted '{title}' to Mastodon: {mastodon_post_url}")
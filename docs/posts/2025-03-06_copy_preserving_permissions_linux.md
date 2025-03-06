---
date:
  created: 2025-03-06T00:00:00
  updated: 2025-03-06T00:00:00
categories:
  - tech
tags:   
  - linux
  - terinal
  - kb
pin: false
draft: true

---

# Copy files, change permissions, and change owner/group

While you can `cp`, `chown`, and `chmod` a file (usually with sudo) to manage a file move, the install command is also for moving files (it’s not for installing things, apparently) and setting various file-level details during the move ; combining with sudo this can be a single command to perform all the necessary actions to move files between various locations!

```bash
sudo install -C -m 775 -o sk -g ostechnix /dir1/file1 /dir2
```

While you can use this command as a replacement for cp, if you do not explicitly set permissions on the operation, this will result in execution permissions being applied. However, this, as the command is probably intended, is helpful for deploying scripts in the correct state.

Source: [How To Copy Files And Change The Ownership, Permissions At The Same Time](https://ostechnix.com/copy-files-change-ownership-permissions-time/)
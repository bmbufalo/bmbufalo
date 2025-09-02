---
title: "Passkeys in iCloud Keychain"
date: 2021-06-28
updated: 2022-11-21
authors:
  - bmbufalo
original_link: https://brian.bufalo.me/2021/06/28/passkeys-in-icloud-keychain/
draft: false
---
<!-- wp:paragraph {"dropCap":true} -->
<p class="has-drop-cap">No one likes passwords. And <a rel="noreferrer noopener" href="https://www.microsoft.com/en-us/microsoft-365/blog/2018/11/20/sign-in-to-your-microsoft-account-without-a-password-using-windows-hello-or-a-security-key/" target="_blank">everyone</a> is trying to replace them, even Apple! This year at #WWDC21 they announced they are working on a new private/public key authentication method designed to replace passwords entirely. If you have ever dug into using your terminal and SSH, then this should feel familiar. Simply create a private and public key on your computer and only share the public key with sites that you want to share your identity with. One of the challenges with SSH keys is managing them on multiple devices and with multiple sites. For Apple's solution, they are using iCloud to sync the keys and offering tools to help you manage this process, making key management seamless. If you are interested, I recommend watching the presentation for a peek at what's coming soon! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>See: <a rel="noreferrer noopener" href="https://developer.apple.com/wwdc21/10106" target="_blank">SSH Key's in iCloud Keychain for apps and websites</a>.</p>
<!-- /wp:paragraph -->

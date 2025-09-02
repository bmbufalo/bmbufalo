---
title: "Cyberduck and Duck CLI"
date: 2022-11-21
updated: 2022-11-21
original_link: https://brian.bufalo.me/?p=178
draft: false
---
<!-- wp:paragraph -->
<p>There are so many different options for accessing files on remote servers and they vary in quality and ease of use. I've tried many of them but, by far, my new favorite is the combination of Cyberduck and Duck CLI. This combination of tools are perfect for accessing a remote server to manage files and automate backups! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Cyberduck is the GUI app that lets you easily navigate any of your remote servers and any local computers on your network using Bonjour. You can easily connect securely to the server with username and either password or ssh keys which are integrated to review the existing keys you have stored in your ~/.ssh folder. You can also store your username and password securely in iCloud Keychain, ensuring they are secure and synced to all your devices. The tight integration doesn't stop there, Cyberduck provides notifications and other standard native integrations with your Mac to provide a seamless experience. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Duck CLI provides the same features as Cyberduck but all from the command line! Updating files and backing up websites are all possible using the simple command line options. To simplify the setup of Duck CLI, I recommend first downloading Cyberduck and setting up the configurations so that they are cached in your iCloud Keychain and then access your servers via the command line. Some examples of what you can use Duck CLI for are:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Backup your files to an S3 bucket on your computer</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>s3://</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

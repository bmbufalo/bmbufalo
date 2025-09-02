---
title: "Automatic WordPress Backups"
date: 2022-11-21
updated: 2022-11-21
authors:
  - bmbufalo
original_link: https://brian.bufalo.me/?p=174
draft: false
---
<!-- wp:paragraph -->
<p>Backups are essential for running a website (or really anything else you do on a computer). And finding a simple solution to perform them regularly can be a challenge. You are, generally, trying to connect to a remote server, capture a backup of the database and the site, archive the files, and then pull the files to your own computer to store them. And you still need to get the backups to a third (and off-site) location to ensure true backup continuity in the case of the worst disasters. The examples below are one's I use to capture backups of a couple of sites I have hosted on DreamHost, but there are many ways to get the same results and this process can easily be replicated. The best part about this method is that it can be easily replicated or modified to meet your requirements and backup technologies of choice. My way demonstrates how to do this using as many open source technologies as well so they are freely available and generally cross-platform (although we all know we will get the best results running on Mac or Linux). If you are doing this on Windows, I highly recommend using the Linux Subsystem to add bash and Ubuntu to your existing Windows command line or use chocolatey to install the required software. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Create SSH keys to your remote server</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This system I use assumes that SSH keys have been generated for command-line access to your site. If you are not already using SSH keys, you really should! They massively improve security overall and once set up, you don't need to enter in your password to connect any longer. The most important thing to remember is that you never share your private key with anyone, only your public key (the one that is generated with a .pub file extension). DreamHost has a wonderful article on <a rel="noreferrer noopener" href="https://help.dreamhost.com/hc/en-us/articles/216499537" target="_blank">getting set up with SSH keys</a> on various platforms that I suggest you refer to and if you are using another host, follow their documents or just modify these steps to match their configuration. In addition to setting up SSH keys, I highly recommend setting up an SSH Config alias which will make using keys much simpler when running commands. This allows you to reference your SSH keys using an alias you chose and without the need to reference the additional details of where the key is located. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Backup WordPress</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once you have your keys set up, the first step is to backup your WordPress site and database. The best way to get a copy of that information is to use WP-CLI to capture a database backup first. If you are not familiar with <a rel="noreferrer noopener" href="https://developer.wordpress.org/cli/commands/" target="_blank">WP-CLI</a>, I recommend getting familiar with the product as it's a wonderful way to manage your site using just the command line.  </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>wp --ssh=dhs_gt:/home/dh_jik7er/buffalochips.online/ db export</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This will generate a SQL backup on your remote server in your WordPress site folder with a default name of: </p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>{dbname}-{Y-m-d}-{random-hash}.sql</p><cite><a href="https://developer.wordpress.org/cli/commands/db/export/" target="_blank" rel="noreferrer noopener">wp db export</a></cite></blockquote>
<!-- /wp:quote -->

<!-- wp:heading -->
<h2>Compress the backup files</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Then, capture an archive of your site using zip (using the date variable to capture today's date and prepend that to the archive name):</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>date=`date +%Y-%m-%d.%H:%M:%S`
zip -r $date_site.zip ~/site/</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>Backup to your computer using Duck CLI</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Duck CLI is a wonderful and fully featured utility made by the same creator of the fantastic Cyberduck app! While you can perform these tasks using built in scp commands or other methods, I like Duck CLI as it works well with multiple backup methods, including working with S3 buckets. </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>duck --username username --identity ~/.ssh/id_rsa --download sftp://site.com/home/username/folder/</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>Upload to DreamObjects</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We will again use Duck CLI but this time, we will upload our latest backups to a DreamHost DreamObjects bucket using an S3 connection. While I'm using DreamObjects, any S3 compatible bucket will work here but the setup will vary by provider so modify to match their configuration requirements.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>duck --username  ~/Documents/Buffalo\ Chips/Backups/ s3://.../</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

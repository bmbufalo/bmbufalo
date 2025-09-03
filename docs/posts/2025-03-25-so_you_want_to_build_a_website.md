---
date:
  created: 2025-03-25T00:00:00
#  updated: 2025-01-01T00:00:00
categories:
  - tech
  - journal
tags:   
  - journal
  - blog
pin: false
draft: true

---

# So you want to build a website

In an effort to document what I've done and, hopefully, pass on that knowledge and hopefully make things easier for someone else, here are some of the basics to making a website. I have been working on converting my sites over from Wordpress to statically generated sites, mostly based on Material for MKDocs but I've experimented with Pelican, Hugo, and Jekyll also. So far, MKDocs is my favorite as it's all Python, YAML, and Markdown based which is directly center of the Venn diagram of what I know. But even if you don't know those things, they are also pretty simple to get started with. If you don't, check out the links and hopefully those can bring you up to speed.

## Python

To build an Material for MKDocs website you will need Python installed first. Each operating system is different and I'm not going to cover them here, there are plenty of guides out there for that. But what I do recommend understanding is that after you have installed Python, using Virtual Environments is a major key to success. Virtual Environments ensure that your Python modules (which Material for MKDocs is) and their depenancies do not overwrite or interfere wtih your systems installed Python. Because that's also the confusing thing about Python, when you install it, you can have several versions of Python available and they live in tandem with the Python that comes with your computer, if you are not running a Windows computer. Windows requires Python to be installed and has no native version but it's still recommended to use Virtual Environments for the same reasons above. If your computer comes with Python, you may also be able to just use that but, like Windows, continue to use Virtual Environments there as well.

To use a Virtual Environment, first create a project folder from the command prompt using a `bash` command such as:

```bash
mkdir ~/mywebsite
```

Then change into that directory with:

```bash
cd ~/mywebsite
```

Then create a Virtual Environment:

```bash
python3 -m venv .venv
```

This will create the environment in your `mywebsite` folder and set up so that your ready to us it for your project. You will then need to activate the Virtual Environment (and, of course, there is a `deactivate` command for when you finish using it):

```bash
source .venv/bin/activate
```

Now, any Python installations you perform will be isolated within the Virtual Environment and you can proceed without impacting your system Python installation.

## Material for MKDocs

Material for MKDocs started off it's life as a theme for MKDocs which is itself the actual static site generator. Those additional features included are so far and beyond what MKDocs can do alone make it worth learning. Of course, if your needs are simple, MKDocs alone may give you what you need and check out their documentation to see.

To get started, create a `requirements.txt` file in your `mywebsite` project folder and add the line:

```txt
pip
mkdocs-material
```

    !!! note It is best practice to actually set this to a version as below but for today we'll get the latest version.
    ```txt
    mkdocs-material==9.6.11
    ```

Then run a command to install Material into your active Virtual Environment:

```bash
python3 -m pip install
```

This will upgrade your version of pip to the latest and then install mkdocs-material and any depandancies that may be required.

You can now create a blank site and get started:

```bash
mkdocs new mkdocs
```

    !!!note The second `mkdocs` is just the name of the site, you can make it anything you want!

Next you can change directories into this folder with:

```bash
cd mkdocs
```

And you can see your website in your browser right away by running:

```bash
mkdocs serve
```

You should see a link to `http://127.0.0.1:8000/` which you can click or copy and paste into your browser and visit your empty but awesome website!

```
mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.03 seconds
INFO    -  [15:44:34] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [15:44:34] Serving on http://127.0.0.1:8000/
INFO    -  [15:44:34] Browser connected: http://127.0.0.1:8000/
``` 

Now, this website is just a shell and only lives on your computer right now, no one else can see it and many options are not set. But from here, the sky is the limit. The website settings are all controlled from the `mkdocs.yaml` file. There is also a `docs` foler that is where you will post all your pages and even blog posts.
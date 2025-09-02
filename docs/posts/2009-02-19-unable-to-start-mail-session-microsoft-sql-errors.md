---
title: "Unable to start mail session Microsoft SQL errors"
date: 2009-02-19
updated: 2009-02-19
authors:
  - bmbufalo
original_link: https://brian.bufalo.me/2009/02/19/unable-to-start-mail-session-microsoft-sql-errors/
draft: false
---
<pre><code>&amp;lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8"&amp;gt;&amp;lt;meta name="ProgId" content="Word.Document"&amp;gt;&amp;lt;meta name="Generator" content="Microsoft Word 11"&amp;gt;&amp;lt;meta name="Originator" content="Microsoft Word 11"&amp;gt;&amp;lt;style&amp;gt; &amp;lt;!--  /* Style Definitions */  p.MsoNormal, li.MsoNormal, div.MsoNormal   {mso-style-parent:"";   margin:0in;   margin-bottom:.0001pt;   mso-pagination:widow-orphan;   font-size:12.0pt;   font-family:"Times New Roman";   mso-fareast-font-family:"Times New Roman";} h3   {mso-margin-top-alt:auto;   margin-right:0in;   mso-margin-bottom-alt:auto;   margin-left:0in;   mso-pagination:widow-orphan;   mso-outline-level:3;   font-size:13.5pt;   font-family:"Times New Roman";} a:link, span.MsoHyperlink   {color:blue;   text-decoration:underline;   text-underline:single;} a:visited, span.MsoHyperlinkFollowed   {color:purple;   text-decoration:underline;   text-underline:single;} span.EmailStyle16   {mso-style-type:personal;   mso-style-noshow:yes;   mso-ansi-font-size:10.0pt;   mso-bidi-font-size:10.0pt;   font-family:Arial;   mso-ascii-font-family:Arial;   mso-hansi-font-family:Arial;   mso-bidi-font-family:Arial;   color:windowtext;} span.google-src-text   {mso-style-name:google-src-text;} @page Section1   {size:8.5in 11.0in;   margin:1.0in 1.25in 1.0in 1.25in;   mso-header-margin:.5in;   mso-footer-margin:.5in;   mso-paper-source:0;} div.Section1   {page:Section1;} --&amp;gt; &amp;lt;/style&amp;gt;Below is an Englsih &lt;a href="http://translate.google.com/"&gt;Google Translation&lt;/a&gt; from Turkish of &lt;a href="http://ekremonsoy.blogspot.com/"&gt;Ekrem &amp;Ouml;nsoy's&lt;/a&gt; blog post with a solution to fix an &lt;span class="google-src-text"&gt;"Unable to start mail session" error message in Microsoft SQL.&lt;/span&gt;&amp;nbsp; I wanted to re-post it here in English in case and save someone the leg work.&amp;nbsp; Anyone else have better suggestions for a fix?&amp;nbsp; Anyone suffering from other SQL woes?&amp;nbsp; Chew it up in the comments!&lt;p /&gt; &lt;blockquote class="gmail_quote" style="border-left:1px solid rgb(204,204,204);padding-left:1ex;margin:0 0 0 .8ex;"&gt;
</code></pre>

<a href="http://74.125.67.102/translate_c?hl=en&amp;sl=tr&amp;tl=en&amp;u=http%3A//ekremonsoy.blogspot.com/2008/02/unable-to-start-mail-session-reason.html&amp;prev=_t&amp;usg=ALkJrhh5std9bD6LqGhNmdc5JL8MSCUQUA">"Unable to start mail session (reason:</a><a href="http://74.125.67.102/translate_c?hl=en&amp;sl=tr&amp;tl=en&amp;u=http%3A//ekremonsoy.blogspot.com/2008/02/unable-to-start-mail-session-reason.html&amp;prev=_t&amp;usg=ALkJrhh5std9bD6LqGhNmdc5JL8MSCUQUA">Mail configuration information could not b</a><br />Microsoft.SqlServer.Management.SqlIMail.Server.Common.BaseException: <strong><span></span></strong><strong>ERROR MESSAGE:</strong><br /> <span class="google-src-text"><span></span>"Unable to start mail session (reason: Microsoft.SqlServer.Management.SqlIMail.Server.Common.BaseException: Mail configuration information could not be read from the database.&gt; System.Data.SqlClient.SqlException: profile name is not valid"</span>

<p />

<strong><span></span></strong><strong>EXPLANATION:</strong><br /> <span class="google-src-text"><span></span>Receive this error, I saw a user habergrubundan and I wanted to archive.</span> <span class="google-src-text"><span></span>The user has created a Mail Profile and Account.</span> <span class="google-src-text"><span></span>Says it can send a test mail.</span> <span class="google-src-text"><span></span>But this account to SQL Server Agent 'ta get this error is when you want to use.</span>

<p />

<span class="google-src-text"><span></span>SQL Server Agent 's properties Alert System' from the Mail Profile 's advice was to Enable.</span> <span class="google-src-text"><span></span>We have checked and this setting was also full.</span> <span class="google-src-text"><span></span>Solution of the problem is very interesting.</span>

<p />

<strong><span></span></strong><strong>SOLUTION:</strong><br /> <span class="google-src-text"><span></span>The person experiencing the problem in Microsoft 's in a "Case" was open and it was suggested that as a solution:</span><br /><span class="google-src-text"><span></span>- Surface Area Configuration from Database Mail 'i Disable the state,</span><br /><span class="google-src-text"><span></span>- Stop SQL Server Agent Service, and start again,</span><br /><span class="google-src-text"><span></span>- Surface Area Configuration from Database Mail 'i bring to the state of Enable.</span>

<p />

<span class="google-src-text"><span></span>Solution of this and it worked.</span>

<p />

<span class="google-src-text"><span><span></span></span><span>You or I would be a day or can it help me.</span></span>
</blockquote>

                           

<p />

Not sure what that last line is but Google Translate isn't perfect yet.&nbsp; Hope this helps!

<p />

--

<p />

Brian M. Bufalo<br /><a href="http://blog.bmbufalo.com/">http://blog.bmbufalo.com</a><br />

<div class="blogger-post-footer"><img class="posterous_download_image" src="https://blogger.googleusercontent.com/tracker/2675399127377711436-5446344884964649?l=bmbufalo.blogspot.com" height="1" alt="" width="1" /></div>

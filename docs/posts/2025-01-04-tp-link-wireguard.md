---
date:
  created: 2025-01-05T21:37:00
  updated: 2025-01-05T21:37:00
categories:
  - tech
  - journal
tags:   
  - meta
  - blog
pin: false
draft: true

---

# TP-Link and Wireguard

While the news on TP-Link has been pretty awful from a security perspective, recent updates to their Deco line have me really happy. The Deco line of routeres are divided by model and further subdivided by the firware version they recive. Just before Christmas my X55 got updated that I had been waiting on since this summer! The update finally brought Wireguard VPN to the router and while an earlier update allowed for other types of VPNs, such as the ancient L2TP/IPSec or OpenVPN, I really wanted to get a Wireguard setup. Wireguard provides several benefits over traditional VPNs:

1. Connection resiliency: switching from wired to WiFi or cellular doesn't phase the connection, your VPN stays active.
2. Speed and performance: Wireguard is extremely fast as compared to other VPNs.
3. Battery performance on mobile: the lightweight protocol and efficient means much less battery drain.
4. On-demand: The mobile app allows iOS devices to be configured to always route traffic when not at home to ensure that my connection is always on and secure (read: private).
5. Easy access to devices at home: I have a couple devices and computers I access when out and about that Wireguard allows me to seamlessly connect to while on the go.

Previously, I had been using Tailscale to provide a lot of these services and keep my connections safe and secure. And I still highly recommend the service, it's really increadible if you don't have access to Wireguard on your router or need advanced routing capabilities for a home lab or even at a large corporation. I wish more companies used services like Tailscale as it provides really easy access to on-prem or cloud resources with a lightweight client. But by self-hosting Wireguard, I can assure my connection back to the house for all my devices without relying on external providers and wihtout having to host complicated servers. Of course, many routers provide Wireguard acces and someone with the know-how can easily set up a server to host and run a Wireguard server to provide this same setup. But I like to keep things simple and Deco's implimentation is exactly that.

It is hard to overstate how nice on-demand is for mobile devices when out and about. Since setting it up, I've been able to move from home to mobile and never miss a beat all while maintaining connection back to the house. Now I can take my iPhone and iPad and still connect back to my Mac Mini at home as though I am still there. Another device I access on the go often I recently got is my Tablo TV. It allows me to watch over-the-air TV via their app on my smart devices. With Wireguard, I have easy access to it as well to watch live streams of TV or recorded shows from anywhere. I will probably do a longer post on my thoughts on it, later.

Another feature I just started playing with is, in additon to creating a VPN Server with my Deco, I can configure a VPN client that lets me have all or select devices connect to an external Wireguard VPN service such as NordVPN, ProtonVPN, or Surfshark. This lets me route my devices at home through alternative VPNs. This allows for privacy for home connections and all kinds of other possibiliteis for obscuring traffic.

Any chance to set up a VPN is recommended, especially if you can get one connected back to your home router. This is, of course, all improved since we have access to fiber here at the house and your own milage may vary.
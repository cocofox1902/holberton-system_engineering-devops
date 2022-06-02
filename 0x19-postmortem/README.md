## Postmortem on my servers
I was working to make an parti of my project assibile online but the fate willed it in an other way. That storie take 2 days to be fix. That fix was not hard but just really weird.
I have a friend that also have that probleme but a lot of people didn't have that probleme so that was confusing.
The root cause was the execution of an programme to install all the things.

I discover this with the non possibility of starting my serveur that won't balance between two serveur.
It was detecded because when a loadbalencer is doing is work the ip taht he balance to it always change.
For that probleme i have to relaod the serveur so i crush my laodbalancer. With the project i was able to have  4 different serve so 4 crush possible but it was my first so i was not woried.
At first i was thinking that was the the code that i executing but that was not it because i take a code of my friend were it work but that seems to be not working either so i crush another server
I have to crush it again becaus that was not working but it was my last serveur so this has to be working or it will finished without loadbalancer. But with a miracle i compile the programme and the load balancer was working. So if you have a probleme kill it. Because i have i have not other issue. 
So for the future if you are a probleme in my life i will take it like my server the 4 times will be the good so killing you will be an option.

I think that the issue was the fact that i was telecharging an other thing that was causing to corrupte the server.
I think for me that was to have no fear to restart an serveur because at first i do not wanted to restart the serveur.
Say when you don't have to install Nginx.
# The very first blog - something about this website

## How it is built

After the very primitive monolith project organization strategy, the microservice was becoming popular. The thing is, if you build a online marketing website, it would be good to implement the microservice. But it will be far too over engineered to build a personal website using microservice that only for some tiny functional modules.

That's why the modularized-monolith is widely used for mid-level projects. The functional modules are isolated to each other and can be easily attached to / removed from the Host (or Core) project, which means if one module is not working well, it will not affect other modules. Each module has its own services, DbContext etc. and they are registered into the shared DI pool. This architecture is also called **Plugin-based modularized monolith**, which is more flexible than simple modularized monolith, since plugins can be registered / unregistered easily.

This website is hosted in docker container, the process is automated using GitHub CI/CD.

## Why the domain is 'XRify'

Actually the website was originally thought for a Startup (started in 2022, called XRify - to enable some traditional processes to be supported by XR). I've chosen '.net' as ending since I develop in .net area. But due to some reasons the startup is always under concept.

As I'm writing this blog, I searched the internet and found some smart guys have used the same name 'XRify' but '.de' for their website, they are doing almost the same thing as I do. Well maybe good ideas look similar, wish them good luck with their business. Maybe we can cooperate in the future.

## Why I bother to build own website for blogs

Well it's actually not only for blogs. There are more functions, but only a few of them are public (like Resume and blogs).

Speaking of blog, I tried posting some blogs on Medium, which is a nice website for bloggers and readers. The problem is if I want to post blog on that website, I need to become "premium", for which I need to pay about 40 euro per year. I found this nonsense because I need to pay to help others with knowledge. Besides, hosting this website will only cost me about 60 euro a year - and I can build much more than blogs for my personal needs.

Besides, I heavily use Markdown for writing but the Medium does not support it well. Meanwhile I do not like writing directly in browser. With my own implementation I can use github repo as my CMS for free.



If there is anything to be added, I will update this blog.
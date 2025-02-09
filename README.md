# Blogs
This repository is for hosting blogs for [my personal website](https://xrify.net/blogs). You can visit the site to get better Markdown reading experience.













I want to write a blazor component module to render my blogs that stored on github in a repo.

The repo has the following structure:

"""

repo

+ README.md
+ tags.txt (containing all tags)
+ Blog name 1 (folder)
    + README.md
    + tag file (example file name: *.NET;Blazor*, file has no content, using file name to determine which tags does the blog have)
    + pinned file (if this file exists, the corresponding blog will be pinned at top)
    + images...
+ Blog name N (folder)
+ ...

"""

I want to fetch the info from this repo (blogs folder) to get the blog list with update date, and corresponding tags, and of course the 'pinned' info.

When user select a blog, the whole folder of the blog will be loaded, to render the md file and its corresponding images. please convert the image path (from ./image.png to path to the image.png on github)

You do not need to care about how I render the md file.

I also want to build a typed httpclient for request to github with my token. the client should be called 'GithubClient' and the token is from appsettings json (config["GithubToken"]). The client should have 3 methods: 

+ `public Task<BlogNoContent[]> GetBlogsAsync(params IEnumerable<string> tags)`
+ `public Task<Blog> GetBlogAsync(string title)`
+ `public Task<string[]> GetAllTagsAsync()`

Here are my models:

```c#
public class Blog : BlogNoContent
{
    public string Content { get; set; }
}

/// <summary>
/// To avoid necessarily loading content 
/// </summary>
public class BlogNoContent
{
    public string Title { get; set; }

    /// <summary>
    /// last commit time
    /// </summary>
    public DateTime LastEditTime { get; set; }

    public bool Pinned { get; set; }

    public ICollection<string>? Tags { get; set; }
}
```

# Jasmin's World Cup Blog

- **Jasmin's World Cup Blog** is a place where you can find out about the latest news and updates regarding the World Cup 2022 in Qatar. Jasmin follows every game and every goal and will be posting relevant content during the duration of the Cup (and perhaps the next World Cup). The blog provides deep insight on the teams and and the players and gives predictions for the tournament. Jasmin/the creator of the site is a huge football fan and has been following the World Cup since 1998. He has been to the World Cup in 2010 and 2014 and is a big fan of Croatia, which is part of his family heritage. He is also a big fan of the Italian Serie A and follows the teams in the league closely.

- The goal of the blog is to share football knowledge surrounding the teams and help people predict results. The posts cover previous matchups, predicted line-ups and some story-telling around the squads. 
- The purpose is also to collect donations to fund trips to upcoming World Cups through it's donation-page.
- The site has an about page so that you can find out more fun-facts about the host and get to know him. 
- The site has 6 posts per page ranked from latest-to-oldest directly on the landing page. 
- The page is also looking for guest-writers to provide extra content, however these posts need to be approved by admin. 

<img> ![A screenshot of the first Question on the page](assets/images/quiz-full-page.png)

# User Experience
## User Stories
---
### As an unregistered, I want to :

+ Be able to read the blog posts.
+ Be able to view the Donate & About Page.
+ Have the ability to register to the site.
+ Be able to read comments.

### As a registered user, I want to:

+ Have the ability to like posts.
+ Be able to make comments.
+ Have the ability to bookmark my favourite posts.
+ Be able to log-out.
+ Be able to view the profile page to see my bookmarked posts. 

### As a superuser, I want to:

+ Be able to log in to an admin panel.
+ Be able to add, delete and edit posts. 
+ Be able to approve posts through the admin panel. 

## Design
---
### Overall feel

For this site I wanted it to be easy to distinguish text and photos with clear headlines, clear text and not too much clutter. 

### Color Scheme

The color green is what many people associate to football because of the grass on the field, howver dark green would make it hard to read text
so I went with a light green color instead. 

### Typography


I went with Oswald for headers and titles, which is a font that I'm very familiar with personally through my video-game background, I find it easy and clear to read.

I chose Public Sans because it feels a bit 'type-writy' and bloggish. Very not-corporate. 

### Bootstrap and Initial Design


Much of the design is borrowed from the 'I think therefore I blog' course-material and tweaked for own personal preference. 

### Imagery


Images on the site are all connected to football in some way or another and they are all from google sorted from the Creative Commons licenses page. 

## Features
---

### Navbar

- The navbar has links to different pages, those are: Home, About, Donate, and Login/Logout. 

### Landing Page

- The landing page has functional links to each post, with an image, who the author is, and title of the post with a small excerpt. Below these is the post date together with the total amount of likes. At the bottom you can click a link so that you can write a guest-article. 

<img> ![A screenshot showing the points being kept, timer going down and event listener triggering on click.](assets/images/game-area-green-button.png)

### The Post-Pages

- If you click the titles, you will get redirected to each post. These pages have Title and images in a neat design, and the body-text of the content below. Below the text you have buttons to like and bookmark the page. Below that you can write a comment, and view the comments on the post. The bookmark and ability to like will only be displayed if you are logged in. 

### About

- The About page is a simple static page with some text about Jasmin (creator of the page)

### Donate

- Donate-page is a page where I explain that the page needs funding in order to be able to run, and where Jasmin is trying to crowd-fund to be able to go to the World Cup. The donation-link is a paypal-image that leads right to the 'send-money' page on Paypal. 

###

- Register page is a simple page so that the user can create an account with a username and password. The e-mail is optional. 
Users need to register and login to be able to like, bookmark and comment. 

### Login/Logout

- The link in the navbar leads you to a page where you can login and logout from your account. 

### Profile

- For now the profile page exists so that the user can view their saved bookmarks, but could be used in future versions for things such as created posts.
Editing a user-profile and adding flavor-text about the user.  

### Footer

- Footer is simple with a text explaining where to go to follow me on socials. 

### Delete

- Delete page exists for super-users, this is a simple page that asks you if you 'really' want to delete a post, currently only has post titles but could be more polished in future versions. 

## Possible Future Features
+ A profile page with more tools to manage posts and a way to have other users check out profiles and read about the people.
+ Users ability to delete their account.

## Defensive Design Features

### Delete Post
- When you delete a post, you're re-directed to a delete page where you're shown the title of the posts you're deleting and if you want to continue doing so. 

### Authenticated vs Unauthenticated
- Unauthenticated users can't add comments, this is to prevent spam and uphold integrity.
- UA users can't like posts, this is to prevent like-padding and botting.  

# Database
---

### 
<img> ![A screenshot of the pop-up form](assets/images/pop-up.png)

<img> ![A screenshot of my g-mail inbox after playing the game](assets/images/e-mail-submission.png)

## Testing

<img> ![Image of page on different screen-size](assets/images/responsiveness.png)

## Bugs
---
### Solved Bugs

- Solved bugs with the help of my mentor where the 'bookmark' button wasn't working properly. 

## Validator Testing
---
### HTML



### CSS



### JSHint



### Accessibility


<img> ![An image showing the scores of 96 in accessibility and a score of 100 in performance, best practices and SEO in the Lighthouse Tool in DevTools.](assets/images/lighthouse-scores.png)

### Unfixed Bugs

- Like button showing two 'hearts' instead of one that becomes red after it's liked. 

## Deployment

- The Site was deployed to the GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository navigate yourself to the Settings tab.
  - From the source section drop-down menu, select the Main branch. 
  - Once the main branch has been selected, the page provided the link to the completed website. 
  
- The live link could be found here: [Coolest Movie Quiz](https://j-a-s-m-i-n-j.github.io/movie-project-new/).

## Credits
---
### Content


### Guides & Troubleshooting




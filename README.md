# Jasmin's World Cup Blog

- **Jasmin's World Cup Blog** is a place where you can find out about the latest news and updates regarding the World Cup 2022 in Qatar. Jasmin follows every game and every goal and will be posting relevant content during the duration of the Cup (and perhaps the next World Cup). The blog provides deep insight on the teams and and the players and gives predictions for the tournament. Jasmin/the creator of the site is a huge football fan and has been following the World Cup since 1998. He has been to the World Cup in 2010 and 2014 and is a big fan of Croatia, which is part of his family heritage. He is also a big fan of the Italian Serie A and follows the teams in the league closely.

- The goal of the blog is to share football knowledge surrounding the teams and help people predict results. The posts cover previous matchups, predicted line-ups and some story-telling around the squads. 
- The purpose is also to collect donations to fund trips to upcoming World Cups through it's donation-page.
- The site has an about page so that you can find out more fun-facts about the host and get to know him. 
- The site has 6 posts per page ranked from latest-to-oldest directly on the landing page. 
- The page is also looking for guest-writers to provide extra content, however these posts need to be approved by admin. 

<img> ![A screenshot of the first Question on the page](assets/images/quiz-full-page.png)

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

### Login/Logout

- The link in the navbar leads you to a page where you can create an account and login. This is needed to be able to write guest-posts and like/bookmark items. When you're logged in, the navbart-link shows 'logout' and vice versa. 

### Footer

- Footer is simple with a text explaining where to go to follow me on socials. 

<img> ![A screenshot of the pop-up form](assets/images/pop-up.png)

<img> ![A screenshot of my g-mail inbox after playing the game](assets/images/e-mail-submission.png)

## Testing

- I conducted a test in Firefox and it was fully functional. The button styling looks a little different, but not much. And I think that the game actually runs better in FireFox because the page is loading everything first. Will elaborate on this in the Bugs-section. 
- When testing in Safari the functionality was good, but just like on Chrome, sometimes the page doesen't load before the alert. Buttons looked the same as they did on FireFox. 
- Chrome has been the main browser whilst creating this game, where additional testing has been done.
  - Tested if all answers were correct. 
  - Tested if there was a way to cheat the input form. 
  - Also tested rushing the game and spam-clicking buttons. 
    - During the development process, I did this a few times and it returned an error, I planned on finding it to add as a screen shot but it was something I couldn't replicate again.
- Confirmed that the site is responsive and works on all different screensizes ranging from 320 pixels to 1200 pixels and above. This includes the pop-up. 
- Confirmed that text is readable, buttons usable, and images are visible. 

<img> ![Image of page on different screen-size](assets/images/responsiveness.png)

## Bugs
---
### Solved Bugs

- Difficulty getting images to be responsive, this was solved with adding several media queries that make the image smaller.

- In the beginning, when clicking buttons they would change color, and the next question would show. However, the color then stayed on that button for the rest of the game, and eventually all buttons would carry colors from previous questions. 
  - This was solved by delaying the loop using 'Promise' 'Resolve' 'Async 'Await', and adding it to the event listener. After the 'answer-button-color' there is a small delay, and then the function clear the colors using button.style. 

- During the process I learned about timers, and how tricky they can be to set-up. I have learned that there are a few different ways to set up a timer, but some of them sometimes only counted up, minutes, wouldn't work at all, or they wouldn't trigger on if-else-statements. 
  - I reached out to the tutors, and they told me I needed a clearInterval function. After this it worked as intended.  

- In my first meeting with my mentor when I presented the wireframe for the project, he added that it would be nice that if by the end, and time was plenty, I should make the make the scores to be sent by e-mail.  
  - Upon writing code and researching I learned that it wasn't possible to do so with only javascript. I finished the function and awaited my final meeting where he showed me emailJS. 
  - There were some problems configuring names with id's in emailJS at first, and after that I received errors in the console. This was because I had added the function to the event listener for the "game-buttons" (making it work like a submit button) thinking that it was alright. 
  - In the end I gave the submit-form-button it's own event listener and errors stopped. 
  - The e-mail validation wasn't working properly. Empty field triggered alerts, however inserting anything in both fields submitted successfully.
  - The HTML with type=email and required also didn't work as intended.
  - This was solved by changing the button to an input instead, and updating that in the event listener. 

## Validator Testing
---
### HTML

- Few errors that have been fixed with official W3C HTML Validator.

### CSS

- Recieved some typing errors that have been fixed. Validated with W3C (Jigsaw) CSS Validator.

### JSHint

- Received comment: "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (isCorrectAnswer, currentQuestion, answerButton, correctAnswerHandler, timeFunction, getNextQuestion, showQuestion, showPopup)". 
  - They are all working as intended though. 

- There are 4 undefined variables: minutes, seconds, Promise, emailjs - but their functions work properly. 

- No console errors are triggering.

### Accessibility
- Confirmed that fonts and colors are readable and site is accessisble through Lighthouse in DevTools. 

<img> ![An image showing the scores of 96 in accessibility and a score of 100 in performance, best practices and SEO in the Lighthouse Tool in DevTools.](assets/images/lighthouse-scores.png)

### Unfixed Bugs

- The timer actually start at 00:00 - then goes up to 01.00 before counting down, which means players actually get about 62 seconds to play the game. 

- There is a minor inconvenience at the start of the game: About half of the times on Safari / Chrome the alert triggers before the page has been loaded in the back. 
  - The idea is that while you read the alert, and recieve further instructions to look at the bottom (to read rules), it actually wont load fast enough. 
  - In the event of this, players then have to press OK - start the game, read the rules at the bottom, and then refresh page to get back the time lost. This solution is presented in the alert. 
  - FireFox does not have this issue. 

- Not really a bug, more of a disclaimer: I intended to use real snapshots / images for many of the movies, however I do not have rights for any good ones. 
  - All photos used are licensed for "creative" use, however many photos are of lower quality and not being able to find the right sizes has impacted the overall style. 

- I had intended to use something different instead of the alert in the beginning to confirm player is ready, like a pop-up, button or model, but time ran out. 

## Deployment

- The Site was deployed to the GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository navigate yourself to the Settings tab.
  - From the source section drop-down menu, select the Main branch. 
  - Once the main branch has been selected, the page provided the link to the completed website. 
  
- The live link could be found here: [Coolest Movie Quiz](https://j-a-s-m-i-n-j.github.io/movie-project-new/).

## Credits
---
### Content

- During Love Math we got to learned how to increment for keeping scores and also how to check answers.
- [Love Math](https://j-a-s-m-i-n-j.github.io/love-maths-jasmin/)

### Guides & Troubleshooting

### Promise, Resolve, Async, Await
- [Geeksforgeeks](https://www.geeksforgeeks.org/how-to-delay-a-loop-in-javascript-using-async-await-with-promise/) 

### EmailJS

- [EmailJS](https://www.emailjs.com/) 

### Window.Onload  

- [Geeksforgeeks](https://www.geeksforgeeks.org/how-to-run-a-function-when-the-page-is-loaded-in-javascript/)
- [Stack Overflow](https://stackoverflow.com/questions/5721704/window-location-reload-with-clear-cache)

### Hiding & Styling a Popup

- [Formget](https://www.formget.com/how-to-create-pop-up-contact-form-using-javascript/)

### Template for Array

- [Simplestepcode](https://simplestepscode.com/javascript-quiz-tutorial/#step2)


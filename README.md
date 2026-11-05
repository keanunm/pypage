<h1 align="center">Pypage</h1>

## python to html!

This is a python file that you can import into your projects.



### How to use:

##### Setup:

Copy the file into your projects. Import it at the top of your python project.

MAKE SURE TO USE THE pypage.init() BEFORE USING ANY OTHER COMMANDS.

###### set\_title

Pypage.set\_title("title")

Allows you to change the title of the site WITHOUT changing repositiory name

###### Addtext

pypage.addtext("This is where you write the text!", "h1")

The first value is the text and the second is the TAG or type of header like: h1, h2, h3, h4, h5, h6, and p!

###### Addimg

It allows you to add images using pypage.addimg("").

You can put your image into the folder created upon running your code once, or put an image address into the file.

###### Addlink

pypage.addlink("my link!", "")

The first value will be the text that you click to go to another website! The second value IS the link to the website.

###### Compile

To compile your code into a functioning HTML file that you can load, you must use pypage.compile() at the end when all of the page details are added.

# RMarkdown requires the latest and greatest packages for formatting and when saving as pdf documents, a latex extension so that it properly reads the formulas in the problems. 

#First, make sure your version of R is the latest by checking the website. If it is not, then take the time to get the latest version of the software. 

# Second, make sure your files are not on the cloud, including OneDrive. If so, then decouple at least your desktop with OneDrive so you can work off the cloud. 

#Finally, run the lines below one at a time. Once the packages are done installing, then restart your computer. Finally, open R Studio and rerun your RMarkdown file.  

install.packages("rmarkdown")
install.packages("knitr")
install.packages("formatR")
tinytex::install_tinytex()
# Select Y when/if it asks down in the console. 

# You may only need to update one of these packages, but they are all connected, so I gave you all of the install commands because this ensures that they are all up to date. 

# If you are having difficulty knitting to pdf, feel free to publish it in a .html and print the .html to a .pdf. I just ask that the final uploaded document with answers be a pdf. To do this, click the drop down arrow on the Knit option and select Knit to HTML.


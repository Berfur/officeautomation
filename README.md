# The power of automation and templating

*Templating* is an effortless strategy to create patterns of information to simplify tasks (both simple and complex). It's mainly an intellectual task, and a very personal one. Some templates you can borrow, but you can't use them without understanding them. For example, you can copy a markdown or todo.txt template. But you can't use them if you don't know markdown or todo.txt syntax.  
*Automation* is the practice to have a repetitive task (providing the correct template for example) the most effortless way possible. It does not matter if you automate electronically, mechanically, humanly or informatically. Do as you please, the best way for you. 

I mostly work in an office environment (windows, email, word processing, etc.). I have *a lot* of repetitive tasks, so I try to automate most of the trivial tasks.

## Templating old and new
If you work with computers a lot you totally get how useful is to have templates for anything involving writing. Programming (skeletons or snippets) or word processing. A template is a very handy thing to set up.
Problem is: you have to set it up every time you change your setup (word; programming environment and so on). Because every tool have it's template management system (not really, text files are always available).
Espanso lets you leverage the power of text templates to every environment.

I organized the templates by function (as it should be), not by program:
Greetings
Mail
Markdown

## Scripts for office automation
Most of it is performed by [Espanso](https://espanso.org/), a wonderful cross platform application for text expanding by [Federico Terzi](https://federicoterzi.com/).
Espanso has the advantage of not being binded to *one* application. It works in word; excel; browsers; shell; everyplace you can type. Almost.
And it's cross platform: Windows; Mac; Linux.
Part is done trough Python (Espanso lacks conditions). But I am far for sufficient in working with it.

# What's in there?
* a collection of [markdown](https://daringfireball.net/projects/markdown/) templates, automated by Espanso. I use [Pandoc](https://pandoc.org/)'s flavour because I think it's complete.

* shortcuts for dealing with other tasks like writing emails (a time-of-the-day aware shortcut for greetings).

# Problems
Sometimes triggers doesn't work if you start tipying in the beginning of the text field. That is true for outlook for example. Just add a space at the start and you're on.

## Installation
You have to install Espanso at least and possibly Python too (for the scripts).
Simply download the yml file inside your .espanso/match directory. Obviously python files go to: .espanso/scripts directory


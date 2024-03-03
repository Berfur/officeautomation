# Espanso Script for Office Automation

I wrote those script to ease the burden of monotonous tasks and repetitive texts.  
It's use is very simple, you couple a trigger (usually a short text formula) to a more long and complex text, and when you type the short formula it gest automatically expanded.

For example:

.bf -> "Buongiorno sig.ra ,"
.cell -> "555 876523"

The program is simple and the scripts can get more complex, even creating simple GUIs.

## Use cases

I use those script to compose texts: email, profiles, professional texts and almost anything that needs templating (useful when you write pandoc documents and excel formulas too).  
It is useful even when you ordinarly write things you don't remember, for example 

I used to work with Word, Outlook and (any other program) but the truth is that it's time consuming to set up a complete set of templates for every program (with it's own syntax and quirks). I find this system a lot better because you have everything at your fingertip. And all you have to do to set it up is to copy some files. Unbeatable.

## Installation and Dependencies
1. You need [Espanso](https://espanso.org). I use the portable version, so very easy on windows. Decompress the archive and follow the instructions to have the system up and running. On Linux I use a snap ('snap install Espanso')
2. Download the scripts you are interested in (remember some scripts depend on other scripts, for example most depends from the "variable.yml" file), and put them in the "match" directory inside Espanso installation.
3. Customize "variable.yml" with your data
* OPTIONAL: .bf and .bm shortcuts depend on a usable python installation. If you want them you need to install python.


# The power of automation and templating

*Templating* is an effortless strategy to create patterns of information to simplify tasks (both simple and complex). It's mainly an intellectual task, and a very personal one. Some templates you can borrow, but you can't use them without understanding them. For example, you can copy a markdown or todo.txt template. But you can't use them if you don't know markdown or todo.txt syntax.  
*Automation* is the practice to have a repetitive task (providing the correct template for example) the most effortless way possible. It does not matter if you automate electronically, mechanically, humanly or informatically. Do as you please, the best way for you. 

I mostly work in an office environment (windows, email, word processing, etc.). I have *a lot* of repetitive tasks, so I try to automate most of the trivial tasks.

## Templating old and new
If you work with computers a lot you totally get how useful is to have templates for anything involving writing. Programming (skeletons or snippets) or word processing. A template is a very handy thing to set up.
Problem is, as I stated before, you have to set it up every time you change your setup (word; programming environment and so on). Because every tool have its own template management system (not really, text files are always available).
Espanso lets you leverage the power of text templates to every environment.

## Due Recognition
Most of it is performed by [Espanso](https://espanso.org/), a wonderful cross platform application for text expanding by [Federico Terzi](https://federicoterzi.com/).
Espanso has the advantage of not being binded to *one* application. It works in: word; excel; browsers; shell; everyplace you can type.
Part is done trough Python (Espanso lacks conditions). But I am far for sufficient in working with it. It could be used way better, please, feel free to change everything you want and please share.

# Problems
Sometimes triggers doesn't work if you start tipying in the beginning of the text field. That is true for outlook for example. Just add a space at the start and you're on.



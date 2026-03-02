# Developer Experience - CDN

## What is it?

> Source 1: A tutorial on CDN, available at https://www.cl.cam.ac.uk/~afb21/CognitiveDimensions/CDtutorial.pdf

Cognitive dimensions is a general tool, in that it's: usable by non-HCI folks (human-computer interaction), and it can be applied to all information systems. It aims to uncover the serious usability issues with an information system.

Dimensions are like different facets of usability.

### Where it's applied?

It aims to _work on_ interactive (like word-processors) and non-interactive (like grpahs) information systems.

It's meant to be applied to any stage of a product and supah easy to understand.

It's centered around lexicalisation: naming familiar concepts, so that they be pointed out, discussed and changed.

### Classes of User-Activity

The framework defines 6 types of user activity, each of which should prioritize different dimensions.

- Incremenation
- Transcription (copying info from one notation to another)
- Modification
- Exploratory Design
- Search\*
- Incremental Understanding\*

All forms of interaction are generalized as either building something or modifying it.\*\*

> \*: The sources for these are [a paper from 2001](https://www.cl.cam.ac.uk/~afb21/publications/CT2001.pdf) by Blackwell et al.
> Although, the paper does mention that the first 4 are more interesting b/c they involve
> "extending" the notation.

> \*\*: The source that introduces this framework seems to differentiate between interactive and non-interactive sources. The framework applies to both of them, so the exact difference seems unimportant. I personally found it a bit confusing.

### Components of Information Systems

The framework defines 3 components that aim to describe an information system:

- Notation: The arrangement of symbols with an information system.
- Environment: The tools or operations used to modify that information system.
- Media: The medium it exists within (paper, digital, sound).

Dimensions apply to all 3 at the same time.

Example: For programming languages, notation is the programming languages themselves, environment is the IDE, and the medium is the computer screen.

### Additional Framework Stuff

The framework mentions layers, which refer to the level of the information system that you're interacting with. This seems to refer to the combination of notation, environment and medium. The example given in Source 1 refers a computer program as being in one layer, and your keyboard strokes as existing in another layer.

buuut.... this seems to be the exact defintion of sub-devices, mentioned below.

Sub-devices refer to the sub-devices of an information system that can be isolated out, as they come with a new notation.

Ok, i'm not sure what's the difference between layers and sub-devices, they seem to refer to the same kind of thing.

Ok, I think layers refer to a pair of notation + environment existing in the same medium. While sub-devices exist on a different medium. buuut.. when it refers to the dimension of abstraction, it discusses an abstraction manager (like keyboard shortcuts) as a sub-device. They still exist on the same medium...

I think the difference between layers and sub-devices is more soft and subjective than technical. If something can be treated in isolation, it's a subdevice. if it's part and parcel of another thing, it's a layer.

in any case, sub-devices seem to be the main object of interest.

## The dimensions

> Source 2: A paper by Blackwell et al., available at: https://www.cl.cam.ac.uk/~afb21/publications/CT2001.pdf

> Source 3 (used sparingly): Introduction to Human-Computer Interaction by Horkbaek et al., available at: https://global.oup.com/academic/product/introduction-to-human-computer-interaction-9780192864543?cc=fi&lang=en&

alriii, time to get to the meat and bones of this framework: the dimensions. This seems as the theoretical centerpiece of this framework, as it aims to offer words for usability scenarios.

### "Viscosity: resistance to change"

There are two types of viscosity labeled:

#### Repitition Viscosity

How many actions of the same type (repitition) do I need to complete a particular task?

#### Knock-on Viscosity

When you make a change, and further changes are needed to restore "consistency". For example, lets say you had the list:

1. orange
2. apple
3. watermelon

If you wanted to add mango between orange and apple, you need to later fix the numbers of apple and watermelon by incrementing them, restoring consistency.

### "Visibility: ability to view components easily"

I wanna see the individual components in my system easily.

### "Premature commitment: contraints on the order of doing things"

this seems to be about systems that force you to do things in a particular order. Example: how you have to call hooks at the top of your component, even if you only use some of them sometime later.

### "Hidden dependencies: important links between entities are not visible"

So when one component depends on another, and changing it will have impact on the other. Are those links visible? This relates to visibility, excepts that the relational component is stressed here.

### "Role-expressiveness: the purpose of an entity is readily inferred"

you can easily tell what the entity does. for example, the name of a React component like "Sidebar" easily tells you what it is: a sidebar.

### "Error-proneness: the notation invites mistakes and the system gives little protection"

self explanatory

### "Abstraction: types and avaialability of abstraction mechanisms"

Abstraction: "definitions of underlying notations" (source 2)

Some abstractions come with an abstraction manager: classes in object-oriented programming langauges. Some do not come with abstraction managers.

The paper mentions an important point: "Systems that allow many abstractions are potentially difficult to learn."

### "Secondary notation: extra information in means other than formal syntax"

When a user needs to do something that isn't in the formal notation, the notatin designer gives user a secondary notation to play around with.

The paper gives an example of code comments, or text formatting options to indicate importance.

### "Closeness of mapping: closeness of representation to domain"

How close the notation is to what it is it's mapping. I like to think an example is like excel spreadsheet to actual spreadsheets, or word documents to actual paper documents.

A web-dev example is maybe jsx, with how you can write javascript code and React components and it still looks like HTML - what it's mapped to

### "Consistency: similar semantics are expressed in similar syntactic forms"

a user will sometimes guess the purpose of a component in a notation by relating it to similar components. this dimension relates to how similar similar components are, and ig vice verse would be included in that too.

### "Diffusness: verbosity of language"

how much screen space the notation takes up.

why was it named diffusness and not just verbosity... i don't know.

### "Hard mental operations: high demand on cognitive resources"

refers to the amount of info you're keeping in working memory, and how hard you need to work your brain at it

### "Provisionality: degree of commitment to actions or marks"

Can i quickly explore different options of reaching a particular goal? Example is git, and how it has high provisionality by allowing you to create branches, check them out, cherry-pick, and if you don't like the result, just delete the branch.

### "Progressive evaluation: work-to-date can be checked at any time"

can i, at a particular time, pause, view and get feedback on the work i did?

obvious examples are photo-editing or modelling apps that allow you to save your work or render it at any time.

Source 3 gives a cool example with linters and type checkers which give you feedback while writing code.

## Additional Dimensions

### Juxtaposability

> This is mentioned in an older article by Green and Petre - the most cited paper (as of known) about the CDN framework.
> Source 4: https://www.sciencedirect.com/science/article/pii/S1045926X96900099

This is related to visibility, and it refers to a user's ability to view two components of a system side by side at the same time.

### Creative Ambiguity

The ability to see different ways of doing something within a notation. This is mentioned in Source 2, but also in this chapter from 2005, where it discusses how notation designers leave parts of their notation vauge to encourage creativity.

In the 2005 source, creative ambiguity seems to be looped in with Provisionality, the ability to explore different ways of doing something.

> Source 5: https://scispace.com/pdf/chapter-5-notational-systems-the-cognitive-dimensions-of-4nm1igonbf.pdf

### Free rides

This was a bit more difficult to understand from the sources mentioned, but a 2021 paper provides an easy explanation of it:

> Source 6: https://link.springer.com/article/10.1007/s10849-021-09331-0

In Source 6, it refers to the idea of translating information from one diagram (notation) to another, and how that makes explicit facts there were not originally explicit.

Perhaps a better definition in the world of web-dev is when notations provide a way for users to make explicit hidden or inferred facts. But, this would make it very similar to visiblity and hidden dependencies...

## Pairwise Independence

> Source 1

This refers to the idea that the dimensions are pairwise independent, meaning that you can change a dimension while keeping another constant. However, because of the nature of design and tradeoffs, a third dimension will have to be altered as well.

For example, when writing in Markdown, you can improve the visibility of a system by adding a Markdown preview window, while keeping viscosity constant. However, that knocks down diffuseness as the notation now takes on more screen space.

## Types of Users

Something to note that is indirectly mentioned in the CDN questionairre is the class of users using an application. Are they a beginner, are they an expert? In that sense, they will find different features easier or more difficult.

> Source 7: CDN Tutorial, https://link.springer.com/content/pdf/10.1007/3-540-44617-6_31
> Source 8: Video, CDN applied to JS: https://www.youtube.com/watch?v=aelyKLi30qg&t=13s

This can be generalized to background of user.

## Previous Applications

This framework seems to traditionally be used to evaluate visual programming languages, as shown by Green's landmark paper about visual languages (Source 4).

### Issues of Applying CDN

> Source 8: https://doi.org/10.1016/j.jvlc.2006.04.006

#### A Tool for Problems, not Correctness

The CDN framework should be used to identify usability problems, not prove that a design is moreso correct.

Does that mean using a radar chart for comparison across notations is fallible?

#### Importance as discussing dimensions based on tradeoffs

This is related to the view that there is no perfect design, it is simply a bunch of tradeoffs.

As such, it's important to discuss the dimensions in terms of the tradeoffs being made. These are technically called "design maneuvers".

#### Adding reinterpretations

The problem with adding reinterpretations to the CD's (cognitive dimensions) is that it no longer becomes a shared vocabulary, and it creates confusion for further discussion.

### Case Studies!

These case studies are derived from Source 8. What's interesting about them is they attempt to analyze two main processes:

1. How the application of CDN differs in the beginning of design, middle of design and end of design process

2. The effectiveness of asking Who, What, How as an extension to the CDN framework.

#### Interactive Football Playbook (IFP)

An interactive application that allows coaches to walkthrough American Football plays. In this case, the CDN framework was applied pretty early within the design process: during the paper-prototype stage.

[![Football-paper-prototype](/developer-experience-cdn/images/football-paper-prototype.png)](u)

They used Blackwell's questinairre to drill down on the CDs.

> Source 9: https://www.cl.cam.ac.uk/~afb21/CognitiveDimensions/CDquestionnaire.pdf

How the process worked, is they would hone in on a dimension by going through the questionairre and identifying the issues with the design. Then, once they got to suggesting remedies, this brought up design maneuvers: how can we fix the one design dimension by trading off another design dimension?

An example of this was _visibility_. They realized that, when zooming into the players, the coaches had to use their working memory (extending to _hard mental operations_) to remember the positions of the players outside of the screen. To account for this, they suggested adding another abstraction: a small screen offering a bird's eye view of the play. This screen increased visibility, but it introduced a new sub-device through a new abstraction.

An interesting note is that for some issues, they suggested conducted further interviews to suggest remedies.

Another issue they found with their paper prototype is the non-existence of a secondary notation. They wanted to provide coaches with an "escape from formalism" by allowing them to add notes to formations.

Blackwell's questionnaire also proved useful as it allowed people "with low levels of familiarity with CDs" to pick out issues with the design.

#### Current Adieu

This is a visual language that they had a prototype of, and that they aimed to use CDN to create an improved versin.

[![Adieu Visual Language](/developer-experience-cdn/images/adieu.png)](https://doi.org/10.1016/j.jvlc.2006.04.006)

##### Small Aside About Visual Languages...

As previously mentioned, the CDN framework has been famously used to analyze visual languages. Now, in hindsight, we know that visual languages have never replaced text-based programming.

But... did they fail?

No, we've actually seen many succesful applications of visual languages in particular domains. The famous example is Scratch, and it's power as an educational tool. There are other ones as well, which you can check out here:

> Source 10: https://www.jointjs.com/blog/visual-programming

Also, a domain that visual programming has been succesful in is AI orchestration. Tools like n8n and Langflow have skyrocketed in popularity by allowing non-code folks to encode in common workflows.

Why do visual languages work sometimes?

I think the missing key here is that there needs to be a way to compare a potential tool (like a visual language) to existing, mainstream tools.

It's easy to understand why tools like Scratch and n8n were succesful is because they offered better usability than existing (text-based) solutions.

Limiting yourself to CDN would help you improve a design, but not tell you how it ultimately compares to what's already out there.

Moreover, CDN cannot be used as a comparison tool because it doesn't tell you anything about correctness, as previously mentioned.

---

An interesting point in their work is they used TAG to measure consistency across prototypes. TAG is discussed in the following source:

> Source 11: https://scispace.com/pdf/task-action-grammars-a-model-of-the-mental-representation-of-1k271becjq.pdf

Another interesting point is that, in their case, error-proneness and viscosity was often discussed together. This makes sense becasue if you need to do a lot of work to modify something (viscosity), then it's likely error-prone (will lead to errors). Error-proness was also discussed together with hard-mental operations.

Something that I noticed here and in the previous case-study is that, after going through the questionairre, they seemed to discuss issues usually through multiple dimensions. That is, an issue probably appeared in the questionairre in mulitiple dimensions, so they discussed it in terms of these mutliple dimensions.

#### SkinBuilder

SkinBuilder is a WYSIWYG (What you see is what you get) editor for graphs. It's intended for graphic designers in software dev teams.

[![Skin Builder Graphs](/developer-experience-cdn/images/SkinBuilder.png)](https://doi.org/10.1016/j.jvlc.2006.04.006)

At the end of a design, the CDN evaluators picked up on issues that were related to the intended audience.

For example, they were confused by the rectangular boxes at the top of the interface as they didn't know what they did (role-expressiveness). Also, they had issues with font editing, where they had the `bold` menu item to consist of choices of true and false (closeness of mapping) (lol).

[![skinbuilder bold option](/developer-experience-cdn/images/skinbuilder-bold.png)](https://doi.org/10.1016/j.jvlc.2006.04.006)

A key element here is that they suggested the use of _personas_ as a way to mitigate this. Personas would allow you to detail information about your user (what kind of person they are) and dedicate your product to them.

They also didn't have an undo feature (error-proneness, closeness of mapping). Although these mistakes are funny, one has to remember the importance of conducting user studies (and a CDN analysis) early. In this case, the undo button was a taxing addition, and the team wasn't willing to implement it before the app's release.

### Who, When and How

The study that showcased the case-studies emphasised the who, when and how aspects of a CDN analysis.

It's important to remember that the framework provides the means, but not the method of evaluation. This means that it provides a series of concepts and how they relate, without telling you how to apply them. As such, the CDN questionairre created by Blackwell provided a way of applying the framework.

To make that application more complete, Dagit et al. added: who, when and how, as factors of governance. The who refers to who is doing the CDN analysis. The when refers to what part of the design process is the CDN analysis being applied. The how refers to how the CDN framework is being applied (questionairre).

They stressed that the _who_ helps mitigate bias and tunnel vision, the _when_ helps estimate the effectiveness of the CDN analysis, while the _how_ helps ensure that the CDN framework is being used correctly (not to prove correctness of design).

### Structure of CDN Analysis by Dagit et al.

So this is a rough sketch of what Dagit et al. CDN analysis might've looked like.

1. identify who, when and how
2. go through questionairre and each dimension
3. consolidate specific issues in dimensions into general issues
4. Discuss design maneuvers in terms of dimension tradeoffs.

## Applying it on Google Docs!

To practice using the CDN framework, we can apply it on the word processor: Google Docs!

[![google docs editor](/developer-experience-cdn/images/google-docs-1.png)](docs.google.com)

### Who, When, How

- _Who_: Me, an external reviewer, and an avid reviewer of Google Docs
- _When_: After the product was released... like really after.
- _How_: Using the CDN questionairre, and Personas

### Persona

Mike Jacobs, about 30 years ago. Works an administrative office job where he spends most of his time editing and reviewing docs, and sometimes creating new ones. He's moderately tech savvy, spending half 4 hours of screen time on his phone, and another 7 hours on his computer. In his free-time, he skateboards around his local park.

![Mike Jacobs](/developer-experience-cdn/images/mike-jacobs.jpg)

### CDN Questionairre

#### Visibility

```
How easy is it to see or find the
various parts of the notation while
it is being created or changed?
Why? What kind of things are more
difficult to see or find?
```

By default, it's pretty easy to see various aspects of the page, especially the place you're editing. You can zoom in and zoom out, and increase or decrease the font size.

However, working on a larger document with many pages, it's hard to keep track of where specific pages are. (Hard mental operaitons). To mitigate this, Google docs offers various design maneuvers.

- (Abstraction) The ability to style headings as Heading 1, Heading 2, etc... such that they appear on the left hand side of your view.
  - However, that can be tedious (viscosity, premature commitment) if you haven't used headings before, and you want to add it at a later time. But, once again, Google Docs offers the tool _select matching text_ to select matching texts so you can set them all in one go.

- (Abstraction) The Find tool, which allows you to find specific words. However, you still have to remember what words were in the page you were looking for (hard mental operations), and you might have to skip over several false-positives - matching words that weren't in the page you were looking for (viscosity)

```
If you need to compare or
combine different parts, can you
see them at the same time? If not,
why not?
```

I guess you can duplicate the tab and position them side by side. You also see the edits being made in one tab on the other (highlighted by a different colored cursor). This is also a similar operation that people do sometimes, so it feels natural.

#### Viscosity

```
When you need to make changes
to previous work, how easy is it to
make the change? Why?
```

It's pretty easy to make changes to previous work as we're dealing with a WYSIWYG editor. Moreover, when working collaboratively, it's easy to add _comments_ or _edits_ for stuff that you want modified.

You can also edit headings easily by using the option _edit style to matching text_.

```
Are there particular changes that
are more difficult or especially
difficult to make? Which ones?
```

If you want to bold/highlight/style all specific instances of a word, you have to select each word individually. - There's an addon called Advanced Find & Replace that seems to do this for you.

Also, if you're using footnotes, and you want to refer to an existing footnote, you have to manually add a superscript to a word, which is also tedious. However, it must be noted that referring to the same footnote in a page is not conventional, at least in some citation styles like Chicago (CMS).

Note, I was gonna talk about the ability to use VIM bindings with Google Docs, but then I realized Mike Jacobs (our persona) probably doesn't know VIM.

Mike sometimes tries to space pieces of text equally on a line.

- There's a bit of a hack for this (Novel), where you add a table and hide the outline. The problem with this, however, is that each piece of text is granted the same space, so it's not really equidistant if some text is larger than others. Here's an example:

```
longer-text    short          short
```

As shown, each piece of text is allocated 15 spaces, and the spaces between each word are not equal because of the longer first word.

Also, adding captions to images, which is an expected task, isn't that simple in google docs. You have to mess around font styles and even the _drawing_ abstraction.

#### Diffuseness

```
Does the notation a) let you say
what you want reasonably briefly,
or b) is it long-winded? Why?
What sorts of things take more
space to describe?
```

it's a WYSIWYG editor, so it's prety simple. You just type and the words appear on your screen.

There looks like there's even AI integration so it's even brief-er to say what you want lol

#### Hard Mental Operations

```
What kind of things require the
most mental effort with this
notation?
```

Nothing (that wasn't aforementioned, like in visibility) takes any mental effort. ~~Mike Jacobs can listen to Reddit AMAs while cruising through Google Docs.~~ Although, it's worthwhile to mention that writing itself is sometimes mentally taxing. This isn't really a problem with Google Docs, however, as this problem exists across different mediums.

```
Do some things seem especially
complex or difficult to work out in
your head (e.g. when combining
several things)? What are they?
```

No, not realy.

#### Error Proneness

```
Do some kinds of mistake seem
particularly common or easy to
make? Which ones?
```

I think a lot of easy mistakes occur with images. When you paste an image into google docs, and you try to move it (a natural, second operation), it doesn't feel like it's moving... That's because the default image formatting option is _in-line_. This means that the image is formatted in line with the rest of the text. So, if there's no text in the direction you're moving the picture, the picture won't move.

- The intended next step is to change the image formatting to _break text_. That works.
  - However, when you paste another image above or below it, one of the images might flow down to the footer of the bage and get cut-off by the page border, instead of flowing on to the next page with the rest of the text.

_Wrap text_ option for images seems the most stable, as errors are bound to happen with other options like break text.

```
Do you often find yourself making
small slips that irritate you or
make you feel stupid? What are
some examples?
```

After selecting an image, and if you went to click on the end of the next line, you might accidentally click on the scroll bar, which flings you down several pages.

#### Closeness of Mapping

```
How closely related is the notation
to the result that you are
describing? Why? (Note that in a
sub-device, the result may be part
of another notation, rather than the
end product).
```

my guess is that Google docs is supposed to mirror a typewriter type of system, where you have a keyboard, and with each key stroke, the letters appear on the paper in front of you.

turns out a lot of typewriters didn't have a real _backspace_, as that button would just move you back one character without erasing anything.

Mike jacobs (about 30 years old) prob didnt use a typewriter, as the computer existed. it makes a lot more sense to discuss the second question (below), where we discuss closeness of mapping to existing products like Microsoft word

```
Which parts seem to be a
particularly strange way of doing
or describing something?
```

In terms of closeness of mapping to existing products (Microsoft Word), it feels very similar. the basic setup of a page with a home tab above it displaying text styling options is universal.

#### Role Expressivevness

```
When reading the notation, is it
easy to tell what each part is for in
the overall scheme? Why?
```

Super niche knitpick, but when you have an _outline_ open on the left hand of your screen, and one of the sections has a comment, it shows up as a `1` indicator next to the section title. If you were to click on it, it doesn't do anything. As a user, i'd expect it to take me to the comments section.

The actual comments section is on the top right of the screen. It's not the most expressive icon in the world, b/c it doesn't exactly look like your round, conventional speech bubble.

![google docs top bar](/developer-experience-cdn/images/google-docs-top-bar.png)

```
Are there some parts that are
particularly difficult to interpret?
Which ones?
```

Everything seems pretty expressive tbh

```
Are there parts that you really
don't know what they mean, but
you put them in just because it's
always been that way? What are
they?
```

There's also the Gemini icon on the top right, but as gemini becomes increasingly popular, it's become ubiquitious

#### Hidden dependencies

```
If the structure of the product
means some parts are closely
related to other parts, and changes
to one may affect the other, are
those dependencies visible? What
kind of dependencies are hidden?
```

An example of a dependency is comments. When you add a comment to a piece of text, it's highlighted and the comment appears besides the document mergins. if you click on the yellow text or the comment on the side, either component is highlighted.

Another dependency is heading styles and how updating a style affects all headings, but that's made very explicit, since you have to click the button to update the style.

```
Do these dependencies stay the
same, or are there some actions
that cause them to get frozen? If
so, what are they?
```

this reminds of another dependency: heading styles and table of contents. Adding a heading should (expectedly) automatically update a table of contents. However, you actually have to go back to the table contents and click the refresh button to get the latest updates.

- A design maneuver could be to create semantic heading groups that don't show up on the actual document, as they solely exist on the table of contents and the _outline_ list on the left hand side of the screen. This allows a viewer to quickly get a sense of what's in the page before picking the section i wanna check out.
  - This presents a problem with closeness of mapping since this is a novel solution that some folks may not be familliar with.

```
In what ways can it get worse
when you are creating a
particularly large description?
```

When you have a very large table of contents, it might flow into a second page, and it becomes hard to understand since there's so many items. I guess that's a problem on the document designer, but yea...

There's no option to hide specific headings from the table of contents. You can remove heading levels, though. Honestly, in terms of consistency and visibility, this seems like the better design maneuver.

### Progressive Evaluation

```
How easy is it to stop in the
middle of creating some notation,
and check your work so far? Can
you do this any time you like? If
not, why not?
```

Very easy. you just stop lol

```
Can you find out how much
progress you have made, or check
what stage in your work you are
up to? If not, why not?
```

yes, bc it's a WYSIWYG editor and you can just scorll

```
Can you try out partially-
completed versions of the
product? If not, why not?
```

Yes.

#### Provisionality

```
Is it possible to sketch things out
when you are playing around with
ideas, or when you aren't sure
which way to proceed? What
features of the notation help you
to do this?

What sort of things can you do
when you don't want to be too
precise about the exact result you
are trying to get?
```

you can use stuff like bullet points or just rough notes to do that.

You can also add in some headings and fill in some work as you go

Finally, Google Docs has this feature called _tabs_ where you can create multiple tabs within a single document. So you can put your notes on one tab, and do your real work on another. Then, when you export, you can select the specific tab that you'd wanna export

Also, Google docs keeps a history of your document changes, so if you dislike a particular result, you can theoritcally restore a previous version, and you can even restore it as a copy. However I seldom do that. I would imagine Mike Jacobs agrees with me as well.

#### Premature Commitment

```
When you are working with the
notation, can you go about the job
in any order you like, or does the
system force you to think ahead
and make certain decisions first?

If so, what decisions do you need
to make in advance? What sort of
problems can this cause in your
work
```

Yes, you need to be sure if you want to style a particular word or phrase in a particular style. This is because it's tedious (viscosity) to later change the style of every instance of a word. Yes, there are extensions like Advanced Find and Replace, however, if you're really tied up in a jam.

But, for most of everything else, you dont need to make any decisions in advance.

#### Consistency

```
Where there are different parts of
the notation that mean similar
things, is the similarity clear from
the way they appear? Please give
examples.
```

They are usually placed next to each other. Text styling options are placed together in the home tab, text formatting options in the formatting tab, and heading styles next to each other.

A lot of collaborative options are also placed in the same general area: the top right of the screen (history, comments, video/present, share).

```
Are there places where some
things ought to be similar, but the
notation makes them different?
What are they?
```

If you were to move an image with the formatting option _wrap text_, you get a minimal blue cursor that goes down the text. However, with an image with the formatting option _break text_, you see the whole silhouette of the image moving with you (visibility). The small blue cursor is hard to see, and it's different compared to an adjacent formatting option.

Another knitpick is that the Find and Replace tool is in the edit tab instead of the tools tab, where you can find tools like Word Count and Dictionary

The Gemini tool icon is also placed in a weird place; it's next to the collaborative tool options... oh, i understand the connection. You're collaborating with Gemini, that's why it's there. lol, that's interesting, because I never viewed using AI as collaborating; it's just a tool that gives me output.

- I might move it to the right sidebar, where other tools are shown like Calendar, To do lists and Google Maps. Yes, it might not get the same attention, but it's a better fit imo.

![google docs top right sidebars](/developer-experience-cdn/images/docs-top-right.png)

#### Secondary notation

```
Is it possible to make notes to
yourself, or express information
that is not really recognised as part
of the notation?
```

```
If it was printed on a piece of
paper that you could annotate or
scribble on, what would you write
or draw?
```

```
Do you ever add extra marks (or
colours or format choices) to
clarify, emphasise or repeat what
is there already? [If yes: does this
constitute a helper device? If so,
please fill in one of the section 5
sheets describing it]
```

### Notes while applying CDN questionnaire

- The multiple questions for each dimension sometimes felt redundant because they asked about very similar things. However, I realized that it intends to somewhat reword itself in different ways to better help you remember the components in the system.

- On that note, I feel a lot of my time was spent remembering all the different ways I've used Google docs. As an aid, perhaps one could start by listing out all the different components of the notation before going through the dimensions.
  - Lets try that. Here are the components for Google docs:
    - text editting (WYSIWYG editor, find and replace)
    - text styling (style, font, size, heading styles)
    - text formatting (alignment, margins)
    - images
    - tables
    - collaboration (comments, history, share)

- In that regard, the more components a system has, the more tedious the CDN questionnaire felt.

- it definitely feels like 14 dimensions is a loooot. I understand that the 14 dimensions are meant to be hoslitic and cover like >95% of the product. But, for the person conducting the CDN questionnaire, and for the person reading the results, it definitely feels a lot.
  - Dagit et al. synthesized the questionairre into issues that sometimes touched upon multiple dimensions. They also grouped the issues into sections. This made the analysis a lot more digestible.
  - If i were to conduct the questionnaire to review multiple products within an ecosystem, i'd wanna cut it down to like... 3 dimensions lol. alri maybe 5 to be more holistic. As a team, however, it does make more sense to go through all dimensions and compare _issues_ to ensure the concise dissemination of results.
  - im about halfway down the questionnaire, and the dimensions that seem the most important in general are:
    - visibility: the need to step back and view the system or its subpart in whole.
    - viscosity: being able to make amends easily
    - diffusness: being able to make changes concisely
    - Hard mental operations: being able to create without too much mental complexity
    - Provisionality: being able to sketch something out quicklky
    - abstraction: the aides that the system provides to manipulate underlying notations
  - The aforementioned dimensions will be a lot less heavy-handed, but aim to provide a good enough picture. Moreover, other dimensions may show up (although not entirely) in them:
    - Error proneness is likely to appear in viscosity, diffusness and hard mental operations.
    - closeness of mapping is likely to appear in hard mental operations and abstraction.
    - role expressiveness may appear in visibility, hard mental operations, abstraction
    - hidden dependencies may appear in visibility, hard mental operations and abstraction
    - progressive evaluation may appear in provisionality
    - premature commitment may appear in viscosity and hard mental operations
    - consistency may appear in abstraction
    - secondary notation may appera in provisionality
    - novel may appear in viscosity, diffusness and hard mental operations.

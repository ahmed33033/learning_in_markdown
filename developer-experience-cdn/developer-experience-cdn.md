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

#### Interactive Football Playbook (IFP)

An interactive application that allows coaches to walkthrough American Football plays. In this case, the CDN framework was applied pretty early within the design process: during the paper-prototype stage.

[![Football-paper-prototype](/developer-experience-cdn/images/football-paper-prototype.png)](https://doi.org/10.1016/j.jvlc.2006.04.006)

They used Blackwell's questinairre to drill down on the CDs.

> Source 9: https://www.cl.cam.ac.uk/~afb21/CognitiveDimensions/CDquestionnaire.pdf

How the process worked, is they would hone in on a dimension by going through the questionairre and identifying the issues with the design. Then, once they got to suggesting remedies, this brought up design maneuvers: how can we fix the one design dimension by trading off another design dimension?

An example of this was _visibility_. They realized that, when zooming into the players, the coaches had to use their working memory (extending to _hard mental operations_) to remember the positions of the players outside of the screen. To account for this, they suggested adding another abstraction: a small screen offering a bird's eye view of the play. This screen increased visibility, but it introduced a new sub-device through a new abstraction.

An interesting note is that for some issues, they suggested conducted further interviews to suggest remedies.

Another issue they found with their paper prototype is the non-existence of a secondary notation. They wanted to provide coaches with an "escape from formalism" by allowing them to add notes to formations.

Blackwell's questionnaire also proved useful as it allowed people "with low levels of familiarity with CDs" to pick out issues with the design.

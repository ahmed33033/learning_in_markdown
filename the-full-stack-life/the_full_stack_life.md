# The Full-Stack Life

Most of the information here is originally based out of the CSC309 course by Professor Kianoosh. External sources are added where relevant. Clicking images will redirect you to their original source.

## Computer Talk for Dummies

For computers to talk to each other, they need an identifier. Think about how we use _names_ to call each other; computers need a name of their own as well.

Every computer that joins a network is given an identifier called an IP (Internet Protocol) Address. There are 2 main _versions_ of IP addresses:

- IPv4, where IP addresses are made up of 32 bits
- IPv6, where IP addresses are made up of 128 bits

Additionally, every computer has various logical (not hardware) channels called ports that an application can use to _listen_ in for a connection.

So, one computer to initiate contact with another, it will have to specify both an IP Address, and a port number!

> Side-note: Every computer has a local network with IP Addresses called loopback IP Addresses. These addresses identify the same computer.

The computer that sends in _requests_ is called a client, and the computer that is listening for requests is called a server. The server responds back with a _response_.

### DNS Servers

We can call the name of the website its domain name. When we type up its name and search for it, its IP Address and Port Number are looked up in Domain Name Servers (DNS). Moreover, so we don't end up with a chicken-egg problem, our computers know which DNS Server to reach out to.

## Network Primer

Here's a lil network primer before diving into more network talk.

A network is composed of 2 or more connected computers that share data with one another ([Britannica](https://www.britannica.com/technology/computer-network)).

The internet is composed of a series of connected networks.

The most common/official way that computers communicate data with one another is using the TCP/IP Protocol. This Protocol can be modeled with the _4-layer model_, which helps us better understand it:

<figure>
<a href="https://medium.com/@kylelzk/networking-theory-understanding-tcp-ip-the-backbone-of-the-internet-c435f50d7a9a"><img src="images/4-layer-model.png" alt="4-layer model"></a>
<figcaption>Source: Kyle Law, 2023</figcaption>
</figure>

**Example:**

When a web browser sends in a request, it starts off at the applicaiton layer with HTTP. Then, an HTTP message is packetized in the TCP layer. The destination server of each packet is then labeled using the IP layer. These packets are then sent over the Network Interface layer which actually transmits these packets from one computer to the next.

Example Source: [Lauren Dagworthy](https://www.youtube.com/watch?v=KEWe-5Bk3Q0&t=157s)

## Stateful and Stateless

Stateful means that we're keeping track of a client's past requests. Stateless means that every request is treated as a new request.

- TCP (Transmission Control Protocol) in the Transport Layer sets up a 2-way connection between 2 computers. Its stateful because it ensures that packets are transferred reliably.

- HTTP (Hypertext Transfer Protocol) in the Application Layer (runs over TCP) can be stateless if it doesn't keep of client requests (doesn't keep track of the server state).

Once a connection ends in TCP, the state data is lost.

## HTTP Messages

HTTP messages can be thought of strings in a special format.

HTTP messages are what the HTTP protocol uses to exchange data between a server and a client. HTTP messages are either requests or responses. They are made up of a header and a body.

HTTP method specifies the type of request that is being made. For example:

- **GET**: Signifies a READ operation
- **POST**: Signifies a CREATE operation
- **PUT**: Signifies an UPDATE operation
- **DELETE**: Signifies a DELETE Operation

The part of the url that comes after the domain name and slash is called the path. Use it to specify a specific page in a website.

HTTP always runs on port 80. The web browser helps render a variety of data types, including HTML.

> Additional Sources:
>
> - [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages)
> - [Contrive](https://www.contrive.mobi/aviorapi/HTTPMETHODS.html)

### HTTP Response Status Codes

- 200-299: Succesful
- 300-399: Redirection
- 400-499: Client Errors
  - 400: Bad Request
  - 403: Permission Denied
  - 404: Page Not Found
- 500-599: Server Errors
  - 500: Internal Server Error

## The Amazing World of HTML

An example file was added to `code_examples/index.html` that showcases the information summarized below.

### Basic Structure

You start off with a `<!DOCTYPE html>` tag.
You then add a pair of `<html>` tags with the starting: `<html lang="en">`

The `<html>` tag has 2 pairs of attributes: `<head>` `</head>` and `<body>` `</body>`
The `<head>` tag has a series of important meta tags. `<meta charset="UTF-8">` is one.
The `<body>` tag is where you define everything visible in the page.

Void elements are elements that cannot have child elements.

### Styling with CSS

The style attribute in an HTML tag is used to declare CSS styles. You can also add the `<style>` tag in the `<head>` pair of tags. Additionally, you can use the `<link>` tag to include an external CSS file.
**Example**: `<link rel="stylesheet" href='my_css_sheet.css">`

The ID attribute is to identify an individual HTML tag. The class attribute can be used to identify a series of HTML tags.

### divs and spans

Divs as a container for multiple HTML elements. Spans for inline text.

### Forms

The "primary" way to send user input as a request to a server.

When defining a `<form>` tag, its tradition to also define 2 attributes alongside it: _action_ and _method_. The action attribute defines the destination URL that will be used after the user clicks submit. The method attributes defines whether the http request method. Usually its GET or POST. GET is used for non-sensitive data because its apppended to the URL.

There are many different types of user input: like `<input type: "radio">` and `<input type: "button">`
The `<label>` tag is used to label input tags using an ID.

You can then use the `<button>` tag with type="submit" to submit a form.

## Skiing into CSS

Let's finally learn what this whole CSS stuff is about!

### CSS Box Model

When styling an HTML element, we've ought to keep the box model in mind. You start with the **content**, which is surrounding with **padding**, which, in turn, is surrounded with **border**, before being surrounded with **margins**. Here's a pic:

<figure>
<img src="https://web.dev/static/learn/css/box-model/image/a-diagram-showing-four-m-af72960a9e79a.svg" alt="box model"/>
<figcaption>CSS box model from web.dev</figcaption>
</figure>

### CSS Selectors

This seems like a really important topic! 👀

The source for this section is: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)

#### Type Selectors

Pretty simple. If you want to style a particular HTML tag/element, you just go:

```css
h1 {
  color: blue;
}
```

#### Class Selectors

Again, pretty simple.

```css
.my_class {
  font-family: Impact;
}
```

##### Multiple Classes

In HTML, you can give an element mulitple classes by using a space character. For example:

```html
<h1 class="foo bar">Hii</h1>
```

Then, in CSS, you can specify elements with multiple classes with:

```css
.foo.bar {
  font: 3em;
}
```

##### Type + Class Selectors

You can combine both of them, and select HTML elements that have a particular class.

```css
h1.my_class {
  color: red;
}
```

#### ID Selectors

Use a hashtag.

```css
#foo {
  background-color: purple;
}
```

##### Type + ID Selectors

Simple as _THAT_.

```css
h1#foo {
  margin: 2;
}
```

#### Selector Lists!

To select multiple tags/classes/ID's at once, then you go:

```css
h1,
#foo,
.my_class {
  margin-top: 10px;
}
```

#### UNIVERSAL

The universal selector selects all elements.

```css
* {
  color: red;
}
```

#### Attribute Selectors

You can select elements with a particular attribute with:

```css
a[href] {
  text-decoration: none;
}
```

## Scripting in JavaScript

A language that was reportedly made in 10 days.

It's interpretted at runtime by the browser, which has a runtime interpretter.

- Not exclusive to the client side, it's also in the server side.

Has 6 datatypes:

- string
- number
- object
- function
- undefined
- boolean

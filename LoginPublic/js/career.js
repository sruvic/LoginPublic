function divContent () {

let div = document.createElement('div');

div.className = 'row';

div.innerHTML = `<form action="javascript:" onsubmit="alert('Your message here, or, run a function from your JavaScript file and do more stuff!!')">
  <label for="name">Name:</label>
  <input type="text" name="name" id="name" value="Mickey Mouse">
  <br>
  <label for="email">Email:</label>
  <input type="text" name="email" id="email" value="mickey@mouse.co.uk">
  <br><br>
  <input type="submit" value="Submit">
</form> `

document.getElementsByTagName ('body')[0].appendChild(div);

};
const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 5000);
}

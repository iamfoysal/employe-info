const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 5000);
}


// var form_options = { target: '#modal', success: function(response) {} };
// $('#news-create').ajaxForm(form_options);

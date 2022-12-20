
 function login() {
   var password = document.getElementById("pass").value;
   if(password == 'codered'){
      document.write("Correct Password!!");
      window.location.replace('bot.html');
   }
   else{
      document.write("Incorrect password");
   }

}



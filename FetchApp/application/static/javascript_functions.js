function redirectUser(id){
window.location.href = 'http://127.0.0.1:5000/edituser/'+ id;
}

function redirectDog(id){
window.location.href ='http://127.0.0.1:5000/editdog/'+ id;
}

function redirectCancel(id){
window.location.href ='http://127.0.0.1:5000/account/'+ id;
}

function removeDog(id){
service.remove_dog(id)}